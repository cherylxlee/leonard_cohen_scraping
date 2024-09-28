import sys
from bs4 import BeautifulSoup
import requests
import argparse
import numpy as np
import re


def get_content_soup_from_url(url):
    result = requests.get(url)
    content = result.text
    return BeautifulSoup(content, "lxml")


def clean_text(text):
    """Given a string of text return clean text
    Clean issues with text
    "1. Hola" --> "Hola" 
    "Hola." --> "Hola" 
    "Hola (L)" --> "Hola"
    "Hola (1790)"  --> "Hola"
    "Hola 1790"  --> "Hola"
    """
    text = re.sub(r"\(.*?\)", "", text)
    
    text = re.sub(r"[0-9]", "", text)
    
    text = text.replace(".", "")
    
    return text.strip()


def process_row(row):
    """ Inputs a row of a table and returns the song, album and url

    The input should follow this format:
        <tr valign="bottom">
        <td align="left">
        Ain't No Cure For Love </td>
        <td align="left">
        <a href="album9.html" style="text-decoration:none">I'm Your Man (L)</a> </td>
        </tr>
    Ouputs: three strings, as shown in the example
        "Ain't No Cure For Love", "I'm Your Man", "album9.html"

    To ensure cleanliness and avoid duplicates, the following actions are performed:
      -- remove "(L)"
      -- remove years
    from album names and song names
    """
    td = row.find_all("td")
    album_content = td[-1].find("a")
    
    song = clean_text(td[0].text.strip())

    if album_content:
        album = clean_text(album_content.text.strip())
    url = album_content.get('href')

    return song, album, url


def get_albums():
    """ Scrape album names from 
    "https://www.leonardcohenfiles.com/songind.html"

    Return a list of unique names in alfabetical order
    To ensure cleanliness and avoid duplicates, the following actions are performed:
      -- remove "(L)"
      -- remove years
    """
    url = "https://www.leonardcohenfiles.com/songind.html"
    soup = get_content_soup_from_url(url)
    tables = soup.find_all('table')
    t = tables[1]
    rows = t.find_all("tr")

    albums = set()
    for row in rows:
        _, album, _ = process_row(row)
        if album:
            albums.add(clean_text(album))
        
    albums_list = list(albums)
    
    return sorted(albums_list)


def get_songs():
    """ Scrape song urls from
    "https://www.leonardcohenfiles.com/songind.html"

    Return a list of unique names in alfabetical order
    Some cleaning to avoid duplicates:
      -- remove "(L)"
    """
    url = "https://www.leonardcohenfiles.com/songind.html"
    soup = get_content_soup_from_url(url)
    tables = soup.find_all('table')
    t = tables[1]
    rows = t.find_all("tr")
    
    songs = set()
    for row in rows:
        song, _, _ = process_row(row)
        if song:
            songs.add(clean_text(song))
    
    songs_list = list(songs)
    
    return sorted(songs_list)


def scrape_lyrics_from_url(song, url):
    """ Given a song and a url return the lyric of the song
    
    Inputs:
       song: string example: "Bird on the Wire"
       url: 'https://www.leonardcohenfiles.com/album2.html'
    
    Return the text of the lyrics:
    
    Like a bird on the wire,
    like a drunk in a midnight choir
    I have tried in my way to be free.
    Like a worm on a hook, 
    ...
    
    """
    try:
        soup = get_content_soup_from_url(url)
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

    song_tables = soup.find_all("table")
    song_table = song_tables[2]
    song_names = song_table.find_all("h2")
    song_lyrics = song_table.find_all("blockquote")

    for i in range(len(song_names)):
        if song.lower() == clean_text(song_names[i].text.strip()).lower():
            return song_lyrics[i].text.strip()
        
    return None


def get_lyrics(s):
    """ Given an input song scrape and return the lyric
    """
    URL_PREFIX = "https://www.leonardcohenfiles.com/"
    url = "https://www.leonardcohenfiles.com/songind.html"
    soup = get_content_soup_from_url(url)
    tables = soup.find_all('table')
    t = tables[1]
    rows = t.find_all("tr")
    
    for row in rows:
        song, album, url = process_row(row)
        if song.lower() == s.lower():
            return scrape_lyrics_from_url(song, URL_PREFIX+url)
        
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", help="Generates a list of songs", action='store_true')
    parser.add_argument("-a", help="Generates a list of albums", action='store_true')
    parser.add_argument("-l", help="Print lyrics for a given song", type=str)
    args = parser.parse_args()
    if args.s:
        songs = get_songs()
        for song in songs:
            print(song)
    if args.a:
        albums = get_albums()
        for a in albums:
            print(a)
    if args.l:
        lyric = get_lyrics(args.l)
        if lyric is None:
            print("No lyric was found")
        else:
            print(lyric)

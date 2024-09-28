import sys
from bs4 import BeautifulSoup
import requests

URL_PREFIX = 'https://catalog.data.gov'

def soup_initializer_for_page(url):
    try:
        response = requests.get(url)
        return BeautifulSoup(response.text, "lxml")
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None


def list_of_pairs_for_one_page(url, n):
    soup = soup_initializer_for_page(url)
    items = soup.find_all('div', class_= "dataset-content")
    
    elms = []
    for i in range(min(n, len(items))):
        content = items[i].find('a')
        elms.append((content.text, URL_PREFIX + content.get('href')))

    return elms


def get_next_button_url(soup):
    buttons = soup.find_all('a', class_= "page-link")
    if buttons and buttons[-1].text == '»':
        return URL_PREFIX + buttons[-1].get('href')

    return None


def list_of_pairs(n):
    """ Get first n datasets

    Output: list of (dataset title, url)
    """
    home_url = 'https://catalog.data.gov/dataset?q=&sort=views_recent+desc'
    result = list_of_pairs_for_one_page(home_url, min(20, n))
    remaining = n - len(result)
    current_url = home_url

    while remaining > 0:
        soup = soup_initializer_for_page(current_url)
        if not soup:
            break
        
        next_url = get_next_button_url(soup)
        if not next_url:
            break
        
        new_results = list_of_pairs_for_one_page(next_url, min(20, remaining))
        result += new_results
        remaining -= len(new_results)
        current_url = next_url

    return result[:n]


if __name__ == "__main__":
    n = int(sys.argv[1])
    pairs = list_of_pairs(n)
    for title, url in pairs:
        print(title, url)



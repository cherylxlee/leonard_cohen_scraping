# Scraping with Beautiful Soup
![Beautiful Soup](https://img.shields.io/badge/Beautiful%20Soup-blue)
![Requests](https://img.shields.io/badge/Requests-brightgreen)
![lxml](https://img.shields.io/badge/lxml-orange)

## Overview
This project demonstrates the use of Python for web scraping using the `Beautiful Soup 4`, `Requests`, and `lxml` libraries. It focuses on extracting data from two different websites: a dataset catalog and a music archive. The project includes test cases to validate the functionality of the scraping scripts.

## Features

### 1. Extracting Most Viewed Datasets
This script scrapes the website [Data.gov Datasets](https://catalog.data.gov/dataset?q=&sort=views_recent+desc) to retrieve a list of the top 'n' most viewed datasets. If 'n' exceeds 20, the script scrapes across multiple pages to collect the required dataset URLs.

To verify the functionality of the dataset scraper, use:
```bash
pytest test_most_used_dataset.py
```

### 2. Leonard Cohen Song and Lyrics Information
This script gathers information about Leonard Cohen’s albums and songs from [The Leonard Cohen Files](https://www.leonardcohenfiles.com/songind.html). It provides:

- A list of unique albums by Leonard Cohen, along with links for more information.
- A list of unique songs by Leonard Cohen.
- Lyrics for a specified song when the song title is provided.

#### Usage:
- To get a list of albums:
  ```bash
  python lyrics.py -a
  ```
  Example output:
  ```bash
  Cohen Live
  Dear Heather
  Death Of A Ladies' Man
  Field Commander Cohen
  I'm Your Man
  ```

- To get a list of songs:
  ```bash
  python lyrics.py -s
  ```
  Example Output:
  ```bash
  A Bunch Of Lonesome Heros
  A Singer Must Die
  A Street
  A Thousand Kisses Deep
  Ain't No Cure For Love
  Alexandra Leaving
  ```
  
- To get the lyrics of a specific song:
  ```bash
  python lyrics.py -l "Suzanne"
  ```
  Example Output:
  ```bash
  Suzanne takes you down to her place near the river 
  You can hear the boats go by 
  You can spend the night beside her 
  And you know that she's half crazy 
  But that's why you want to be there 
  And she feeds you tea and oranges 
  That come all the way from China 
  And just when you mean to tell her 
  That you have no love to give her 
  Then she gets you on her wavelength 
  And she lets the river answer 
  That you've always been her lover 
  And you want to travel with her 
  And you want to travel blind 
  And you know that she will trust you 
  For you've touched her perfect body with your mind. 
  
  And Jesus was a sailor 
  When he walked upon the water 
  And he spent a long time watching 
  From his lonely wooden tower 
  And when he knew for certain 
  Only drowning men could see him 
  He said "All men will be sailors then 
  Until the sea shall free them" 
  But he himself was broken 
  Long before the sky would open 
  Forsaken, almost human 
  He sank beneath your wisdom like a stone 
  And you want to travel with him 
  And you want to travel blind 
  And you think maybe you'll trust him 
  For he's touched your perfect body with his mind. 
  Now Suzanne takes your hand 
  And she leads you to the river 
  She is wearing rags and feathers 
  From Salvation Army counters 
  And the sun pours down like honey 
  On our lady of the harbour 
  And she shows you where to look 
  Among the garbage and the flowers 
  There are heroes in the seaweed 
  There are children in the morning 
  They are leaning out for love 
  And they will lean that way forever 
  While Suzanne holds the mirror 
  And you want to travel with her 
  And you want to travel blind 
  And you know that you can trust her 
  For she's touched your perfect body with her mind.
  ```

To verify that the script works as expected, run:

```bash
pytest test_lyrics.py
```

This will ensure that the scraper correctly retrieves album and song information as well as lyrics.

#### Note:
This script currently supports songs listed under album-specific URLs on the website. Other song links may require additional handling due to different URL structures.





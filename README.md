# Scraping with Beautiful Soup

## Overview
This project demonstrates the use of Python for web scraping using the `Beautiful Soup 4`, `Requests`, and `lxml` libraries. It focuses on extracting data from two different websites: a dataset catalog and a music archive. The project includes test cases to validate the functionality of the scraping scripts.

## Features

### 1. Extracting Most Viewed Datasets
This script scrapes the website [Data.gov Datasets](https://catalog.data.gov/dataset?q=&sort=views_recent+desc) to retrieve a list of the top 'n' most viewed datasets. If 'n' exceeds 20, the script scrapes across multiple pages to collect the required dataset URLs.

#### Test Instructions:
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
- To get a list of songs:
  ```bash
  python lyrics.py -s
  ```
- To get the lyrics of a specific song:
  ```bash
  python lyrics.py -l "Suzanne"
  ```

#### Testing:
To verify that the script works as expected, run:

```bash
pytest test_lyrics.py
```

This will ensure that the scraper correctly retrieves album and song information as well as lyrics.

#### Note:
This script currently supports songs listed under album-specific URLs on the website. Other song links may require additional handling due to different URL structures.





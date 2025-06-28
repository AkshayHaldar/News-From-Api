# News Fetcher Script

This is a simple Python script that fetches news articles from the NewsAPI based on a user-provided query. It retrieves the latest news articles related to the topic of interest and displays their titles and URLs.

## Features

- Fetches news articles using the NewsAPI.
- Allows the user to specify the type of news they are interested in.
- Displays the title and URL of each news article.

## Requirements

- Python 3.x
- `requests` library

You can install the required library using pip:

```
pip install requests
```

## Usage

1. Obtain an API key from [NewsAPI](https://newsapi.org/).
2. Replace the `api` variable in `main.py` with your API key.
3. Run the script:

```
python main.py
```

4. When prompted, enter the type of news you are interested in (e.g., technology, sports, business).

## Notes

- The script fetches news articles from a fixed date (2025-05-28) and sorts them by publication date.
- Make sure your API key is valid and has sufficient quota.

## License

This project is licensed under the MIT License.

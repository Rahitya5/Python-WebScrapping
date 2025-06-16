# 🕵️‍♂️ Python Job Scraper using BeautifulSoup & Requests

This Python script automatically scrapes the latest **Python developer jobs** from [TimesJobs.com](https://www.timesjobs.com), filters them based on a skill you're **not familiar with**, and saves matching jobs to individual `.txt` files inside a `posts` directory.

## 🔍 Features

- Scrapes real-time job postings from TimesJobs.
- Filters out jobs that include user-defined **unfamiliar skills**.
- Extracts key job details:
  - Company name
  - Required skills
  - Posting date
  - Direct link to apply
- Saves job listings into separate text files for easy review.
- Runs in an infinite loop, checking for new jobs every few minutes (default: 1 minute).
- Ethical scraping with custom headers (User-Agent).

## 🛠️ Requirements

- Python 3.6+
- `requests`
- `beautifulsoup4`
- `lxml`

Install dependencies using:

```bash
pip install requests beautifulsoup4 lxml

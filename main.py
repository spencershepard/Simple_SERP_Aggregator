import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import urllib.parse
import os

load_dotenv()

def get_search_results(query, result_qty, api_key):
    """Use Scale SERP API to retrieve Google Search Results"""
    # set up the request parameters
    params = {
        'api_key': api_key,
        'q': query,
        'output': 'json',
        'gl': 'ca', # Google location ie. Google.ca vs Google.com
        'num': str(result_qty),
        'include_html': 'false'
    }

    # make the http GET request to Scale SERP
    api_result = requests.get('https://api.scaleserp.com/search', params)

    # return the JSON response from Scale SERP
    return api_result.json()

def get_html(url: str):
    session = requests.Session()
    response = session.get(url, headers={'User-Agent': 'Mozilla/5.0',
                                                        'referer': 'https://www.google.com/',
                                                        'accept': 'text/html,application/xhtml+xml,application/xml'})

    if response.status_code == 200:
        return response.text


def get_headings_from_html(html: str):
    """Parses HTML string and returns a list of the text within header tags"""
    headings = []
    soup = BeautifulSoup(html, 'html.parser')
    heading_tags = ["h2", "h3"]

    for tags in soup.find_all(heading_tags):
        h = tags.text.strip().lower()
        for i in range(25):
            # attempt to remove prefixes from numbered lists
            substrings = [str(i) + '.', str(i) + ")"]  # eg "8)" or "8."
            for s in substrings:
                if s in h:
                    h = h[len(s) + 1:].strip()  # remove the substring and strip whitespace

        headings.append(h)

    if len(headings) > 0:
        return headings

def count_occurrence(a: list):
    """Returns a sorted dictionary representing the count of keys in a list"""
    k = {}
    for j in a:
        if j in k:
            k[j] += 1
        else:
            k[j] = 1

    return dict(sorted(k.items(), key=lambda item: item[1], reverse=False))


if __name__ == '__main__':

    api_key = os.getenv("SCALE_SERP_API_KEY")

    if not api_key:
        input('Enter scaleserp.com API key:')

    search_query = input('Enter search query: ')
    site_qty = input('How many sites should we crawl? ')

    search_results = get_search_results(search_query, site_qty, api_key)
    if search_results.get("request_info").get("success") is not True:
        print("ScaleSERP API request failed.")
    print(search_results.get("request_info"))

    headings = []

    for site in search_results.get("organic_results"):
        html = get_html(site.get("link"))
        if html:
            new_headings = get_headings_from_html(html)
            if new_headings:
                headings += new_headings
                print('Got ' + str(len(new_headings)) + ' headings from ' + site.get("link") + ' "' + site.get("title") + '"')

    sorted_headings = count_occurrence(headings)
    for i in sorted_headings.items():
        print(i[0] + " (" + str(i[1]) + ")  " + "https://google.com/search?q=" + urllib.parse.quote_plus(i[0]))

# Simple SERP Aggregator
 
This was created as a quick way to find common recommendations for things like 'Best SEO Software'.  Typically I would visit a handful of 'Top 10' lists from the first page of google search results, and make note of the recommendations that we made most frequently. This automates that process, by scraping the top search results for any particular query, and showing the most common text within header tags in the HTML.

## Installation
1) install Python 3.10 or later
2) type 'pip install -r requirements.txt' from a command line in the installation directory

You will need an API key from ScaleSERP.com (free for some limited usage; currently 125 free searches per month).  

If you don't want to keep entering your API key for each search, create a .env file in the home directory and add this line: 
SCALE_SERP_API_KEY=add_your_api_key_here

## Usage
1) Type 'python main.py' from a terminal in the installation directory
2) Enter your search query (ie. 'Best Lead Generation Software')
3) Enter the number of sites you would like to scrape. (ie if you enter 50, it will scrape the first 50 results from Google)

## Results
The results aren't perfect, as you'll need to filter out some common headings that aren't names of products.  For example, in the list of results in the below image, 'pros' and 'cons' are not likely what you're looking for, but 'tapfiliate', 'post affiliate pro', etc are valid, seemingly popular products.  

![Sample of results](results-sample.png)
Click the google link to do a web search for the respective result. The number in brackets is the number of occurrences in all scraped pages.

## How to find web design clients
Shameless plug!  I've created the best way to find new clients for web design agencies.  Grape Leads is a powerful marketing tool that helps connect agency owners, marketers and freelancers with the clients who need their services the most.  Find businesses without websites and your next clients:  https://grapeleads.com  
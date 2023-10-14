import requests
from bs4 import BeautifulSoup
import wikipediaapi

def search_wikipedia(query):
    # Create a Wikipedia API object
    wiki_wiki = wikipediaapi.Wikipedia('en')

    # Search for the given query
    page = wiki_wiki.page(query)

    if page.exists():
        # Get the Wikipedia page title and content
        page_title = page.title
        page_content = page.text

        # Print the title and a summary
        print("Title:", page_title)
        print("Summary:")
        print(page_content[:500])  # Print the first 500 characters as a summary
    else:
        print("Page not found on Wikipedia.")

if __name__ == "__main__":
    search_query = input("Enter a word to search on Wikipedia: ")
    search_wikipedia(search_query)

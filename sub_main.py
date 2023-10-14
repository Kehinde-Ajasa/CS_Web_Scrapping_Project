import wikipedia


def search_wikipedia(query):
    try:
        # Set the language for Wikipedia (default is 'en' for English)
        wikipedia.set_lang("en")

        # Search for the given query
        search_results = wikipedia.search(query)

        if search_results:
            # Get the first search result
            result_page = wikipedia.page(search_results[0])

            # Print the title and a summary
            print("Title:", result_page.title)
            print("Summary:")
            print(result_page.summary)
        else:
            print("No results found on Our Database for you")
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation errors by printing options
        print("Disambiguation options:")
        for option in e.options:
            print(option)


if __name__ == "__main__":
    search_query = input("What do you want to search for:  ")
    search_wikipedia(search_query)

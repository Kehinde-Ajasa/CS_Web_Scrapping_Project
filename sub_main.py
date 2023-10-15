import wikipedia  # wikipedia API for ease of development


class SummarizeVersion:
    """OOP style of summarizing web pages"""

    def __init__(self, query):
        """first instance created"""
        self.query = query

    def get_summary(self):
        try:
            # Set the language for Wikipedia
            user_language = input("Which language would you like to learn in: ").lower()
            wikipedia.set_lang(user_language[:2])

            # Search for the given query
            search_results = wikipedia.search(self.query, results = 10, suggestion= True)

            if search_results:
                for index, context in enumerate(search_results):
                    print(f"Topic {index + 1}: {context}")

                display_page = int(input("Select Topic to learn: "))
                # Get the user's page result
                result_page = wikipedia.page(search_results[display_page - 1])
                # Print the title and a summary
                print(f"Title: {result_page.title}")
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
    search_query = input("What do you want to learn about:  ")
    search_instance = SummarizeVersion(search_query)
    search_instance.get_summary()

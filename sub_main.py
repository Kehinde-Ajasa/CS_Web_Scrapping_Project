import wikipedia  # wikipedia API for ease of development
import random

class SummarizeVersion:
    """OOP style of summarizing web pages"""

    def __init__(self, query):
        """Instance created"""
        self.query = query

    def get_summary(self):
        json_dictionary = {}
        try:
            # Set the language for Wikipedia
            wikipedia.set_lang("en")

            # Search for the given query
            search_results = wikipedia.search(self.query,)
            if search_results:

                result_1 = wikipedia.page(search_results[0])
                result_2 = wikipedia.page(search_results[random.randint(1, 5)])
                result_3 = wikipedia.page(search_results[random.randint(6, 10)])

                pages_list = [result_1, result_2, result_3]

                for result in pages_list:
                    json_dictionary[result.title] = result.summary


                print(json_dictionary)
            else:
                print("No results found on Our Database for you")
        except wikipedia.exceptions.DisambiguationError as e:
            # Handle disambiguation errors by printing options
            print("Disambiguation options:")
            for option in e.options:
                print(option)

        except wikipedia.exceptions.PageError:
            print("Sorry one of the pages on our database has an issue\nPlease Try again Later!")


if __name__ == "__main__":
    search_query = input("What do you want to learn about:  ")
    search_instance = SummarizeVersion(search_query)
    search_instance.get_summary()

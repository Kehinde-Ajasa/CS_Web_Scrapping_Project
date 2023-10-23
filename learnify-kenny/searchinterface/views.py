from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import wikipedia  # wikipedia API for ease of development
import random

# Create your views here.

def index(request):
    return render(request, 'searchinterface/index.html')

@csrf_exempt
def display_search(request, userinput): 
    # 
    json_dictionary = {}
    # 
    try:
        # Set the language for Wikipedia
        wikipedia.set_lang("en")
        # Search for the given query
        search_results = wikipedia.search(userinput)
        # 
        if search_results:
            # 
            result_1 = wikipedia.page(search_results[0])
            result_2 = wikipedia.page(search_results[random.randint(1, 5)])
            result_3 = wikipedia.page(search_results[random.randint(6, 8)])
            pages_list = [result_1, result_2, result_3]
            # 
            for result in pages_list:
                json_dictionary[result.title] = result.summary
            return JsonResponse(json_dictionary, status = 200)
            # 
        else:
            message = {"message": "No results found on Our Database for you" , "status": 400}
            return JsonResponse(message, safe = False)
            # 
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation errors by printing options
        message = {"message": "Disambiguation request" , "status": 400}
        return JsonResponse(message, safe = False)
        # 
    except wikipedia.exceptions.PageError:
        message = {"message": "Sorry one of the pages on our database has an issue. Please Try again Later! ", "status": 400}
        return JsonResponse(message, safe = False)



    

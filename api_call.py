from langchain.tools import tool
from langchain_core.utils.function_calling import convert_to_openai_function
import os
import json
import requests

class rapidapi_functions():
    def __init__(self):
        super(rapidapi_functions).__init__()
        self.tool_names = []
        self.functions = []
        finish_func = {
            "type": "function",
            "function": {
              "name": "Finish",
              "description": "If you believe that you have obtained a result that can answer the task, please call this function to provide the final answer. Alternatively, if you recognize that you are unable to proceed with the task in the current state, call this function to restart. Remember: you must ALWAYS call this function at the end of your attempt, and the only part that will be shown to the user is the final answer, so it should contain sufficient information.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "return_type": {
                          "type": "string",
                          "enum": ["give_answer","give_up_and_restart"],
                      },
                      "final_answer": {
                          "type": "string",
                          "description": "The final answer you want to give the user. You should have this field if \"return_type\"==\"give_answer\"",
                      }
                  },
                  "required": ["return_type"],
              }
            }
        }
        self.functions.append(finish_func)

    def get_current(power: int) -> int:
          """This API can be used to convert UK standard electrical units of measurement. Currently this is limited to the conversion of Power (in Watts) to and from Current (in Ampheres)."""
          url = 'https://electrical-units.p.rapidapi.com/power_to_current/single_phase'
          
          params=  {
            'power': power,
            'voltage': '230',
            'powerfactor': '0.95'
          }
          headers = {
            'X-RapidAPI-Key': 'b7bff29dbamsh733868f06fac1c1p127433jsn7f88eb1c6e12',
            'X-RapidAPI-Host': 'electrical-units.p.rapidapi.com'
          }
          response = requests.get(url, headers=headers, params=params)
          return response.json()

    def add(a: int, b: int)-> int:
        """
        add num1 and num2, both integers
        """
        url = f"https://adder3.p.rapidapi.com/add/"
        querystring = {'num2': a, 'num1': b, }
        
        headers = {
                "X-RapidAPI-Key": "vb3ES6u4KJdPrGDBcQUiszCxpl5tjZAyagIMqX9o1WwTY7OFLV",
                "X-RapidAPI-Host": "adder3.p.rapidapi.com"
            }


        response = requests.get(url, headers=headers, params=querystring)
        try:
            observation = response.json()
        except:
            observation = response.text
        return observation


    def get_bloomberg_stock_information(query: str) -> str:
        """These APIs helps to query for all information about Indices, Commodities, Currencies, Futures, Rates, Bonds, etc… as on official website."""
        url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/auto-complete"

        querystring = {"query":query}

        headers = {
            "X-RapidAPI-Key": "b7bff29dbamsh733868f06fac1c1p127433jsn7f88eb1c6e12",
            "X-RapidAPI-Host": "bloomberg-market-and-financial-news.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        return response.json()
    

    def search_airport(query: str) -> str:
        """
        The query is just the location
        Tripadvisor API helps to query realtime Hotels search, Flights prices, Restaurants, Attracting locations, etc to create a travelling site.
        Tripadvisor, Inc. is an American online travel company that operates a website and mobile app with user-generated content and a comparison shopping website. It also offers online hotel reservations and bookings for transportation, lodging, travel experiences, and restaurants.
        """
        url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchAirport"

        querystring = {"query":query}

        headers = {
            "X-RapidAPI-Key": "b7bff29dbamsh733868f06fac1c1p127433jsn7f88eb1c6e12",
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.json())
        return response.json()
    def search_flights(query: str) -> str:
        """
        query = {"sourceAirportCode":"BOM","destinationAirportCode":"DEL","date":"<REQUIRED>","itineraryType":"<REQUIRED>","sortOrder":"<REQUIRED>","numAdults":"1","numSeniors":"0","classOfService":"<REQUIRED>","pageNumber":"1","currencyCode":"USD"}
        Tripadvisor API helps to query realtime Hotels search, Flights prices, Restaurants, Attracting locations, etc to create a travelling site.
        Tripadvisor, Inc. is an American online travel company that operates a website and mobile app with user-generated content and a comparison shopping website. It also offers online hotel reservations and bookings for transportation, lodging, travel experiences, and restaurants.
        """
        url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"

        querystring = {"sourceAirportCode":"BOM","destinationAirportCode":"DEL","date":"<REQUIRED>","itineraryType":"<REQUIRED>","sortOrder":"<REQUIRED>","numAdults":"1","numSeniors":"0","classOfService":"<REQUIRED>","pageNumber":"1","currencyCode":"USD"}

        headers = {
            "X-RapidAPI-Key": "b7bff29dbamsh733868f06fac1c1p127433jsn7f88eb1c6e12",
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.json())
        return response.json()

    def search_flights_multicity(query: str) -> str:
        """
        query = {"legs":"[{\"sourceAirportCode\":\"BOS\",\"destinationAirportCode\":\"LON\",\"date\":\"2023-10-18\"},{\"sourceAirportCode\":\"LON\",\"destinationAirportCode\":\"BOS\",\"date\":\"2023-10-26\"}]","classOfService":"<REQUIRED>","sortOrder":"<REQUIRED>","currencyCode":"USD"}

        Tripadvisor API helps to query realtime Hotels search, Flights prices, Restaurants, Attracting locations, etc to create a travelling site.
        Tripadvisor, Inc. is an American online travel company that operates a website and mobile app with user-generated content and a comparison shopping website. It also offers online hotel reservations and bookings for transportation, lodging, travel experiences, and restaurants.
        """
        url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlightsMultiCity"

        querystring = {"legs":"[{\"sourceAirportCode\":\"BOS\",\"destinationAirportCode\":\"LON\",\"date\":\"2023-10-18\"},{\"sourceAirportCode\":\"LON\",\"destinationAirportCode\":\"BOS\",\"date\":\"2023-10-26\"}]","classOfService":"<REQUIRED>","sortOrder":"<REQUIRED>","currencyCode":"USD"}

        headers = {
            "X-RapidAPI-Key": "b7bff29dbamsh733868f06fac1c1p127433jsn7f88eb1c6e12",
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.json())
        return response.json()
    def get_filters(query: str) -> str:
        """
        The query is just the  {"sourceAirportCode":"BOM","destinationAirportCode":"DEL","date":"<REQUIRED>","itineraryType":"<REQUIRED>","classOfService":"<REQUIRED>"}
        Tripadvisor API helps to query realtime Hotels search, Flights prices, Restaurants, Attracting locations, etc to create a travelling site.
        Tripadvisor, Inc. is an American online travel company that operates a website and mobile app with user-generated content and a comparison shopping website. It also offers online hotel reservations and bookings for transportation, lodging, travel experiences, and restaurants.
        """
        url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/getFilters"

        querystring = {"sourceAirportCode":"BOM","destinationAirportCode":"DEL","date":"<REQUIRED>","itineraryType":"<REQUIRED>","classOfService":"<REQUIRED>"}

        headers = {
            "X-RapidAPI-Key": "b7bff29dbamsh733868f06fac1c1p127433jsn7f88eb1c6e12",
            "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=query)

        return response.json()
    
    def get_hotel_prices(query):
        """
        querystring = {"location":"Paris","checkin":"2023-09-16","checkout":"2023-09-17","adults":"1","children":"0","infants":"0","pets":"0","page":"1","currency":"USD"}

        Get Airbnb listings data, find rooms, search availability, prices on all locations.

        Find rooms on Airbnb by geo coordinates or location. Search rooms at a location (e.g. Paris) between two dates, get availability and prices. Search rooms in an area limited by two GEO points between two dates. Use autocomplete to help find location names.
        """

        url = "https://airbnb13.p.rapidapi.com/search-location"

        querystring = {"location":"Paris","checkin":"2023-09-16","checkout":"2023-09-17","adults":"1","children":"0","infants":"0","pets":"0","page":"1","currency":"USD"}

        headers = {
            "X-RapidAPI-Key": "b7bff29dbamsh733868f06fac1c1p127433jsn7f88eb1c6e12",
            "X-RapidAPI-Host": "airbnb13.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=query)

        return response.json()
    
    
    
    def api_json_to_openai_json(self, api_json):
        description_max_length=256
        templete =     {
            "type":"function",
            "function": {
              "name": "",
              "description": "",
              "parameters": {
                  "type": "object",
                  "properties": {
                  },
                  "required": [],
                  "optional": [],
              }
            }
        }

        pure_api_name = api_json['name']
        templete['function']['name']= pure_api_name

        templete['function']["description"] = api_json['description']
        templete['function']['parameters']['properties'] = api_json['parameters']['properties']
        templete['function']['parameters']['required'] = api_json['parameters']['required']
        return templete
    
    def get_openai_functions(self):
      tools = [self.get_current,self.add,self.get_bloomberg_stock_information, self.get_filters, self.search_airport, self.search_flights,self.search_flights_multicity, self.get_hotel_prices]
      openai_functions = [convert_to_openai_function(tool) for tool in tools]
      new_list = []
      for x in openai_functions:
         new_list.append(self.api_json_to_openai_json(x))
      return new_list+self.functions


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

@tool
def sandiego_weather() -> str:
    """Get the temperature in San Diego now, unit is Celsius."""
    return 25

@tool
def get_bloomberg_stock_information(query) -> str:
    """These APIs helps to query for all information about Indices, Commodities, Currencies, Futures, Rates, Bonds, etc… as on official website."""
    url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/auto-complete"

    querystring = {"query":query}

    headers = {
        "X-RapidAPI-Key": "b7bff29dbamsh733868f06fac1c1p127433jsn7f88eb1c6e12",
        "X-RapidAPI-Host": "bloomberg-market-and-financial-news.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
    return response.json()

@tool
def add(a,b):
  """Multiply two numbers."""
  url = 'https://electrical-units.p.rapidapi.com/power_to_current/single_phase'
  
  params=  {
    'power': '3000',
    'voltage': '230',
    'powerfactor': '0.95'
  }
  headers = {
    'X-RapidAPI-Key': 'b7bff29dbamsh733868f06fac1c1p127433jsn7f88eb1c6e12',
    'X-RapidAPI-Host': 'electrical-units.p.rapidapi.com'
  }
  response = requests.get(url, headers=headers, params=params)
  return response.json()




tools = [multiply, sandiego_weather, get_bloomberg_stock_information]

openai_functions = [convert_to_openai_function(tool) for tool in tools]




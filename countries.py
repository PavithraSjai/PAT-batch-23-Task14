import requests

#class countries 
class Countries:
    def __init__(self, url):#constructor
        self.url = url
        self.data = None
    #Method to fetch Country data 
    def fetch_countrydata(self): 
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.data = response.json()
                return "Country data is fetched successfully"
            else:
                return f"Failed to fetch data. Status code: {response.status_code}"
        except requests.RequestException as e:
            return f"Request Exception: {e}"
    #Method to fetch countries and currencies along with dollar and Euro countries 
    def fetch_Country_Currencies(self):
        if self.data:
            for country_data in self.data:
                name = country_data.get('name', {}).get('common', 'Not Available')#getting the name of the country 
                currencies = country_data.get('currencies', []) #getting the currency details 
                dollar_countries = [name for currency in currencies if 'USD' in currency]#getting the Country name whose currency is Dollar 
                Euro_countries = [name for currency in currencies if 'EUR' in currency]#getting the Country name whose currency is Euro

                #Printing the output 
                print(f"Country name: {name}")
                print(f"Currencies: {currencies}")
                if dollar_countries:
                    print(f"Countries whose currency is Dollar: {dollar_countries}")
                                
                elif Euro_countries:
                    print(f"Countries whose currency is Euro: {Euro_countries}")
                else:
                    print("Currency does not belong to Dollar or Euro" )
                
                print("\n")

url = "https://restcountries.com/v3.1/all" #Json URL 
obj = Countries(url) #Instance of class country
print(obj.fetch_countrydata()) #calling Fetch country data method 
print(obj.fetch_Country_Currencies()) #calling fetch country and currency details method 

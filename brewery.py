import requests

#Fetching the brewery data from URL
def fetch_brewery_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return None
#Method to find breweries by state 
def breweries_by_states(breweries, states):
    filtered_breweries = [brewery for brewery in breweries if brewery['state'] in states]
    return filtered_breweries
#Method to find the total count of breweries by state
def count_breweries_by_state(filtered_breweries):
    state_counts = {}
    for brewery in filtered_breweries:
        state = brewery['state']
        state_counts[state] = state_counts.get(state, 0) + 1
    return state_counts
#Method to find count of breweries by city 
def count_brewery_types_by_city(filtered_breweries):
    city_brewery_types = {}
    for brewery in filtered_breweries:
        city = brewery['city']
        brewery_type = brewery['brewery_type']
        city_brewery_types[city] = city_brewery_types.get(city, {})
        city_brewery_types[city][brewery_type] = city_brewery_types[city].get(brewery_type, 0) + 1
    return city_brewery_types
#Method to find the count and list of breweries with active website 
def count_and_list_breweries_with_websites(filtered_breweries):
    breweries_with_websites = [brewery for brewery in filtered_breweries if 'website_url' in brewery and brewery['website_url']]
    return len(breweries_with_websites), breweries_with_websites

# URL for Open Brewery DB API documentation
api_url = "https://api.openbrewerydb.org/breweries"

# Fetch all brewery data
all_breweries = fetch_brewery_data(api_url)

# Filter breweries by states - Alaska, Maine and New York
expected_states = ['Alaska', 'Maine', 'New York']
filtered_breweries = breweries_by_states(all_breweries, expected_states)

#List names of all breweries in the specified states
brewery_names = [brewery['name'] for brewery in filtered_breweries]
print("Breweries in Alaska, Maine, and New York states:")
print(brewery_names)
print("\n")

#Count of breweries in each state
state_counts = count_breweries_by_state(filtered_breweries)
print("Total Count of breweries in each state:")
for state, count in state_counts.items():
    print(f"{state}: {count}")
print("\n")

#Count of brewery types in individual cities
city_brewery_types = count_brewery_types_by_city(filtered_breweries)
print("Total Count of brewery types in individual cities:")
for city, types in city_brewery_types.items():
    print(f"{city}: {types}")
print("\n")

#Count and list breweries with websites in specified states
website_count, breweries_with_websites = count_and_list_breweries_with_websites(filtered_breweries)
print(f"Total Count of breweries with websites: {website_count}")
print("Breweries with active websites:")
for brewery in breweries_with_websites:
    print(f"{brewery['name']}")

import requests
import os

def get_comet_data(api_key):
    print("::: COMET INFORMATION :::")
    print("-------------------------")

    try:
        api_url = "https://api.nasa.gov/neo/rest/v1/neo/3726712"
        response = requests.get(api_url, params={'api_key': api_key})
        response.raise_for_status()
        data = response.json()

        print(f"Comet name: {data['name']}")
        print(f"Absolute magnitude: {data['absolute_magnitude_h']}")
        estimated_diameter = data['estimated_diameter']
        print(f"Estimated diameter max (KM): {estimated_diameter['kilometers']['estimated_diameter_max']}")
        print(f"Estimated diameter min (KM): {estimated_diameter['kilometers']['estimated_diameter_min']}")
        print(f"Estimated diameter max (FT): {estimated_diameter['feet']['estimated_diameter_max']}")
        print(f"Estimated diameter min (FT): {estimated_diameter['feet']['estimated_diameter_min']}")
        orbital_data = data['orbital_data']
        print(f"Last observation date: {orbital_data['last_observation_date']}")

    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")

# Main
def main():
    api_key_nasa = 'UHfJAbib0edUGaHGQEU5awMvUvQYNO44axsB7Iyf'
    get_comet_data(api_key_nasa)

if __name__ == "__main__":
    main()

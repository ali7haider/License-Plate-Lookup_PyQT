import requests
import traceback

API_URL_PLATE = "https://api.licenselookup.org/license-plate-search"
API_URL_PHONE = "https://api.licenselookup.org/usa-advanced-phone-search"
API_URL_ZIP = "https://api.licenselookup.org/zip-code-search-us"

ACCESS_TOKEN = "5b13d1c13f8a04d0ffe80b725866843f"  # Move to env variable in production

def get_plate_info(plate, state):
    """Fetch license plate details from API."""
    try:
        url = f"{API_URL_PLATE}?plate={plate}&state={state}&format=json&request_type=web&access_token={ACCESS_TOKEN}"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        return data.get("content")
    
    except requests.exceptions.Timeout:
        print("ERROR: API request timed out.")
        return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ERROR: {http_err}")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"REQUEST ERROR: {req_err}")
        return None
    except Exception as e:
        print(f"Unexpected API Error: {e}\n{traceback.format_exc()}")
        return None

def get_phone_info(phone):
    """Fetch phone number details from API."""
    try:
        url = f"{API_URL_PHONE}?phone={phone}&format=json&request_type=web&access_token={ACCESS_TOKEN}"

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("data")

    except requests.exceptions.Timeout:
        print("ERROR: API request timed out.")
        return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ERROR: {http_err}")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"REQUEST ERROR: {req_err}")
        return None
    except Exception as e:
        print(f"Unexpected API Error: {e}\n{traceback.format_exc()}")
        return None

def get_zip_info(zip_code):
    """Fetch ZIP code details from API."""
    try:
        url = f"{API_URL_ZIP}?zip={zip_code}&format=json&request_type=web&access_token={ACCESS_TOKEN}"

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data

    except requests.exceptions.Timeout:
        print("ERROR: API request timed out.")
        return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ERROR: {http_err}")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"REQUEST ERROR: {req_err}")
        return None
    except Exception as e:
        print(f"Unexpected API Error: {e}\n{traceback.format_exc()}")
        return None

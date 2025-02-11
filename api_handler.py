import requests
import traceback

def get_plate_info(plate, state):
    """Fetch license plate details from API."""
    try:
        url = f"https://api.licenselookup.org/license-plate-search?plate={plate}&state={state}&format=json&request_type=web&access_token=5b13d1c13f8a04d0ffe80b725866843f"

        response = requests.get(url, timeout=10)  # 10-second timeout for reliability
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

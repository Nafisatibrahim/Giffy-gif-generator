# utils.py
import requests

def get_gif_url(term, api_key):
    url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "api_key": api_key,
        "q": term,
        "limit": 1,
        "rating": "pg"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if data.get("data"):
            return data["data"][0]["images"]["original"]["url"]
    except Exception as e:
        print(f"Error fetching single GIF: {e}")
    return None

def get_random_gif(api_key):
    url = "https://api.giphy.com/v1/gifs/random"
    params = {
        "api_key": api_key,
        "rating": "pg"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data["data"]["images"]["original"]["url"]
    except Exception as e:
        print(f"Error fetching random GIF: {e}")
    return None

def get_top_gifs(term, api_key, limit=3):
    url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "api_key": api_key,
        "q": term,
        "limit": limit,
        "rating": "pg"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return [item["images"]["original"]["url"] for item in data["data"]]
    except Exception as e:
        print(f"Error fetching top GIFs: {e}")
    return []

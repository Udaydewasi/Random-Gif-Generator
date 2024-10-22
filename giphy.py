import requests
import webbrowser

# Replace with your Giphy API key
API_KEY = "your_giphy_api_key"
GIPHY_API_URL = "https://api.giphy.com/v1/gifs/random"

def get_random_gif():
    """Fetches a random GIF URL from Giphy API."""
    params = {
        "api_key": API_KEY,
        "tag": "",  # You can specify a tag like 'funny', 'cat', etc. Leave empty for random GIFs.
        "rating": "G",  # You can change rating (e.g., G, PG, PG-13, R)
    }
    response = requests.get(GIPHY_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        gif_url = data['data']['images']['original']['url']
        return gif_url
    else:
        print(f"Error: Unable to fetch GIF. Status code {response.status_code}")
        return None

def open_gif_in_browser(gif_url):
    """Opens the GIF in the web browser."""
    webbrowser.open(gif_url)

if __name__ == "__main__":
    gif_url = get_random_gif()
    if gif_url:
        print(f"Random GIF URL: {gif_url}")
        open_gif_in_browser(gif_url)

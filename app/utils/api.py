from dotenv import load_dotenv
import os
import requests
import json
from functools import lru_cache
load_dotenv()

TOKEN_URL = os.getenv("TOKEN_URL")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


def get_access_token():
    
    response = requests.post(TOKEN_URL, headers={
        "Content-Type" : 'application/x-www-form-urlencoded'
    },data={
        "grant_type":'client_credentials',
        "client_id" : CLIENT_ID,
        "client_secret" : CLIENT_SECRET
    })
    data = json.loads(response.content)
    token = data['access_token']
    return token



def search_for_artist(token, query,limit):
    url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization" : f"Bearer {token}"
    }
    query = f"?q={query}&type=artist&limit={limit}"
    query_url = f"{url}{query}"
    response = requests.get(query_url, headers)
    json_result = response.json()
    return json_result

def get_artist_byId():
    pass





    
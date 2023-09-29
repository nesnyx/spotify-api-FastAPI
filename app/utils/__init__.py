from fastapi import APIRouter, status
from app.utils import api
import requests
from typing import Optional, List


router = APIRouter()


#Search for Artist
@router.get("/api/v1/artist", tags=['Artist'], status_code=status.HTTP_200_OK)
async def search_artist(token : str,limit:int, query:str):
    storage = []
    url = f"https://api.spotify.com/v1/search?q={query}&type=artist&limit={limit}"
    response = requests.get(url, headers={
        "Authorization" : f"Bearer {token}"
    })
    data = response.json()
    for i in data['artists']['items']:
        data_storage = {
            "id" : i['id'],
            "link" : i['href'],
            "name" : i['name'],
            "genres": i['genres'],
        }
    storage.append(data_storage)
    return {"data":storage}

# Get artist by Id
@router.get("/api/v1/artist/{id}",tags=['Artist'], status_code=status.HTTP_200_OK)
async def get_artist_byId(id : str, token:str):
    storage = []
    url = f"https://api.spotify.com/v1/artists/{id}"
    response = requests.get(url, headers={
        "Authorization" : f"Bearer {token}"
    })
    
    data = response.json()
    data_storage = {
        "id" : data['id'],
        "name" : data['name'],
        "genres" : data['genres'],
        "followers" : float(data['followers']['total']),
        "images": data['images'][0]
    }
    storage.append(data_storage)
    return {"data": storage}

# get artists album
@router.get("/api/v1/artist/{id}/albums", tags=['Artist'], status_code=status.HTTP_200_OK)
async def get_artist_album(token:str, id:str,limit:int, include_groups : Optional[str] = "album"):
    storage = []
    url = f"https://api.spotify.com/v1/artists/{id}/albums?include={include_groups}&limit={limit}"
    response = requests.get(url, headers={
        "Authorization" : f"Bearer {token}"
    })
    data = response.json()
    for i in data['items']:
        data_storage= {
            "id_artist" : i["artists"][0]['id'],
            "name" : i["artists"][0]['name'],
            "uri" : i["artists"][0]['uri'],
            "id_album" : i['id'],
            "name_album" : i['name'],
            'release_date' : i['release_date'],
            "album_url" : i['external_urls']['spotify'],
            "total_tracks": i["total_tracks"],
            "uri": i['uri']
        }
    
    storage.append(data_storage)
    return {"data" : storage}

#Get Token
@router.post("/api/v1/token", tags=['Access Token'], status_code=status.HTTP_200_OK)
async def get_token():
    data_token = api.get_access_token()
    return {"data": data_token}


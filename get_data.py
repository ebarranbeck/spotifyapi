from dotenv import load_dotenv
import requests
import os

load_dotenv()

AUTH_URL=os.getenv('AUTH_URL')
API_URL=os.getenv('API_URL')
CLIENT_ID=os.getenv('CLIENT_ID')
CLIENT_SECRET=os.getenv('CLIENT_SECRET')
print(AUTH_URL)

def get_token():
    auth_response=requests.post(AUTH_URL,{
        'grant_type':'client_credentials',
        'client_id':CLIENT_ID,
        'client_secret':CLIENT_SECRET
    })

    auth_response_data=auth_response.json()

    access_token=auth_response_data['access_token']
    return access_token
access_token=get_token()
print(access_token)

headers={'Authorization':'Bearer {token}'.format(token=access_token)}

def get_top_items(type):
    params={'time_range':'medium_term','limit':10}
    response=requests.get(API_URL+f"/me/top/{type}",headers=headers)
    print(response.reason)
    return response.json
#top_artists=get_top_items('artists')
#print(top_artists)

def get_artist(artist_id):
    params={'time_range':'medium_term','limit':10}
    response=requests.get(API_URL+f"/artists/{artist_id}/albums",headers=headers)
    return response.json()
artist_id='1r1uxoy19fzMxunt3ONAkG'
artist=get_artist(artist_id)
for album in artist["items"]:
    print(album['name'])
#print(json.dumps(artist,indent=4))
    
def get_artist_tracks(artist_id):
    params={'market':'GB'}
    response=requests.get(API_URL+f"/artists/{artist_id}/top-tracks",headers=headers,params=params)
    return response.json()
artist_id='1r1uxoy19fzMxunt3ONAkG'
artist=get_artist_tracks(artist_id)
for track in artist["tracks"]:
    print(track['name'])

def get_artist(artist_id):
    response=requests.get(API_URL+f"/artists/{artist_id}",headers=headers)
    return response.json()
artist_id='1hLiboQ98IQWhpKeP9vRFw'
artist=get_artist(artist_id)
print(artist['popularity'])

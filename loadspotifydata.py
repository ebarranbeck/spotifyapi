from pymongo import MongoClient
import json
from dotenv import load_dotenv
import os
load_dotenv()

# Connecting to MongoDB Atlas
conn_str = os.getenv('CONN_STR')
client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)

try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")

database_list = client.list_database_names()
print(database_list)


# Creating the database and the collections
myDB = client["Spotify"]
#dropping the collections
myDB.Inferences.drop()
myDB.Marquee.drop()
myDB.Playlists.drop()
myDB.Searches.drop()
myDB.StreamingHistory.drop()
myDB.Library.drop()

#Creating the collections
Inferences = myDB["Inferences"]  # Use square brackets to access the collection
Marquee =myDB["Marquee"]
Playlists=myDB["Playlists"]
Searches=myDB["Searches"]
StreamingHistory=myDB["StreamingHistory"]
Library=myDB["Library"]


#Loading the files and inserting them into collections
with open('/Users/elliebarranbeck/Spotify Account Data/Inferences.json') as f:
   inference_items = json.load(f)

Inferences.insert_one(inference_items)

with open('/Users/elliebarranbeck/Spotify Account Data/Marquee.json') as f:
   marquee_items = json.load(f)
Marquee.insert_many(marquee_items)

with open('/Users/elliebarranbeck/Spotify Account Data/StreamingHistory0.json') as f:
   streaming_items = json.load(f)
StreamingHistory.insert_many(streaming_items)

with open('/Users/elliebarranbeck/Spotify Account Data/StreamingHistory1.json') as f:
   streaming_items = json.load(f)
StreamingHistory.insert_many(streaming_items)

with open('/Users/elliebarranbeck/Spotify Account Data/Playlist1.json') as f:
   playlist_items = json.load(f)
   for items in playlist_items["playlists"]:
      Playlists.insert_one(items)

with open('/Users/elliebarranbeck/Spotify Account Data/SearchQueries.json') as f:
    search_items = json.load(f)
Searches.insert_many(search_items)

with open('/Users/elliebarranbeck/Spotify Account Data/YourLibrary.json') as f:
   library_items = json.load(f)
   for items in library_items["tracks"]:
      Library.insert_one(items)

client.close()
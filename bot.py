#import libraries and packages
import googleapiclient.discovery
import googleapiclient.errors
from textblob import TextBlob
import csv
import os
import re

#authentication
api_service_name = "youtube"
api_version = "v3"
youtube_api_key = "insert your YouTube API key here"

api = googleapiclient.discovery.build(api_service_name, api_version, developerKey=youtube_api_key)

# request comments from desired YouTube video
channel = "insert channel name here"
id = "insert video ID here"

request = api.commentThreads().list(part="snippet", videoId=id, maxResults=4)
response = request.execute()

#add comments to comments list
comments = []
for item in response['items']:
    comments.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])
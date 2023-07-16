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

#function to clean comments
def clean_comment(comment):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", comment).split())

#function to append comment sentiments to csv file
def append_list_to_csv(comments, filename):
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if not file_exists:
            writer.writerow(['Comment', 'Polarity', 'Subjectivity', 'Channel'])  # write header only if the file is newly created
        for comment in comments:
            text = clean_comment(comment.text)
            analysis = TextBlob(text)
            polarity = analysis.polarity
            subjectivity = analysis.subjectivity
            writer.writerow([text, polarity, subjectivity, channel])
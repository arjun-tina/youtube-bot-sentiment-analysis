#import libraries and packages
import googleapiclient
import googleapiclient.discovery
import googleapiclient.errors
from textblob import TextBlob
import csv
import os
import re

#authentication
api_service_name = "youtube"
api_version = "v3"
youtube_api_key = "insert your key here"

api = googleapiclient.discovery.build(api_service_name, api_version, youtube_api_key)


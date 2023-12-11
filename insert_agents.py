from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

# load environment variables
load_dotenv()

# load the mongodb connection string
mongo_uri = os.getenv('MONGODB_URI')

# connect to mongodb
client = MongoClient(mongo_uri)

# set the database
db = client.ai_agents

# collection
collection = db.agents

# read the json
with open('ai_agents.json','r') as file:
    data = json.load(file)

# insert the data into the mongodb
collection.insert_many(data['agents'])
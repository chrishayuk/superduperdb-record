from pymongo import MongoClient
from superduperdb import superduper
from superduperdb.backends.mongodb import Collection
from superduperdb.base.document import Document
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
db = superduper(MongoClient(mongo_uri).ai_agents)

# collection
collection = Collection('agents')

# read the json
with open('ai_agents.json','r') as file:
    data = json.load(file)

agent_docs = []
for agent in data['agents']:
    json_string = json.dumps(agent)
    agent['search_data'] = json_string
    agent_docs.append(Document(agent))

# insert the data into the mongodb
db.execute(collection.insert_many(agent_docs))
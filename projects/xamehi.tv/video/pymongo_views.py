from django.shortcuts import render
from django.http import HttpResponse
import pymongo

# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello and welcome to my <u>Django App</u> project!</h1>")


client = pymongo.MongoClient(
    'mongodb+srv://bot:Rhixe&company%401@rhixecompany.ejlsb.mongodb.net/test')

# Define DB Name
dbname = client['xamehitv']

# Define Collection
collection = dbname['movies']

movies_1 = {
    "name": "Stargirl",
    "image": "https://static.netnaija.com/i/rOx7xxw270M.jpg"
}

collection.insert_one(movies_1)

mascot_details = collection.find({})

for r in mascot_details:
    print(r['name'])

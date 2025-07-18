from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from User import User

def main():

    uri = "mongodb+srv://admin:admin@cluster0.blirv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    print('Connection created with mongo :)')
    
    query = {'email':'himanshu@gmail.con'}
    db = client['user']
    result = db['user'].delete_one(query)

    print("result",result, type(result))


if __name__ == "__main__":
    main()
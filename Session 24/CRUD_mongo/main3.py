from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from User import User

def main():

    uri = "mongodb+srv://admin:admin@cluster0.blirv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    print('Connection created with mongo :)')
    
    document ={"_id":{"$oid":"6879e42b64e09455b43df103"},"name":"jack","age":{"$numberInt":"45"},"email":"ero@gmail.com"}
    query = {'email':'jack@gmail.com'}
    db = client['user']
    result = db['user'].update_one(query,{'$set':document})
    print(result)
    # {"_id":{"$oid":"6879e42b64e09455b43df103"},"name":"jack","age":{"$numberInt":"45"},"email":"ero@gmail.com"}


if __name__ == "__main__":
    main()
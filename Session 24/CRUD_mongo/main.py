from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from User import User

def main():

    uri = "mongodb+srv://admin:admin@cluster0.blirv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    print('Connection created with mongo :)')

    user = User()
    user.input_user_details()
    print('User created with data')

    user.show()
    user_doc = user.to_document()
    print(user_doc)

    db = client['user']
    result = db['user'].insert_one(user_doc)

    print("result is", result,type(result))

    print('total documents: ')
    documents = db['user'].find()

    for d in documents:
        print(d)


if __name__ == "__main__":
    main()
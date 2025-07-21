"""
controller
    mongoDB helper

    database contains collections
    collection which contains documents


    document: dictionary

    User    : name, phone, email, age, gender etc
    Address : adrsLine, city, state, incode


    User HAS A address

    User can have 1 address
    or can have many addresses

    1. referencetial technique
        collection 1 : users
        {
            '_id': 'kjasjdfiouahsdfh87y8oaihdsuf',
            'name': 'John',
            etc

            'address_id' : 'lhafispd697iayudshfi
        }
        collection 2 : addresses
        {
            '_id': 'lhafispd697iayudshfi',
            'adrsLine': '123 Main St',
            'city': 'New York'
            etc

            'user_id': 'kjasjdfiouahsdfh87y8oaihdsuf
        }

        Loose coupling between collections

        user and address are saved differntly 
        and they have reference sabed inside them

    2. containerzied technique
    collection 1 : users
        {
            '_id': 'kjasjdfiouahsdfh87y8oaihdsuf',
            'name': 'John',
            etc

            'address' : {
                    'adrsLine': '123 Main St',
                    'city': 'New York'
                    etc
                }
        }

        {
            '_id': 'kjasjdfiouahsdfh87y8oaihdsuf',
            'name': 'John',
            etc

            'addresses' : [
                {
                    'adrsLine': '123 Main St',
                    'city': 'New York'
                    etc
                },
                {
                    '
                }
            ]
        }


"""


"""
1. create connnection with mongoDB  atlas in cloud
2. select the database and the collection, in which you want to work
3. create write function (insert, delete, update)
    mongoDB: insert_one(), delete_one(), update_one()
4. create read function (retrieve/fetch)
    MongoDB : find()

    their can be a query to delete , update as well find
"""



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class MongoDBHelper:
    # 1. create connnection with mongoDB  atlas in cloud
    def __init__(self):

        self.client = MongoClient("mongodb+srv://admin:admin@cluster0.blirv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", server_api=ServerApi('1'))
        print('Connection created')
    
    # 2. select the database and the collection, in which you want to work
    def select_db(self, db_name='Training',collection='User'):
        self.db = self.client[db_name]
        self.collection = self.db[collection]
        print('[mongoDBHelper] db {} collection {} selected'.format(db_name,collection))


    # 3. create write function (insert, delete, update)--------------------------
    def insert(self,doc):
        result = self.collection.insert_one(doc)
        print('data inserted {} in collection {} '.format(doc, self.collection.name))
        return result
    

    def delete(self,query):
        result = self.collection.delete_one(query)
        print('data deleted from collection {} '.format(self.collection.name))
        return result
    
    def update(self,query,doc):
        result = self.collection.update_one(query,{'$set':doc})
        print('data updated')
        return result
    

    def fetch(self,query=''):
        documents = self.collection.find()
        return list(documents)
        
    
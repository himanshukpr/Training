from MongoHelper import MongoDBHelper
from User import User

def main():
    db_helper = MongoDBHelper()
    db_helper.select_db(db_name='user', collection='user')


    user = User()
    user.input_user_details()

    result = db_helper.insert(doc=user.to_document())
    print('user saved in mongoDB with id:', result.inserted_id)


if __name__ == "__main__":
    main()
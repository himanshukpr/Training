from flask import *
from user import User
from MongoHelper import MongoDBHelper
import hashlib

app = Flask('app')
db = MongoDBHelper()
db.select_db()


# view
@app.route('/')
def index():
    return render_template('index.html')
# view
@app.route('/register')
def register():
    return render_template('Register.html')


# controller function
@app.route('/add-user',methods=['POST'])
def add_user_in_db():
    user = User()
    user.name = request.form['name']
    user.email = request.form['email']
    # encryption
    user.password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()

    db.insert(user.to_document())
    return render_template('home.html')

def main():
    # secret key is used to session management, it is required for session management
    app.secret_key  = 'doctors-app-key-v1'
    app.run()

if __name__ == '__main__':
    main()
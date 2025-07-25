from flask import *
from user import User
from MongoHelper import MongoDBHelper
import hashlib
import datetime
from Patient import Patient
from bson.objectid import ObjectId

app = Flask('app')
db = MongoDBHelper()
db.select_db()



@app.route('/logout')
def logout():
    session['user_id'] = ''
    session['name'] = ''
    session['email'] = ''
    return redirect('/')

# view
@app.route('/')
def index():
    return render_template('index.html')
# view
@app.route('/register')
def register():
    return render_template('Register.html')

@app.route('/home')
def home():
    if len(session['user_id']) > 0:
        return render_template('home.html',name = session['name'],email = session['email'],login_at = session['login_at'])
    else:
        return redirect('/')

@app.route('/add-patient')
def add_patient():
    if len(session['user_id']) > 0:
        return render_template('add-patient.html')
        
    else:
        return redirect('/')

# controller function
@app.route('/add-user',methods=['POST'])
def add_user_in_db():
    user = User()
    user.name = request.form['name']
    user.email = request.form['email']
    # encryption
    user.password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()

    db.select_db(collection='User')
    result = db.insert(user.to_document())
    if len(str(result.inserted_id)) > 0:

        # session is used to save data whenever you need to access it in throughout the session
        session['user_id']  = str(result.inserted_id)
        session['name'] = user.name
        session['email'] = user.email
        session['login_at'] = datetime.datetime.now()

        # return render_template('home.html',name = user.name,email = user.email,login_at = datetime.datetime.now())
        return redirect('/home')
    else:
        return 'Something went wrong, please Try again later'



@app.route('/fetch-user',methods=['POST'])
def fetch_user_from_db():

    db.select_db(collection='User')

    query = {
        'email':request.form['email'],
        'password': hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
    }

    documents = db.fetch(query)
    if len(documents) > 0:
        user = documents[0]
        session['user_id']  = str(user['_id'])
        session['name'] = user['name']
        session['email'] = user['email']
        session['login_at'] = datetime.datetime.now()


        return redirect('/home')
    else:
        return render_template('error.html',message = 'User not found, please register first')
    
@app.route('/add-patient-details', methods=['POST'])
def add_patient_details():
    patient = Patient(
        name = request.form['name'],
        phone = request.form['phone'],
        email = request.form['email'],
        address = request.form['address'],
        gender = request.form['gender'],
        age = request.form['age'],
        doctor_id= session['user_id']
    )

    print(patient.to_document())

    db.select_db(collection='Patient')
    result = db.insert(patient.to_document())

    if result:
        return redirect('/home')
    else:
        return redirect('error.html',message = 'Something went wrong, please try again later')
   
    
@app.route('/fetch-patients')
def fetch_patients_from_db():
    if len(session['user_id']) > 0:

        db.select_db(collection='Patient')
        query = {
            'doctor_id':session['user_id']
        }
        documents = db.fetch(query)
        # if len(documents) > 0:
        return render_template('patients.html',name = session['name'],email = session['email'],
                            total = len(documents), patients = documents)
        # else:
        #     return render_template('error.html',message =  'Patients not found, please add patients first')
    else:
        return redirect('/')

# controller: recives an input in url

@app.route('/delete-patient/<id>')
def delete_patient(id):
    db.select_db(collection='Patient')
    query = {
        '_id': ObjectId(id)
    }
    result  = db.delete(query)
    if result:
        return redirect('/fetch-patients')
    else:
        return render_template('error.html', message='Something while deleting, please try again later')

@app.route('/update-patient/<id>')
def update_patient(id):
    query = {
        '_id': ObjectId(id)
    }
    db.select_db(collection='Patient')
    documents  = db.fetch(query)
    if len(documents) > 0:
        return render_template('update-patient.html', data = documents[0])
    else:
        return render_template('error.html', message='Patient not found, please try again later')


@app.route('/update-patient-details/<id>', methods=['POST'])
def update_patient_details(id):
    patient = Patient(
        name = request.form['name'],
        phone = request.form['phone'],
        email = request.form['email'],
        address = request.form['address'],
        gender = request.form['gender'],
        age = request.form['age'],
        doctor_id= session['user_id']
    )
    db.select_db(collection='Patient')

    query = {
        '_id': ObjectId(id)
    }

    result = db.update(query, patient.to_document())
    if result:
        return redirect('/home')
    else:
        return redirect('error.html',message = 'Something went wrong, please try again later')
   
    

def main():
    # secret key is used to session management, it is required for session management
    app.secret_key  = 'doctors-app-key-v1'
    app.run(debug=True)

if __name__ == '__main__':
    main()
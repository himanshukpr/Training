"""
    web app development with flask
    
    1. install flask library
    2. create a Flask application instance and run it in main
    3. display some index content to the user
"""


from flask import *
web_app = Flask('web_app')

@web_app.route('/') # decorator to define the route
def index():
    return render_template('index.html')

def main():
    pass

if __name__ == '__main__':
    web_app.run()
    main()
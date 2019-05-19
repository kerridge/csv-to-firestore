import pyrebase
import firebase_admin
import google.cloud

db = None
user = None

# a method to make the connection to firebase and set a user + db object
def db_connect():
    config = {
        'apiKey': "AIzaSyCC1-jL3YJMaz3gROmtRk75ohr1H2WFErM",
        'authDomain': "test-241002.firebaseapp.com",
        'databaseURL': "https://test-241002.firebaseio.com",
        'projectId': "test-241002",
        'storageBucket': "test-241002.appspot.com",
        "serviceAccount": "serviceCredentials.json"
    }

    # test-241002-0609914a6747

    # tell python to use globals
    global user
    global db

    # make the db connection
    firebase = pyrebase.initialize_app(config)

    # get our auth object
    auth = firebase.auth()

    # authenticate a user
    user = auth.sign_in_with_email_and_password("yolokerridge@gmail.com", "savethewhales")

    # get a reference to db services
    db = firebase.database()


    return db


# method to read data from our db
def db_read():

    all_agents = db.child("agents").get(user['idToken']).val()

    lana_data = db.child("agents").child("Lana").get(user['idToken']).val()

    print(all_agents)
    print(lana_data)


# method to create some mock data
def db_create():
    # create data
    lana = {"name": "Lana Kane", "agency": "Figgis Agency"}
    archer = {"name": "Stirling Archer", "agency": "Figgis Agency"}

    # push update
    db.child("agents").child("Lana").set(lana, user['idToken'])
    db.child("agents").child("Archer").set(archer, user['idToken'])



def main():
  db_connect()
  db_create()
  db_read()
  
if __name__== "__main__":
  main()















# <!-- The core Firebase JS SDK is always required and must be listed first -->
# <script src="https://www.gstatic.com/firebasejs/6.0.2/firebase-app.js"></script>

# <!-- TODO: Add SDKs for Firebase products that you want to use
#      https://firebase.google.com/docs/web/setup#config-web-app -->

# <script>
#   // Your web app's Firebase configuration
#   var firebaseConfig = {
#     apiKey: "AIzaSyCC1-jL3YJMaz3gROmtRk75ohr1H2WFErM",
#     authDomain: "test-241002.firebaseapp.com",
#     databaseURL: "https://test-241002.firebaseio.com",
#     projectId: "test-241002",
#     storageBucket: "test-241002.appspot.com",
#     messagingSenderId: "767423857707",
#     appId: "1:767423857707:web:e19a076bb90beb62"
#   };
#   // Initialize Firebase
#   firebase.initializeApp(firebaseConfig);
# </script>
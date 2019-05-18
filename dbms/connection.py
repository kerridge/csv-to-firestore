import pyrebase

db = None
user = None


def main():
  print("Hello World!")
  
if __name__== "__main__":
  main()


# a method to make the connection to firebase and set a user + db object
def db_connect():
    config = {
        'apiKey': "AIzaSyCC1-jL3YJMaz3gROmtRk75ohr1H2WFErM",
        'authDomain': "test-241002.firebaseapp.com",
        'databaseURL': "https://test-241002.firebaseio.com",
        'projectId': "test-241002",
        'storageBucket': "test-241002.appspot.com",
        "serviceAccount": "../test-241002-0609914a6747.json"
    }

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


# method to read data from our db
def read():
    # querying
    all_agents = db.child("agents").get(user['idToken']).val()

    lana_data = db.child("agents").child("Lana").get(user['idToken']).val()

    print(all_agents)
    print(lana_data)


def create():
    # create data
    lana = {"name": "Lana Kane", "agency": "Figgis Agency"}

    # push update
    db.child("agents").child("Lana").set(lana, user['idToken'])



















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
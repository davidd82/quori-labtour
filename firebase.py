import pyrebase
import firebase_config


firebase = pyrebase.initialize_app(firebase_config.firebaseConfig)

storage = firebase.storage()
database = firebase.database()

users = database.child("appID").get()
print(users.val())
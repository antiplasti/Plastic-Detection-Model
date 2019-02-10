import datetime
import pyrebase
from env import auth_cred

class Firebase:
    
    def __init__(self):
        pass

    def authenticate(self):
        self.firebase = pyrebase.initialize_app(
            {
                "apiKey": auth_cred["API_KEY"],
                "authDomain": auth_cred["AUTH_DOMAIN"],
                "databaseURL": auth_cred["DATABASE_URL"],
                "storageBucket": auth_cred["STORAGE_BUCKET"]
            }
        )
        self.db = self.firebase.database()
        self.auth = self.firebase.auth()
        self.user = self.auth.sign_in_with_email_and_password(auth_cred["EMAIL"], auth_cred["PASS"])
        self.uid = self.user["localId"]   
        
    def push(self, result):

        self.db.child("dummy").child(auth_cred["B_ID"]).update({"current_result": result, "last_updated": str(datetime.datetime.now())}, self.user["idToken"])

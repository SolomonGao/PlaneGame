from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin
import os

HTML= "https://console.firebase.google.com/project/game-c2306/storage/game-c2306.appspot.com/files"


class MyDatabase():

    def __init__(self):

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "game-c2306-firebase-adminsdk-qxb0l-967f71f84e.json"

        self.cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(self.cred, {
            "projectId" : "game-c2306"
        })

        self.__db = firestore.client()


    def getDb(self):
        return self.__db
    

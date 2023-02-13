import os

import pyrebase
from PIL import Image

#CONFIG
firebaseConfig = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": "saritasa-python-test.firebaseapp.com",
    "databaseURL": "",
    "projectId": "saritasa-python-test",
    "storageBucket": "saritasa-python-test.appspot.com",
    "messagingSenderId": "894879225222",
    "appId": os.getenv("FIREBASE_APP_ID")
    }

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

def resize_img(img_name):
    fixed_height = 512   #height of carousel
    image = Image.open(f"media/{img_name}")
    height_percent = (fixed_height / float(image.height))
    width_size = int((float(image.width) * float(height_percent)))

    new_img = image.resize((width_size, fixed_height))

    new_img.save(f"media/{img_name}")

def upload_img(user_id, memory_id, img_name):
    path_on_cloud = f"images/{user_id}/{memory_id}/{img_name}"
    path_local = f"media/{img_name}"
    storage.child(path_on_cloud).put(path_local)

def get_img(user_id, memory_id, img_name):
    auth = firebase.auth()
    email = os.getenv("FIREBASE_STORAGE_EMAIL")
    password = os.getenv("FIREBASE_STORAGE_PASSWORD")
    user = auth.sign_in_with_email_and_password(email, password)
    path_on_cloud = f"images/{user_id}/{memory_id}/{img_name}"
    url = storage.child(path_on_cloud).get_url(user['idToken'])
    return url

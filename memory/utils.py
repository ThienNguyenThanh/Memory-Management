from PIL import Image
import pyrebase

#CONFIG
firebaseConfig = {
    "apiKey": "AIzaSyB-HRMYLqKT3nUHdJlOKpQJcbwFSRjp07E",
    "authDomain": "saritasa-python-test.firebaseapp.com",
    "databaseURL": "",
    "projectId": "saritasa-python-test",
    "storageBucket": "saritasa-python-test.appspot.com",
    "messagingSenderId": "894879225222",
    "appId": "1:894879225222:web:82c6503f51fdca1ff5c807"
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
    email = "Saritasa-Python-Test@gmail.com"
    password = "PassTest!"
    user = auth.sign_in_with_email_and_password(email, password)
    path_on_cloud = f"images/{user_id}/{memory_id}/{img_name}"
    url = storage.child(path_on_cloud).get_url(user['idToken'])
    return url

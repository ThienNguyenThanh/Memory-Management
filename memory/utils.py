from PIL import Image
import pyrebase


def resize_img():
    fixed_height = 512
    image = Image.open("triumph.png")
    height_percent = (fixed_height / float(image.height))
    width_size = int((float(image.width) * float(height_percent)))

    image = image.resize((width_size, fixed_height))

    image.save("triumph-resize.png")

def upload_img():
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

    path_on_cloud = "images/test1.jpg"
    path_local = "s1000rr.png"
    # storage.child(path_on_cloud).put(path_local)

    #get image
    auth = firebase.auth()
    email = "Saritasa-Python-Test@gmail.com"
    password = "PassTest!"
    user = auth.sign_in_with_email_and_password(email, password)
    url = storage.child(path_on_cloud).get_url(user['idToken'])
    print(url)
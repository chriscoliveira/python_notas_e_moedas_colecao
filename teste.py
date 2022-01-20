from firebase_admin import credentials
from firebase_admin import credentials, initialize_app, storage

# Init firebase with your credentials
cred = credentials.Certificate(
    "minha-colecao-a01d5-firebase-adminsdk-ehm8b-b1a0aed377.json")
initialize_app(cred, {'storageBucket': 'minha-colecao-a01d5.appspot.com'})


# Put your local file path
fileName = "screenshot.png"
bucket = storage.bucket()
blob = bucket.blob(fileName)
blob.upload_from_filename(fileName)

# Opt : if you want to make public access from the URL
blob.make_public()

print("your file url", blob.public_url)

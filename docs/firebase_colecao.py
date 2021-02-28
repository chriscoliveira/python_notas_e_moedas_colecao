import pyrebase

#sudo pip install requests
#sudo pip install python-firebase



def baixar_CSV_android():
    config = {
        "apiKey": "AIzaSyDnr73j6rAWweD05JWNBTfUVLC7Y_wi00s",
        "authDomain": "minha-colecao-a01d5.firebaseapp.com",
        "databaseURL": "https://minha-colecao-a01d5.firebaseio.com",
        "projectId": "minha-colecao-a01d5",
        "storageBucket": "minha-colecao-a01d5.appspot.com",
        "messagingSenderId": "275801323997",
        "appId": "1:275801323997:web:5663d46308a2cbb5e29e34"
    }

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password("christian.coliveira@gmail.com", "chr15714n")
    print("Usuario autenticado")


    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    storage.child("Y2hyaXN0aWFuLmNvbGl2ZWlyYUBnbWFpbC5jb20=/bancodados/bancoMoedas.csv").download("bancoMoedas.csv")
    print("Download concluido bancoMoedas")
    storage.child("Y2hyaXN0aWFuLmNvbGl2ZWlyYUBnbWFpbC5jb20=/bancodados/bancoNotas.csv").download("bancoNotas.csv")
    print("Download concluido bancoNotas")





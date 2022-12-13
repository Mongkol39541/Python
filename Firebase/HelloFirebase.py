import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("hellowordfirebase-9c746-firebase-adminsdk-kve97-226f587cb3.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://hellowordfirebase-9c746-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('User') 


hopper_ref = ref.child('gracehop')
hopper_ref = hopper_ref.child('Somsong')
hopper_ref.update({
    'nicknamehfgjfg': 'Amazing Grace'
})

data = ref.get()
print(data)
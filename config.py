import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("crud-project-5a2a5-firebase-adminsdk-fbsvc-d13c090b61.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://crud-project-5a2a5-default-rtdb.firebaseio.com/"
})

pratos_ref = db.reference("pratos")
mesas_ref = db.reference("mesas")
pedidos_ref = db.reference("pedidos")
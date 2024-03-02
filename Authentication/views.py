# views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import initialize_app, auth
import pyrebase
import firebase_admin
from firebase_admin import credentials

config = {
  "apiKey": "AIzaSyDRKSyS7OJt-ulSn4us0L0MGoe_qQv8SrA",
  "authDomain": "respondr-8b7c0.firebaseapp.com",
  "projectId": "respondr-8b7c0",
  "storageBucket": "respondr-8b7c0.appspot.com",
  "messagingSenderId": "884863782470",
  "appId": "1:884863782470:web:836fdab3662ddc959fc447",
  "measurementId": "G-0L4S4P5EZH",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@csrf_exempt
def signIn(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
        except:
            return JsonResponse({"error": "Invalid Credentials!! Please Check your Data"}, status=400)
        session_id = user['idToken']
        request.session['uid'] = str(session_id)
        return JsonResponse({"message": "Logged in successfully", "email": email})

@csrf_exempt
def signUp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        try:
            user = auth.create_user_with_email_and_password(email, password)
            uid = user['localId']
            idtoken = request.session['uid']
        except:
            print()
            return JsonResponse({"error": "Error creating user"}, status=400)
        return JsonResponse({"message": "User created successfully"})
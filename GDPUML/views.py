from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistration
from .models import Signup, Login
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import bcrypt
#----------------------
#python Ml Code

# Training and testing datasets
l1 = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
      'stomach_pain', 'acidity',
      'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety',
      'cold_hands_and_feets', 'mood_swings'
    , 'weight_loss', 'restlessness', 'lethargy', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
      'dehydration',
      'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
      'back_pain',
      'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellowing_of_eyes', 'swelled_lymph_nodes',
      'malaise', 'blurred_and_distorted_vision',
      'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain',
      'weakness_in_limbs',
      'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
      'neck_pain',
      'dizziness', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'excessive_hunger',
      'drying_and_tingling_lips', 'slurred_speech', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
      'movement_stiffness',
      'loss_of_balance', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort',
      'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
      'depression',
      'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation',
      'dischromic _patches',
      'watering_from_eyes', 'family_history', 'mucoid_sputum', 'lack_of_concentration', 'visual_disturbances',
      'blood_in_sputum',
      'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring']

disease = ['Fungal infection', 'Allergy', 'Drug Reaction',
           'Peptic ulcer diseae', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
           ' Migraine', 'Cervical spondylosis',
           'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'Tuberculosis',
           'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
           'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
           'Arthritis', 'Acne', 'Urinary tract infection']

df = pd.read_csv("Training.csv")

df.replace({'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'Drug Reaction': 2,
                          'Peptic ulcer diseae': 3, 'Gastroenteritis': 4, 'Bronchial Asthma': 5, 'Hypertension ': 6,
                          'Migraine': 7, 'Cervical spondylosis': 8,
                          'Paralysis (brain hemorrhage)': 9, 'Jaundice': 10, 'Malaria': 11, 'Chicken pox': 12,
                          'Dengue': 13, 'Typhoid': 14, 'Tuberculosis': 15,
                          'Common Cold': 16, 'Pneumonia': 17, 'Dimorphic hemmorhoids(piles)': 18, 'Hypothyroidism': 19,
                          'Hyperthyroidism': 20, 'Hypoglycemia': 21, 'Arthritis': 22,
                          'Acne': 23, 'Urinary tract infection': 24}}, inplace=True)

X = df[l1]

y = df[["prognosis"]]
np.ravel(y)

# In[5]:


tr = pd.read_csv("Testing.csv")
tr.replace({'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'Drug Reaction': 2, 'Peptic ulcer diseae': 3,
                          'Gastroenteritis': 4,
                          'Bronchial Asthma': 5, 'Hypertension ': 6, 'Migraine': 7, 'Cervical spondylosis': 8,
                          'Paralysis (brain hemorrhage)': 9, 'Jaundice': 10, 'Malaria': 11, 'Chicken pox': 12,
                          'Dengue': 13,
                          'Typhoid': 14, 'Tuberculosis': 15, 'Common Cold': 16, 'Pneumonia': 17,
                          'Dimorphic hemmorhoids(piles)': 18,
                          'Hypothyroidism': 19, 'Hyperthyroidism': 20, 'Hypoglycemia': 21, 'Arthritis': 22, 'Acne': 23,
                          'Urinary tract infection': 24}}, inplace=True)

X_test = tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)


#-----------------------

# Create your views here.
def index(request):
    return render(request, "index.html")


def dashBoard(request):
    if request.session['uname'] is not None:
        return render(request, "dashBoard.html", {'uname': request.session['uname']})


def signup(request):
    if request.session['uname'] is not None:
        return render(request, "dashBoard.html", {'uname': request.session['uname']})
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            # Signup.objects.create(uname=form.uname, uemail=form.uemail, upass=form.upass, udate=form.udate)
            return render(request, 'index.html')
        else:
            return render(request, 'index.html')


def login(request):
    if request.session['uname'] is not None:
        return render(request, "dashBoard.html", {'uname': request.session['uname']})
    request.session['uname'] = ''
    if request.method == 'POST':
        uemail = request.POST['uemaill']
        upass = request.POST['upassl']
        p = Signup.objects.raw('SELECT *  FROM gdpuml_signup where uemail=%s', [uemail])[0]
        if (p.uemail == uemail and p.upass == upass):
            request.session['uname'] = p.uname
            return render(request, 'dashBoard.html')
        else:
            l = "Invalid User Id or Password"
            error = {'inv': l}
            return render(request, 'index.html', error)


def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")


def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get('uname'):
        response += "Name : {0} <br>".format(request.session.get('uname'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('upassword'))
        return HttpResponse(response)
    else:
        return redirect('create/')

def predict_disease(request):
    return HttpResponse("response")

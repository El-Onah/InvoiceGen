# import modules
import streamlit as st
import pyrebase
import datetime as datetime

# configuraton key
firebaseConfig = {
    'apiKey': "AIzaSyADZRvWFJqnkdK1BB_4scJGDew7SSX5hTc",
    'authDomain': "streamlit-invoice.firebaseapp.com",
    'databaseURL': "https://streamlit-invoice-default-rtdb.europe-west1.firebasedatabase.app",
    'projectId': "streamlit-invoice",
    'storageBucket': "streamlit-invoice.appspot.com",
    'messagingSenderId': "356333189411",
    'appId': "1:356333189411:web:c33719e3f8f4d120cb7496",
    'measurementId': "G-3TSP8ZHHND"
}

# firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


# Database
db = firebase.database()
storage = firebase.storage()

st.sidebar.title('Free Invoice Generator!')

# Authentication
choice = st.sidebar.selectbox('login/Sign UP', ['Login', 'Sign Up!'])

email = st.sidebar.text_input('Please Enter Your Email Address')
password = st.sidebar.text_input('Please Enter your Password')

if choice == 'Sign Up!':
    handle = st.sidebar.text_input(
        'Please input your Company Name', value='Default')
    submit = st.sidebar.button('Create my account')

    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Your account has been successfully created')
        st.balloons()
        # sIGN IN
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Your account has been successfully created')
        db.child(user['LocalId']).child('handle').set(handle)
        db.child(user['LocalId']).child('ID').set(user['LocalId'])
        st.title('Welcome' + handle)
        st.info('You may now log in successfully')

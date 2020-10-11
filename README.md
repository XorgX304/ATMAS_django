# Development of Automated Teller Machine Authentication System (ATMAS)

## Introduction

Automated Teller Machine(ATM) has become a vital part of our daily transactions since customers can
access their bank deposit or card details to perform various financial transactions, most specifically cash withdrawals and
balance checking through the medium of ATM. Additionally, ATMs are important to travelers as one can withdraw cash in
foreign countries thanks to ATM. ATM skimming and fraud are major security breaches are frequent for quite some time
now. As currently, the PIN on the card is the only security layer guarding customer’s cash deposits. This work aims to
enhance the standard of security concerning ATMs through means of creating a multibiometric authentication system
comprising of a 6 digit one-time password(OTP) being sent to the registered mobile number and finally performing facial
recognition along with blink detection is used to verify the identity of the customer. Furthermore, this system will free the
customer from the burden of remembering PIN as the random OTP generated itself acts as the PIN. If an unauthorized user
is detected an alert SMS will be sent to the PIN admin.


## Software design
![Flow Chart](https://i.imgur.com/FU8UBym.png)

## Conceptual Model
![Conceptual Model](https://i.imgur.com/PmaiB3x.png)
## Directory Structure

```
├── ATMAS_django
│   └── templates
├── atm_demo
│   ├── migrations
│   └── templates
├── card_login
│   ├── migrations
│   └── templates
├── face_recognition
│   ├── research
│   │   ├── cascades
│   │   │   └── data
│   │   ├── images
│   │   ├── plot_images
│   │   └── sample_images
│   └── templates
│       └── login
└── static
```
## Dependencies
```
asgiref==3.2.10
astroid==2.4.2
certifi==2020.6.20
chardet==3.0.4
cycler==0.10.0
Django==3.1
django-crispy-forms==1.9.2
dlib==19.21.0
idna==2.10
isort==5.4.2
kiwisolver==1.2.0
lazy-object-proxy==1.4.3
matplotlib==3.3.1
mccabe==0.6.1
numpy==1.19.1
opencv-contrib-python==4.4.0.42
Pillow==7.2.0
PyJWT==1.7.1
pylint==2.6.0
pylint-django==2.3.0
pylint-plugin-utils==0.6
pyparsing==2.4.7
python-dateutil==2.8.1
python-decouple==3.3
pytz==2020.1
requests==2.24.0
six==1.15.0
sqlparse==0.3.1
toml==0.10.1
twilio==6.45.0
urllib3==1.25.10
wrapt==1.12.1
```
## Getting Started
1. Create a virtual environment `pip -m virtualenv venv`
2. Source the virtualenv path using `source venv/bin/activate`
3. Install dependencies using `pip install -r requirements.txt`
4. Run `python face_recognition/research/createDataSet.py` to create a dataset of images using webcam or store images in face_recognition/research/images.
5. Run `python face_recognition/research/trainer.py` to make a train the model.
6. Run `python manage.py createsuperuser` to create a superuser
6. Run the server using `python manage.py runserver`
7. Open browser and go to https://localhost:8000/admin then login and add a new record with the userid of face_recognition dataset creation.
8. Open https://localhost:8000 and proceed according to the onscreen directions.

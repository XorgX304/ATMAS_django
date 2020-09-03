from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from ATMAS_django.settings import BASE_DIR
import numpy as np
import cv2


def warn_face(request):
    return render(request, 'warn.html')


def detectFace(request):
    face_cascade = cv2.CascadeClassifier(
        str(BASE_DIR) +
        '/face_recognition/research/cascades/data/haarcascade_frontalface_alt2.xml'
    )

    cap = cv2.VideoCapture(0)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(
        str(BASE_DIR) +
        "/face_recognition/research/trainer.yml")  #Learning the trained data

    getId = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    card_number = request.session[
        'CARD_NUMBER']  #we will use request.session to store the card number
    print(f"CARD_NUMBER is {card_number}")
    userId = 0
    while (True):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            getId, conf = recognizer.predict(gray[y:y + h, x:x + w])
            # print(type(getId))
            # print(type(card_number))
            print(conf)
            if conf < 42 and getId == int(card_number):
                userId = getId
                cv2.putText(img, "Detected", (x, y + h), font, 2, (0, 255, 0),
                            2)
            else:
                cv2.putText(img, "Unknown", (x, y + h), font, 2, (0, 0, 255),
                            2)
        cv2.imshow("Face", img)
        if (cv2.waitKey(1) == ord('q')):
            break
        elif (userId != 0):
            cv2.waitKey(5000)
            break
    print(userId)

    cap.release()
    cv2.destroyAllWindows()
    if userId != 0:
        return redirect('/admin')
    else:
        return redirect('/')

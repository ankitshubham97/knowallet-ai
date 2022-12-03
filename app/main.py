from flask import Flask,render_template,request,jsonify
from app.models.models import db
from app.models.user import UserModel
from app.models.model_encoder import ModelEncoder
import os
from difflib import SequenceMatcher
from datetime import datetime
from dotenv import load_dotenv
from deepface import DeepFace

from passporteye import read_mrz
import datetime
import time
import io
import base64
import sys
from base64 import decodebytes

# Use load_env to trace the path of .env:
load_dotenv('.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}:5432/{PGDATABASE}'.format(
  PGUSER=os.environ["PGUSER"],
  PGPASSWORD=os.environ["PGPASSWORD"],
  PGHOST=os.environ["PGHOST"],
  PGDATABASE=os.environ["PGDATABASE"])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json_encoder = ModelEncoder
db.init_app(app)


@app.route("/")
def home_view():
  return "Welcome to atmos intelligence!"

@app.route("/face", methods = ['POST'])
def face():
  body = request.json
  backends = [
    'opencv', 
    'ssd', 
    'dlib', 
    'mtcnn', 
    'retinaface', 
    'mediapipe'
  ]
  result = DeepFace.verify(
    img1_path = body["img1"],
    img2_path = body["img2"],
    detector_backend = backends[4])

  return {"success": (result["verified"])}


@app.route("/mrz", methods = ['POST'])
def mrz():
  body = request.json
  b64_encoded_image = body["img"].split(",")
  mrz = read_mrz(io.BytesIO(base64.decodebytes(bytes(b64_encoded_image[len(b64_encoded_image)-1], "utf-8")))).__dict__
  passport_dob = mrz["date_of_birth"]
  short_year = int(passport_dob[0:2])
  month = int(passport_dob[2:4])
  day = int(passport_dob[5:6])
  year = 2000 + short_year
  if short_year > 30:
    year = 1900 + short_year
  date_time = datetime.datetime(year, month, day)
  age_in_epochs = int((time.mktime(date_time.timetuple())))
  return {"birthyear": year}
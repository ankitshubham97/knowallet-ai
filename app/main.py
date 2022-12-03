from flask import Flask,render_template,request,jsonify
from app.models.models import db
from app.models.user import UserModel
from app.models.model_encoder import ModelEncoder
import os
from difflib import SequenceMatcher
from datetime import datetime
from dotenv import load_dotenv
from deepface import DeepFace

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

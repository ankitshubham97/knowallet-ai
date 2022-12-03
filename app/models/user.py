import json
from app.models.models import db

class UserModel(db.Model):
  __tablename__ = 'Users'

  id = db.Column(db.Integer, primary_key = True)
  slackId = db.Column(db.String())
  email = db.Column(db.String())
  number = db.Column(db.String())
  name = db.Column(db.String())
  isActive = db.Column(db.Boolean())
  createdAt = db.Column(db.Date())
  updatedAt = db.Column(db.Date())
  

  def __init__(self):
    pass

  def __repr__(self):
    return json.dumps({
      "id": "{self.id}",
      "slackId": "{self.slackId}",          
    })
  
  def to_json(self):
    return {
      "id": self.id,
      "slackId": self.slackId,
      "email": self.email,
      "number": self.number,
      "isActive": self.isActive,
      "createdAt": str(self.createdAt),
      "updatedAt": str(self.updatedAt)
    }
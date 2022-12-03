from app.main import app
import os
from dotenv import load_dotenv

# Use load_env to trace the path of .env:
load_dotenv('.env')

if __name__ == "__main__":
  if (os.environ['FLASK_ENV'] == "development"):
    app.run(debug=True)
  else:
    app.run()
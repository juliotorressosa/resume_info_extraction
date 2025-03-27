import os
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
import warnings
from dotenv import load_dotenv

"""This file connects to the GCP service, an active project, region and account are required."""
  
load_dotenv()
PROJECT_ID = os.getenv('project_id')
REGION = os.getenv("region")


def conn():
  # Suppress warnings (optional, comment out if needed)
  warnings.filterwarnings("ignore")

  # Ensure the JSON key file path is correct and accessible
  key_path = os.getenv('GCP_KEY_PATH', 'vertex-ai-course.json')
  print(key_path)

  try:
    # Load credentials from the JSON key file
    credentials = Credentials.from_service_account_file(
        key_path, scopes=['https://www.googleapis.com/auth/cloud-platform']
    )

    # Now you have authenticated credentials to interact with GCP services
    # (Replace this with your specific GCP API usage)
    print(credentials, "Successfully authenticated with GCP project! to project ")
  except Exception as e:
    print(f"Error connecting to GCP project: {e}")

if __name__ == "__main__":
  conn()

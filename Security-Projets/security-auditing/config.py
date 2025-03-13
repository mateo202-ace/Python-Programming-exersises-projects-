# Importing the 'os' module to interact with the operating system (e.g., handling files, environment variables)
import os

#Azure credentials from env var
AZURE_CLIENT_ID = os.getenv('AZURE_CLIENT_ID')
AZURE_CLIENT_SECRET = os.getenv('AZURE_CLIENT_SECRET')
AZURE_TENANT_ID = os.getenv('AZURE_TENANT_ID')
AZURE_SUBSCRIPTION_ID = os.getenv('AZURE_SUBSCRIPTION_ID')
# this ensures that the script uses eenvironment variables to access Azure securely


#GCP credentials from env var
GCP_CREDENTIALS_PATH = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

#this retirvese the GCP creds form Environment Variable
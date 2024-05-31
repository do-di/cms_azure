import os
import urllib.parse
from urllib.parse import quote_plus

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'AB6C7F1DE983FABF4D38C481A8A9D'

    # BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'dodicms3'
    # BLOB_STORAGE_CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName=dodicms3;AccountKey=nV0/2/LUTFtKQro6vy2gE5mV5xUE0qiM2Q+TyUgU0K+LATG8QspNyMyun0I6AQQfJKb8/t04qiHl+AStArVjmQ==;EndpointSuffix=core.windows.net'
    # BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'dodicms'

    # For Storage emulator
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'devstoreaccount1'
    BLOB_STORAGE_CONNECTION_STRING = os.environ.get('BLOB_STORAGE_CONNECTION_STRING') or 'AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;DefaultEndpointsProtocol=http;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'local-cms'

    # For SQL Localhost
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'localhost'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'local_cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'sa'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '1234'

    # SQL_SERVER = os.environ.get('SQL_SERVER') or 'dodi-cms.database.windows.net'
    # SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'dodi-cms'
    # SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'dodi-admin'
    # SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Abc@1234'

    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + quote_plus(SQL_PASSWORD) + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect={}".format(
        quote_plus(
            "DRIVER={ODBC Driver 17 for SQL Server};"+"SERVER={};DATABASE={};UID={};PWD={};".format(SQL_SERVER, SQL_DATABASE, SQL_USER_NAME, SQL_PASSWORD)
        )
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    # CLIENT_SECRET = "6ed8Q~60lTvYP5124X6dVZ1Q-~lQJjWcbHFRMb3T"
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'test_ahihi'
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    # CLIENT_ID = "d970448a-fc19-4c99-b1e3-da66678cd7de"
    CLIENT_ID = os.environ.get('CLIENT_ID') or 'test_ahihi'


    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
#!flask/bin/python
from app import app

SERVER_NAME = '0.0.0.0'
SERVER_PORT = 5000

app.run(SERVER_NAME, SERVER_PORT, debug = True)

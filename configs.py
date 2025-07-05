import os

API_ID = int(os.getenv("API_ID", 22250562))
API_HASH = os.getenv("API_HASH", "07754d3bdc27193318ae5f6e6c8016af")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8110392842:AAFkUeghnvu1XHulOh-EwlCa_tW1Qi2tHQw")
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://claw-earning:5213680099@cluster0.je3b1k7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", -1002260555414))

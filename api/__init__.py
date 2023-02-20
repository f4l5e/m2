from flask import Flask


api = Flask(__name__)

@api.get("/")
def status():
    return {"status" : "success"}






if __name__ == "__main__":
    api.run(host="0.0.0.0")
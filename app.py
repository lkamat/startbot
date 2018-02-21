from flask import Flask
from flask import render_template,jsonify,request
import requests
from models import *
from knowledge import *
import random



app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat',methods=['POST'])
def chat():
    try:
        user_message = request.form["text"]
        response = requests.get("http://localhost:5000/parse",params={"q":user_message})
        response = response.json()
        print(response)
        entities = response.get("entities")
        intent = response.get("intent")
        print("Intent {}, Entities {}".format(intent['name'],entities))
        if intent['name'] == "startup_search":
            response_text = startup_search(entities)
        elif intent['name'] == "startup_info":
            response_text = startup_info(entities)
        elif intent['name'] == "affirm":
            response_text = affirm()
        elif intent['name'] == "greet":
            response_text = greeting()
        elif intent['name'] == "goodbye":
            response_text = goodbye()
        else:
            response_text = "Sorry, can not help at this time"
        return jsonify({"status":"success","response":response_text})
        #return 'OK'
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})

app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)
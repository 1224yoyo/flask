from flask import Flask, request


app=Flask(__name__)

open_web = True

flask_key=750701

flask_key=str(flask_key)

@app.route("/")
def home():
    global open_web

    if open_web:
        return "True"
    else:
        return "False"
    
@app.route("/on")
def web_on():
    global open_web
    if request.args.get("key")==flask_key: open_web = True
    else:return"key不正確"
    return "網站已開啟"

@app.route("/off")
def web_off():
    global open_web
    if request.args.get("key")==flask_key: open_web = False
    else:return"key不正確"
    return "網站已關閉"

app.run(host="0.0.0.0", port=5000)

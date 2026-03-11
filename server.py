from flask import Flask


app=Flask(__name__)

open_web = True


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
    open_web = True
    return "網站已開啟"

@app.route("/off")
def web_off():
    global open_web
    open_web = False
    return "網站已關閉"

app.run(host="0.0.0.0", port=5000)
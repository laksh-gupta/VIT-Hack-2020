from flask import Flask, redirect, url_for, request, render_template, jsonify
import vithack_final

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'pymdb'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/pymdb'


@app.route("/")
def Welcome():
    message = "Welcome, This is the IPL chatbot."
    return render_template("welcome.html", message = message)


@app.route("/interact", methods=['GET','POST'])
def interact():
    if(request.method == "GET"):
        return render_template("interact.html")
    elif request.method == "POST":
        a = request.json
        print(a)
        b = vithack_final.main_function(a.usr_in)
        return jsonify(result=b)

if __name__ == '__main__':
    app.debug = True
    app.run(port = 5000, debug = True)
from flask import Flask, render_template, request
from web.database import init_db
from web.models import User
from web.database import db_session



app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_data")
def add_data():
    init_db()
    return render_template("add_data.html")

@app.route('/result',methods = ['POST'])#['POST', 'GET']
def result():
   if request.method == 'POST':
      u = User(request.form['name'],request.form['age'],request.form['height'],request.form['weight'])
      db_session.add(u)
      db_session.commit()
      return render_template("result.html",data = u.query.all())

@app.route("/personal")
def personal():
    
    return render_template("personal.html")


@app.route("/morning")
def morning():
    return render_template("morning.html")


@app.route("/ok_data",methods=['POST'])
def okdata():
    dish_text = request.form['dish']
    return render_template("ok_data.html",text=dish_text)


@app.route("/confirmmorning")
def confirmmorning():
    return render_template("confirmmorning.html")


@app.route("/lunch")
def lunch():
    return render_template("lunch.html")


@app.route("/confirmlunch")
def confirmlunch():
    return render_template("confirmlunch.html")


@app.route("/dinner")
def dinner():
    return render_template("dinner.html")


@app.route("/confirmdinner")
def confirmdinner():
    return render_template("confirmdinner.html")


# if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8080, debug=True)

# ---- YOUR APP STARTS HERE ----

# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import shout


# -- Initialization section --
app = Flask(__name__)
props = {}
# -- Routes section --

# INDEX
@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")


@app.route('/sendUsername', methods=['GET','POST'])
def handleUsername():
  global props
  if request.method == 'GET':
    return "Uhhhh an error occured, but why tho..."
  else:
    print(request.form)
    username = request.form["username"]
    print(username)
    loudname = shout(username)
    props = {
      "loudname":loudname,
      "username":username
    }
    return render_template('carculator.html', props=props)

#This is the second page you go to; right after you hit submit on homepage
@app.route('/sendIncome', methods=['GET', 'POST'])
def handleIncome():
  if request.method == 'GET':
    return "Uhhhh an error occured"
  else:
    check = request.form.get('check')
    if check == 'on':
      print(request.form)
      income = request.form["income"]
      print(income)
      income = round((float(income)*12) * 0.15)
      global props
      props["income"]=income
    else:
      print(request.form)
      income = request.form["income"]
      print(income)
      income = round(float(income) * 0.15)
      props["income"]=income
  return render_template('results.html', props=props)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

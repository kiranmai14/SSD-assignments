from enum import unique
from flask import Flask, request,session
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from sqlalchemy.orm import session
from flask import session as sess
# import bill

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/restaurant'
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(120))
    username = db.Column(db.String(80))
    password = db.Column(db.String(120))

    def __init__(self, type, username, password):
        self.type = type
        self.username = username
        self.password = password

    # def __repr__(self):
    #     return '<User %r>' % self.username
    
    def getType(self):
        return  self.type


class Menu(db.Model):


    item_id = db.Column(db.Integer, primary_key=True)
    half_plate = db.Column(db.Numeric(20,2))
    full_plate = db.Column(db.Numeric(20,2))

    def __init__(self, item_id, half_plate, full_plate):
        self.item_id = item_id
        self.half_plate = half_plate
        self.full_plate = full_plate

    # def __repr__(self):
    #     return '<User %r>' % self.username
    
    def getType(self):
        return  self.type

db.drop_all()
db.create_all()

@app.route('/')
def root():
    sess.pop('type',None) 
    sess.pop('loggedIn',None) 
    return  "This is root"
    
@app.route("/signup", methods=['POST'])
def signup():
    if(request.method == 'POST'):
        data = request.get_json()
        type = data['type']
        username = data['username']
        password = data['password']
        obj = User(type=type, username=username, password=password)
        db.session.add(obj)
        db.session.commit()
        return "User created successfully"

@app.route("/login", methods=['POST'])
def update():
     if(request.method == 'POST'):

        sess.pop('type',None) 
        sess.pop('loggedIn',None) 
        data = request.get_json()
        username = data['username']
        password = data['password']
        check_user = User.query.filter_by(username=username, password=password).first()
        if(check_user is None):
            return "id not found"
        else:
            sess['loggedIn'] = True
            sess['type'] = check_user.getType()
            return "loggedin successfully"

@app.route("/logout", methods=['GET'])
def logout():
     if(request.method == 'GET'):
        sess.pop('type',None) 
        sess.pop('loggedIn',None) 
        return "logged out successfully"

@app.route("/additem", methods=['POST'])
def additem():

    if not sess.get("loggedIn"):
        return "you are not loggedin"
    
    if sess.get("type") != "chef":
        return "you are allowed to perform this action"
    
    if(request.method == 'POST'):

        data = request.get_json()
        item_id = data['item_id']
        half_plate = data['half_plate']
        full_plate = data['full_plate']
        menu_item = Menu(item_id=item_id,half_plate=float(half_plate),full_plate=float(full_plate))
        db.session.add(menu_item)
        db.session.commit()
        return "added successfully"

if __name__ == '__main__':
    app.run(port=9001,debug=True)

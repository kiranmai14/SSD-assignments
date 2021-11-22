from enum import unique
from os import pipe
from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from sqlalchemy.orm import session
from flask import session as sess

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/restaurant'
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(120))
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, type, username, password):
        self.type = type
        self.username = username
        self.password = password

    # def __repr__(self):
    #     return '<User %r>' % self.username

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id


class Menu(db.Model):

    item_id = db.Column(db.Integer, primary_key=True)
    half_plate = db.Column(db.Numeric(20, 2))
    full_plate = db.Column(db.Numeric(20, 2))

    def __init__(self, item_id, half_plate, full_plate):
        self.item_id = item_id
        self.half_plate = half_plate
        self.full_plate = full_plate

    # def __repr__(self):
    #     return '<User %r>' % self.username

    def getType(self):
        return self.type

    def get_item(self):
        item = []
        item.append(self.item_id)
        item.append(self.half_plate)
        item.append(self.full_plate)
        return item


class Transaction(db.Model):

    user_id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    total = db.Column(db.Numeric(20, 2))
    tip = db.Column(db.Integer)
    discount = db.Column(db.Numeric(20, 2))
    final_bill = db.Column(db.Numeric(20, 2))
    people = db.Column(db.Integer)

    def __init__(self, user_id, total, tip, discount, final_bill, people):
        self.user_id = user_id
        self.total = total
        self.tip = tip
        self.discount = discount
        self.final_bill = final_bill
        self.people = people

    def get_transaction_id(self):
        return self.transaction_id

    def get_transaction_data(self):


        transaction_details = {}
        transaction_details["total"] = self.total
        transaction_details["tip"] = self.tip
        transaction_details["discount"] = self.discount
        transaction_details["final_bill"] = self.final_bill
        transaction_details["people"] = self.people
        return transaction_details


class Items(db.Model):

    user_id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, primary_key=True)
    is_half_plate = db.Column(db.Boolean, unique=False, default=False)
    is_full_plate = db.Column(db.Boolean, unique=False, default=False)
    quantity = db.Column(db.Integer)

    def __init__(self, user_id, transaction_id, item_id, is_half_plate, is_full_plate, quantity):
        self.user_id = user_id
        self.transaction_id = transaction_id
        self.item_id = item_id
        self.is_half_plate = is_half_plate
        self.is_full_plate = is_full_plate
        self.quantity = quantity

    def get_item_data(self):

        price_of_each_item = []

        price_of_each_item.append(self.item_id)
        if(self.is_half_plate):
            price_of_each_item.append("Half")
        elif(self.is_full_plate):
            price_of_each_item.append("Full")
        price_of_each_item.append(self.quantity)

        return price_of_each_item


# db.drop_all()
# db.create_all()
# db.session.commit()

@app.route('/')
def root():
    sess.pop('type', None)
    sess.pop('id', None)
    sess.pop('loggedIn', None)
    return "This is root"


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
def login():
    if(request.method == 'POST'):
        sess.pop('type', None)
        sess.pop('loggedIn', None)
        sess.pop('id', None)
        data = request.get_json()
        username = data['username']
        password = data['password']
        check_user = User.query.filter_by(
            username=username, password=password).first()
        if(check_user is None):
            return "id not found"
        else:
            sess['loggedIn'] = True
            sess['type'] = check_user.get_type()
            sess['id'] = check_user.get_id()
            return "loggedin successfully"


@app.route("/logout", methods=['GET'])
def logout():
    if(request.method == 'GET'):
        sess.pop('type', None)
        sess.pop('id', None)
        sess.pop('loggedIn', None)
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
        menu_item = Menu(item_id=item_id, half_plate=float(
            half_plate), full_plate=float(full_plate))
        db.session.add(menu_item)
        db.session.commit()
        return "added successfully"


@app.route("/getMenu", methods=['GET'])
def display_menu():

    if not sess.get("loggedIn"):
        return "you are not loggedin"

    menu_card = {}
    menu_objects = Menu.query.all()
    for menu_obj in menu_objects:
        lines = menu_obj.get_item()
        menu_card[lines[0]] = {'half_plate': lines[1], 'full_plate': lines[2]}
    return jsonify(menu_card)


@app.route("/transacton", methods=['PUT'])
def insert_transaction_data():

    if not sess.get("loggedIn"):
        return "you are not loggedin"

    transaction_details = request.get_json()
    ordered_items = transaction_details["ordered_items"]
    total = transaction_details["total"]
    tip = transaction_details["tip"][:-1]
    discount = transaction_details["discount"]
    final_bill = transaction_details["final_bill"]
    people = transaction_details["people"]
    user_id = sess["id"]
    transaction_item = Transaction(
        user_id, total, tip, discount, final_bill, people)
    db.session.add(transaction_item)
    db.session.commit()

    transaction_id = transaction_item.get_transaction_id()
    for key, value in ordered_items.items():
        print(key, value)
        id = int(key.split(" ")[0])
        type = key.split(" ")[1]
        is_half_plate = False
        is_full_plate = False
        if(type == "half"):
            is_half_plate = True
        if(type == "full"):
            is_full_plate = True
        order_item = Items(user_id, transaction_id, id,
                           is_half_plate, is_full_plate, value)
        db.session.add(order_item)
        db.session.commit()
    return "transaction details inserted successfully"


@app.route("/showtransactionslist", methods=['GET'])
def show_transactions():

    if not sess.get("loggedIn"):
        return "you are not loggedin"

    user_id = sess["id"]
    transaction_objects = Transaction.query.filter_by(user_id=user_id).all()
    transaction_ids = []

    for obj in transaction_objects:
        transaction_ids.append(obj.get_transaction_id())
    
    return jsonify({"ids" : transaction_ids})



@app.route("/showbreakdown", methods=['POST'])
def show_breakdown():

    if not sess.get("loggedIn"):
        return "you are not loggedin"

    data = request.get_json()
    transaction_id = data["transaction_id"]
    user_id = sess["id"]

    transaction_object = Transaction.query.filter_by(user_id=user_id,transaction_id = transaction_id).first()
    transaction_details = transaction_object.get_transaction_data()


    items_obj = Items.query.filter_by(user_id=user_id,transaction_id = transaction_id).all()

    price_of_each_item = []

    for obj in items_obj:
        price_of_each_item.append(obj.get_item_data())

    transaction_details["ordered_items"] = price_of_each_item
    return jsonify(transaction_details)


if __name__ == '__main__':
    app.run(port=8000, debug=True)

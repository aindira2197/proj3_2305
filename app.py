from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


@app.route('/')
def home():

    products = Product.query.all()

    text = ""

    for product in products:
        text += f"{product.id} - {product.name}<br>"

    return text


@app.route('/add/<name>')
def add(name):

    product = Product(name=name)

    db.session.add(product)
    db.session.commit()

    return "Product Added"


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)

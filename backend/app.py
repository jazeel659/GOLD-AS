from flask import Flask
import sqlite3
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origin": "localhost"
    }
})


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = make_dicts
    return conn


@app.route('/gold/safe-gold')
def lista():
    conn = get_db_connection()
    safe = conn.execute(
        'SELECT * FROM gold_list ').fetchall()
    conn.close()
    return safe


# @app.route('/gold/mmtc')
# def list():
#     conn = get_db_connection()
#     safe = conn.execute(
#         'SELECT * FROM gold_list where category="MMTC-PAMP"').fetchall()
#     conn.close()
#     return safe


# @app.route('/laxmi-price')
# def laxmi():
#     price = {}
#     conn = get_db_connection()
#     laxmi = conn.execute(
#         """SELECT price FROM GOLD WHERE name='laxmi'""").fetchone()
#     conn.close()
#     laxmi. headers["Access-Control-Allow-Origin"] = "*"
#     price["price"] = laxmi["price"]
#     return price


# @app.route('/<brand>/gold')
# def details(brand):
#     details = {}
#     conn = get_db_connection()
#     detail = conn.execute(
#         'SELECT * FROM GOLD WHERE name=?', (brand,)).fetchall()
#     conn.close()
#     details["name"] = detail[0][1]
#     details["price"] = detail[0][2]
#     details["purity"] = detail[0][1]
#     details["Email"] = detail[0][3]
#     details["image_url"] = detail[0][4]
#     return jsonify(details)


# @app.route('/')
# def main():
#     return render_template('main.html')

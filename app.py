from flask import Flask, render_template, request
from DB_handling import cursor, db
import joblib

model = joblib.load("house_price.pkl")

app = Flask(__name__)

@app.route('/')
def user_input_page():
    return render_template("index.html")

@app.route("/submit_form", methods=['GET', 'POST'])
def house_price():
    area = request.args.get("area")
    area = int(area)
    price_predicted = model.predict([[area]])[0]
    query = "INSERT INTO house_info (area, price_predicted) VALUES (%s, %s)"
    cursor.execute(query, (area, float(price_predicted),))
    db.commit()
    return render_template("result.html", price=price_predicted)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


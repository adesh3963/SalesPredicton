from flask import Flask, request,jsonify, render_template
from data_collecting.collect_data import CollectData
from prediction import Prediction
import logging as lg


lg.basicConfig(filename= "./logging/logs.log",level= lg.INFO, format = '%(asctime)s %(message)s')
app = Flask(__name__)


@app.route("/")
def home_page():
    lg.info("Home page opened")
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def prediction():
    try:
        lg.info("/prediction URl called")
        if request.method == "POST":
            form = request.form
            # print(request.form)
            lg.info("Data from the web page has arrinved.")
            get_data = CollectData(lg)
            data = get_data.collect_data(form)
            lg.info("Data collection done")
            lg.info("Data is going for prediction.")
            pred = Prediction(lg)
            result = pred.predict(data)
            lg.info("Result returning to page")
            return render_template("index.html", result=round(result, 2))
        else:
            return render_template("index.html")

    except Exception as e:
        lg.error("ERROR occured %s"%str(e))
        raise e


if __name__ == "__main__":
    app.run()

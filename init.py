# initialize the app and connect to the database
import pymongo

client = pymongo.MongoClient("mongodb+srv://n26110320:dsLIc40TeklfczEv@cluster0205.2thmpz6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0205")
db = client.Health_Center
print("Database connected")

# create flask server
from flask import *

app = Flask(__name__,
            static_folder = "./public",
            static_url_path = "/"
)
app.secret_key = "a_secret_key"

@app.route("/")
def home():
    return render_template("index.html"), 200

@app.route("/success")
def success():
    message = request.args.get("msg", "Success")
    return render_template("success.html", message = message), 200

@app.route("/type/historyData")
def typeHistoryData():
    return render_template("historyData.html"), 200

@app.route("/upload/historyData", methods=["POST"])
def uploadData():
    try:
        patientId = request.form["patientId"]
        totalTime = request.form["totalTime"]
        cycleTime = request.form["cycleTime"]
        stimulationTime = request.form["stimulationTime"]
        collection = db.historyData
        collection.insert_one({"patientId": patientId, "totalTime": totalTime, "cycleTime": cycleTime, "stimulationTime": stimulationTime})
        return redirect("/success?msg=Upload success"), 200
    except KeyError:
        return "Missing form data", 400
    except Exception as e:
        return str(e), 500

@app.route("/type/PPG&EDA")
def typePPG():
    return render_template("PPG&EDA.html"), 200

@app.route("/upload/PPG&EDA", methods=["POST"])
def uploadPPG():
    try:
        patientId = request.form["patientId"]
        PPG = request.form["ppg"]
        EDA = request.form.get("eda", "")
        PPG_array = [float(x) for x in PPG.split(" ")]
        collection = db.PPG_EDA
        collection.insert_one({"patientId": patientId, "PPG": PPG_array, "EDA": EDA})
        return redirect("/success?msg=Upload success"), 200
    except KeyError:
        return "Missing form data", 400
    except Exception as e:
        return str(e), 500

@app.route("/delete/PPG&EDA", methods=["POST"])
def deletePPG():
    try:
        collection = db.PPG_EDA
        latest_match_data = collection.find_one({"patientId": request.form["patientId"]}, sort=[("timestamp", -1)])
        if latest_match_data:
            # 刪除最新一筆資料
            result = collection.delete_one({"_id": latest_match_data["_id"]})
            delete_count_str = "已刪除的資料筆數：" + str(result.deleted_count)
            success_url = "/success?msg=" + delete_count_str
            return redirect(success_url), 200
        else:
            return "找不到指定 patientId 的資料。", 404
    except Exception as e:
        return str(e), 500
    
@app.route("/test")
def testKeyError():
    my_dict = {"a": 1, "b": 2}
    try:
        value = my_dict["c"]
        return str(value), 200
    except KeyError as e:
        return "KeyError occurred", 400

app.run(debug=True, port=3000)
from flask import Flask, jsonify
from database import init_db
from routes.drivers import drivers
from routes.vehicles import vehicles
from routes.route import route
from routes.packages import packages

init_db()

app = Flask(__name__)
app.register_blueprint(drivers, url_prefix="/drivers")
app.register_blueprint(vehicles, url_prefix="/vehicles")
app.register_blueprint(packages, url_prefix="/packages")
app.register_blueprint(route, url_prefix="/route")


@app.route("/")
def home():
    return jsonify({"message": "Server Online"})


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template
from flask_cors import CORS
from database import init_db
from routes.drivers import drivers
from routes.vehicles import vehicles
from routes.route import route
from routes.packages import packages

init_db()

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)
app.register_blueprint(drivers, url_prefix="/drivers")
app.register_blueprint(vehicles, url_prefix="/vehicles")
app.register_blueprint(packages, url_prefix="/packages")
app.register_blueprint(route, url_prefix="/route")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
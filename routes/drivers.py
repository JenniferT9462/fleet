from flask import jsonify, request, Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection

drivers = Blueprint("drivers", __name__)

@drivers.route("/")
def get_drivers():
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory = RealDictCursor)
        cur.execute("""
                        SELECT * FROM drivers
                    """)
        rows = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify(rows)
    

@drivers.route("/", methods=["POST"])
def create_driver():
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute("""
                    insert into drivers
                    (driver_id, name, license_type)
                    values 
                    (%s, %s, %s)
            """, (data["driver_id"],data["name"], data["license_type"]))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
       return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Created"}), 201


@drivers.route("/<int:id>", methods=["PUT"])
def update_driver(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        print(data)
        cur.execute("""
                    update drivers
                    set name = %s ,
                        license_type = %s
                    where driver_id = %s
            """, (data["name"], data["license_type"], id))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"{e}"}), 500
    else:
        return jsonify({"message": "Object Updated"}), 201
    
@drivers.route("/<int:id>", methods=["DELETE"])
def delete_driver(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        cur.execute("""
                    delete from drivers
                    where driver_id = %s
            """, (id, ))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Deleted"}), 201
from flask import jsonify, request, Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection

vehicles = Blueprint("vehicles", __name__)

@vehicles.route("/")
def get_vehicles():
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory = RealDictCursor)
        cur.execute("""
                        SELECT * FROM vehicles
                    """)
        rows = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify(rows)
    

@vehicles.route("/", methods=["POST"])
def create_vehicle():
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute("""
                    insert into vehicles
                    (vehicle_id, license_plate, model, driver_id)
                    values
                    (%s, %s, %s, %s)
            """, (data["vehicle_id"], data["license_plate"], data["model"], data.get("driver_id")))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
       return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Created"}), 201


@vehicles.route("/<int:id>", methods=["PUT"])
def update_vehicle(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute("""
                    update vehicles
                    set license_plate = %s,
                        model = %s,
                        driver_id = %s
                    where vehicle_id = %s
            """, (data["license_plate"], data["model"], data.get("driver_id"), id))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"{e}"}), 500
    else:
        return jsonify({"message": "Object Updated"}), 201
    
@vehicles.route("/<int:id>", methods=["DELETE"])
def delete_vehicle(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        cur.execute("""
                    delete from vehicles
                    where vehicle_id = %s
            """, (id, ))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Deleted"}), 201
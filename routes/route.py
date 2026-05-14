from flask import jsonify, request, Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection

route = Blueprint("route", __name__)

@route.route("/")
def get_routes():
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory = RealDictCursor)
        cur.execute("""
                        SELECT * FROM route
                    """)
        rows = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify(rows)
    

@route.route("/", methods=["POST"])
def create_route():
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute("""
                    insert into route
                    (route_id, date, service_zone)
                    values 
                    (%s, %s, %s)
            """, (data["route_id"],data["date"], data["service_zone"]))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
       return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Created"}), 201


@route.route("/<int:id>", methods=["PUT"])
def update_route(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        print(data)
        cur.execute("""
                    update route
                    set date = %s ,
                        service_zone = %s
                    where route_id = %s
            """, (data["date"], data["service_zone"], id))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"{e}"}), 500
    else:
        return jsonify({"message": "Object Updated"}), 201
    
@route.route("/<int:id>", methods=["DELETE"])
def delete_route(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        cur.execute("""
                    delete from route
                    where route_id = %s
            """, (id, ))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Deleted"}), 201
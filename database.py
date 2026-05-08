import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    conn = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        sslmode = os.getenv("DB_SSLMODE"),
    )
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
            

                create table  drivers
                (
    
                    driver_id SERIAL PRIMARY KEY,
                    name VARCHAR(50),
                    license_type VARCHAR(50)
                    
                );

                create table  vehicles
                (
    
                    vehicle_id SERIAL PRIMARY KEY,
                    license_plate VARCHAR(50),
                    model VARCHAR(50),
                    driver_id INT UNIQUE, 
                    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id)
                    
                );

                create table  route
                (
    
                    route_id SERIAL PRIMARY KEY,
                    service_zone VARCHAR(50),
                    date date,
                    driver_id INT,
                    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id)
                    
                );

                create table packages
                (
    
                    package_id SERIAL PRIMARY KEY,
                    description VARCHAR(250),
                    weight int,
                    route_id INT,
                    FOREIGN KEY (route_id) REFERENCES route(route_id)
                    
                )

                """)
    conn.commit()
    cur.close()
    conn.close()
    print("Database Ready!")




# Last-Mile Logistics & Fleet Management System

A robust back-end database system built with **Python Flask** and **PostgreSQL** to manage daily delivery operations, vehicle assignments, and package routing.

## 🚚 Project Overview

This system implements a relational database structure based on a logistics case study. It manages the relationships between Drivers, Vehicles, Delivery Routes, and Packages, ensuring data integrity through Foreign Key constraints and specific cardinality rules.

### Business Logic & Cardinality

* **Driver ↔ Vehicle (1:1):** Each vehicle is assigned to exactly one driver using a `UNIQUE` constraint on the `driver_id`.
* **Route ↔ Packages (1:N):** A single route contains multiple packages, but each package belongs to only one route.
* **Driver ↔ Route (1:N):** Drivers are assigned to specific routes for daily operations.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Framework:** Flask
* **Database:** PostgreSQL
* **Library:** Psycopg2 (PostgreSQL adapter)

## 🚀 Getting Started

### 1. Prerequisites

- Python installed
- PostgreSQL database (local or hosted)

### 2. Installation

Clone the repository and install the dependencies:

```bash
    pip install -r requirements.txt
```

### Environment Variables

Create a .env file in the root directory and add your database credentials:

```bash
DB_HOST=your_host
DB_PORT=5432
DB_NAME=your_db_name
DB_USER=your_user
DB_PASSWORD=your_password
DB_SSLMODE=require
```

### Initialize Database

The system is designed to initialize the schema automatically upon the first run of the Flask app via the init_db() method in database.py.

### Running the App

```bash
python app.py
```

## 📋 API Endpoints (CRUD)

### Drivers

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | /drivers | List all drivers |
| POST | /drivers | Register a new driver |
| PUT | /drivers/`<id>` | Update driver details |
| DELETE | /drivers/`<id>` | Remove a driver |

### Packages

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | /packages | List all packages |
| POST | /packages | Register a new package |
| PUT | /packages/`<id>` | Update package details |
| DELETE | /packages/`<id>` | Remove a package |

### Vehicles

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | /vehicles | List all vehicles |
| POST | /vehicles | Register a new vehicle |
| PUT | /vehicles/`<id>` | Update vehicle details |
| DELETE | /vehicles/`<id>` | Remove a vehicle |

### Routes

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | /route | List all route |
| POST | /route | Register a new route |
| PUT | /route/`<id>` | Update route details |
| DELETE | /route/`<id>` | Remove a route |

---

### One Last Step: Generate `requirements.txt`

To make sure the `pip install -r requirements.txt` command in the README works, run this in your terminal while your environment is active:

```bash
pip freeze > requirements.txt
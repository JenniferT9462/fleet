# Fleet API Documentation

A REST API for managing a fleet of drivers, vehicles, routes, and packages.

**Base URL:** `http://127.0.0.1:5000`  
**Deployed Backend:** `http://codex-jennifer.duckdns.org/`
**Stack:** Python / Flask, PostgreSQL  
**Format:** All request and response bodies are JSON.

---

## Health Check

### `GET /`

Returns server status.

**Response `200`**
```json
{ "message": "Server Online" }
```

---

## Drivers

### `GET /drivers`

Returns all drivers.

**Response `200`**
```json
[
  {
    "driver_id": 1,
    "name": "Jenn Tarleton",
    "license_type": "basic"
  }
]
```

---

### `POST /drivers`

Creates a new driver.

**Request Body**
| Field | Type | Max Length | Required |
|---|---|---|---|
| `driver_id` | integer | — | Yes |
| `name` | string | 50 | Yes |
| `license_type` | string | 50 | Yes |

**Example**
```json
{
  "driver_id": 1,
  "name": "Jenn Tarleton",
  "license_type": "basic"
}
```

**Response `201`**
```json
{ "message": "Object Created" }
```

---

### `PUT /drivers/<id>`

Updates an existing driver.

**Path Parameter:** `id` — the `driver_id` to update

**Request Body**
| Field | Type | Max Length | Required |
|---|---|---|---|
| `name` | string | 50 | Yes |
| `license_type` | string | 50 | Yes |

**Response `201`**
```json
{ "message": "Object Updated" }
```

---

### `DELETE /drivers/<id>`

Deletes a driver.

**Path Parameter:** `id` — the `driver_id` to delete

**Response `201`**
```json
{ "message": "Object Deleted" }
```

---

## Vehicles

### `GET /vehicles`

Returns all vehicles.

**Response `200`**
```json
[
  {
    "vehicle_id": 1,
    "license_plate": "456hgd",
    "model": "Kia Soul",
    "driver_id": 1
  }
]
```

---

### `POST /vehicles`

Creates a new vehicle.

**Request Body**
| Field | Type | Max Length | Required |
|---|---|---|---|
| `vehicle_id` | integer | — | Yes |
| `license_plate` | string | 50 | Yes |
| `model` | string | 50 | Yes |

**Example**
```json
{
  "vehicle_id": 1,
  "license_plate": "456hgd",
  "model": "Kia Soul"
}
```

**Response `201`**
```json
{ "message": "Object Created" }
```

---

### `PUT /vehicles/<id>`

Updates an existing vehicle.

**Path Parameter:** `id` — the `vehicle_id` to update

**Request Body**
| Field | Type | Max Length | Required |
|---|---|---|---|
| `license_plate` | string | 50 | Yes |
| `model` | string | 50 | Yes |

**Response `201`**
```json
{ "message": "Object Updated" }
```

---

### `DELETE /vehicles/<id>`

Deletes a vehicle.

**Path Parameter:** `id` — the `vehicle_id` to delete

**Response `201`**
```json
{ "message": "Object Deleted" }
```

---

## Routes

### `GET /route`

Returns all routes.

**Response `200`**
```json
[
  {
    "route_id": 1,
    "service_zone": "east-4",
    "date": "2026-04-23",
    "driver_id": 1
  }
]
```

---

### `POST /route`

Creates a new route.

**Request Body**
| Field | Type | Format | Required |
|---|---|---|---|
| `route_id` | integer | — | Yes |
| `date` | string | `MM-DD-YY` | Yes |
| `service_zone` | string (max 50) | — | Yes |

**Example**
```json
{
  "route_id": 1,
  "date": "04-23-26",
  "service_zone": "east-4"
}
```

**Response `201`**
```json
{ "message": "Object Created" }
```

---

### `PUT /route/<id>`

Updates an existing route.

**Path Parameter:** `id` — the `route_id` to update

**Request Body**
| Field | Type | Required |
|---|---|---|
| `date` | string (`MM-DD-YY`) | Yes |
| `service_zone` | string (max 50) | Yes |

**Response `201`**
```json
{ "message": "Object Updated" }
```

---

### `DELETE /route/<id>`

Deletes a route.

**Path Parameter:** `id` — the `route_id` to delete

**Response `201`**
```json
{ "message": "Object Deleted" }
```

---

## Packages

### `GET /packages`

Returns all packages.

**Response `200`**
```json
[
  {
    "package_id": 1,
    "description": "Two iPads",
    "weight": 23.5,
    "route_id": 1
  }
]
```

---

### `POST /packages`

Creates a new package.

**Request Body**
| Field | Type | Max Length | Required |
|---|---|---|---|
| `package_id` | integer | — | Yes |
| `description` | string | 250 | Yes |
| `weight` | number | — | Yes |
| `route_id` | integer | — | Yes |

**Example**
```json
{
  "package_id": 1,
  "description": "Two iPads",
  "weight": 23.5,
  "route_id": 1
}
```

**Response `201`**
```json
{ "message": "Object Created" }
```

---

### `PUT /packages/<id>`

Updates an existing package.

**Path Parameter:** `id` — the `package_id` to update

**Request Body**
| Field | Type | Max Length | Required |
|---|---|---|---|
| `description` | string | 250 | Yes |
| `weight` | number | — | Yes |

**Response `201`**
```json
{ "message": "Object Updated" }
```

---

### `DELETE /packages/<id>`

Deletes a package.

**Path Parameter:** `id` — the `package_id` to delete

**Response `201`**
```json
{ "message": "Object Deleted" }
```

---

## Error Responses

All endpoints return `500` on unexpected errors.

```json
{ "error": "<error message>" }
```

---

## Data Model

```
drivers ──< routes ──< packages
   │
   └── vehicles (1:1)
```

- One driver can have many routes
- One driver has at most one vehicle
- One route can have many packages

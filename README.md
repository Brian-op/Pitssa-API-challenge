# Pitssa-API-challenge

A RESTful Flask API for managing pizzas, restaurants, and their price offerings.

---

##  Setup Instructions

1. **Fork the repo**

2. **Clone the repo**

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

3. **Set up virtual environment with Pipenv**

```bash
pipenv install
pipenv shell
```

4. **Set environment variable for Flask**

```bash
export FLASK_APP=server
```

5. **Run the app**

```bash
flask run
```

##  Database Migration & Seeding

**(one) Initialize & migrate DB**

```bash
flask db init
flask db migrate -m "your prefered message"
flask db upgrade
```

**(two) Seed data**

```bash
PYTHONPATH=. python server/seed.py
```

##  Routes Summary

### GET /pizzas

Returns all pizzas

### POST /pizzas

Creates a new pizza

```json
{
  "name": "Margherita",
  "ingredients": "Tomato, Mozzarella, Basil"
}
```

### GET /restaurants

Returns all restaurants

### GET /restaurants/\:id

Returns one restaurant with pizzas offered

### DELETE /restaurants/\:id

Deletes a restaurant and all associated RestaurantPizzas

### POST /restaurants

Creates a new restaurant

```json
{
  "name": "Mama Mia",
  "address": "Ngong Lane St"
}
```

### POST /restaurant\_pizzas

Creates a new restaurant pizza (price entry)

```json
{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

---

## Validation Rules

### Pizza

* `name` is required and must be unique
* `ingredients` is required

### RestaurantPizza

* `price` must be between 1 and 30 (inclusive)
* `pizza_id` and `restaurant_id` must reference valid models

##  Testing with Thunder Client or Postman

* Make sure the server is running
* Use `http://127.0.0.1:5000` as the URL for your CRUD operations

---

##  Example GET Response

### GET /restaurants/1

```json
{
  "id": 1,
  "name": "Mama's Pizza",
  "address": " Ngong Lane St",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Tomato, Mozzarella, Basil"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Tomato, Cheese, Pepperoni"
    }
  ]
}
```

---

## Error Response Example

### POST /restaurant\_pizzas with invalid price

```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

---

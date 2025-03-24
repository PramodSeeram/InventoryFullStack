
# Inventory Management System

This project provides a basic inventory management system using FastAPI and SQLAlchemy for database operations. It allows users to create, read, update, and delete inventory items.

## Features

- **Create Inventory Items**: Users can add new items to the inventory with details such as name, description, quantity, and price.
- **Read Inventory Items**: Users can view all items in the inventory or retrieve specific items by ID.
- **Update Inventory Items**: Users can modify existing items in the inventory.
- **Delete Inventory Items**: Users can remove items from the inventory.

## Requirements

- **Python**: The project is built using Python.
- **FastAPI**: Used for creating the API endpoints.
- **SQLAlchemy**: Used for database operations.
- **Pydantic**: Used for model validation.
- **sqlite3**: Default database engine, but can be configured to use other databases via environment variables.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/inventory-management-system.git
   ```

2. **Install Dependencies**:
   Navigate into the project directory and install required packages:
   ```bash
   cd inventory-management-system
   pip install -r requirements.txt
   ```

3. **Configure Database**:
   - By default, the project uses SQLite. For other databases, set the `DATABASE_URL` environment variable.
   - Create a `.env` file in the root directory and add:
     ```bash
     DATABASE_URL="sqlite:///./inventory.db"
     ```
   - For PostgreSQL or other databases, adjust the `DATABASE_URL` accordingly.

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Create Item
- **Endpoint**: `/inventory/additems`
- **Method**: `POST`
- **Request Body**: JSON object with `name`, `description`, `quantity`, and `price`.
- **Example**:
  ```json
  {
    "name": "Example Item",
    "description": "This is an example item.",
    "quantity": 10,
    "price": 9.99
  }
  ```

### Read All Items
- **Endpoint**: `/inventory/`
- **Method**: `GET`

### Read Item by ID
- **Endpoint**: `/inventory/{item_id}`
- **Method**: `GET`

### Update Item
- **Endpoint**: `/inventory/{item_id}`
- **Method**: `PUT`
- **Request Body**: JSON object with updated `name`, `description`, `quantity`, and `price`.

### Delete Item
- **Endpoint**: `/inventory/{item_id}`
- **Method**: `DELETE`

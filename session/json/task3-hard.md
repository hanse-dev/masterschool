# Task: Advanced JSON-based Inventory Management System

Create a Python program that manages a multi-store inventory system using JSON files. The program should handle complex operations, error checking, and data validation.

Create three JSON files:

``` json
stores.json:
{
  "stores": [
    {"id": 1, "name": "Downtown Store", "location": "123 Main St"},
    {"id": 2, "name": "Suburban Store", "location": "456 Oak Ave"},
    {"id": 3, "name": "Online Store", "location": "www.example.com"}
  ]
}
```
``` json
products.json:
{
  "products": [
    {"id": 101, "name": "Laptop", "category": "Electronics", "price": 999.99},
    {"id": 102, "name": "Desk Chair", "category": "Furniture", "price": 199.99},
    {"id": 103, "name": "Coffee Maker", "category": "Appliances", "price": 49.99}
  ]
}
```
``` json
inventory.json:
{
  "inventory": [
    {"store_id": 1, "product_id": 101, "quantity": 15},
    {"store_id": 1, "product_id": 102, "quantity": 10},
    {"store_id": 2, "product_id": 101, "quantity": 20},
    {"store_id": 2, "product_id": 103, "quantity": 5},
    {"store_id": 3, "product_id": 101, "quantity": 50},
    {"store_id": 3, "product_id": 102, "quantity": 25},
    {"store_id": 3, "product_id": 103, "quantity": 30}
  ]
}
```

## Implement the following functions:

1. `load_data(file_path)`: Reads a JSON file and returns the data. Handle file not found and JSON decoding errors.

2. `save_data(data, file_path)`: Writes data to a JSON file. Include error handling for file writing issues.

3. `get_store_inventory(store_id, stores, products, inventory)`: Returns a detailed inventory list for a specific store, including product names and prices.

4. `update_inventory(store_id, product_id, quantity_change, inventory)`: Updates the inventory for a specific product in a store. Ensure quantities don’t go below 0.

5. `add_new_product(product_data, products, inventory)`: Adds a new product to the system and initializes its inventory across all stores.

6. `generate_inventory_report()`: Creates a comprehensive report of all products in all stores, including total value of inventory per store.

7. `data_consistency_check(stores, products, inventory)`: Verifies that all store_ids and product_ids in the inventory match existing stores and products.

## In the main program:

1. Load all three JSON files.

2. Implement a command-line interface that allows users to:
   - View inventory for a specific store
   - Update inventory (add or remove items)
   - Add a new product
   - Generate an inventory report
   - Perform a data consistency check

3. After each operation that modifies data, save the updated data back to the respective JSON files.

4. Implement proper error handling and user input validation throughout the program.
 
## Advanced features to implement:

1. Use `json.dumps()` with indentation to create a “pretty print” function for displaying JSON data.

2. Implement a logging system that records all inventory changes in a separate JSON file.

3. Create a function to export the entire inventory system as a single JSON string, and another function to import and restore the system from this string.

4. Implement a simple caching mechanism to reduce file I/O operations, only writing changes to disk periodically or when explicitly requested.
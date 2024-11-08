# Task 2: JSON Data Merger

1. Create two JSON files:
``` json
employees.json:
{
  "employees": [
    {"id": 1, "name": "John Doe", "department": "HR"},
    {"id": 2, "name": "Jane Smith", "department": "IT"},
    {"id": 3, "name": "Mike Johnson", "department": "Finance"}
  ]
}
```

``` json
salaries.json:
{
  "salaries": [
    {"id": 1, "salary": 50000},
    {"id": 2, "salary": 60000},
    {"id": 3, "salary": 55000}
  ]
}
```
2. Write a function `read_json_file(file_path)` that uses `json.load()` to read a JSON file.

3. Write a function `merge_data(employees, salaries)` that combines the employee and salary data based on the employee ID.

4. Write a function `write_json_file(data, file_path)` that uses `json.dump()` to write data to a JSON file.

5. Write a function `data_to_json_string(data)` that uses `json.dumps()` to convert data to a JSON string.

6. In your main program: 
   1. Read both JSON files using `read_json_file()`. 
   2. Merge the data using `merge_data()`.
   3. Write the merged data to a new file called merged_data.json using `write_json_file()`. 
   4. Convert the merged data to a JSON string using `data_to_json_string()`. 
   5. Use `json.loads()` to parse the JSON string back into a Python object. 
   6. Print the parsed data to verify it matches the merged data.
# Task 1: JSON Config Manager

1. Create a configuration file named config.json with the following content:

``` json
{
  "app_name": "MyApp",
  "version": "1.0",
  "settings": {
    "dark_mode": false,
    "notifications": true,
    "language": "en"
  }
}
```

2. Write a function `read_config(file_path)` that uses `json.load()` to read the configuration file.
3. Write a function `update_config(config, key, value)` that updates a specific setting in the configuration.
4. Write a function `save_config(config, file_path)` that uses `json.dump()` to save the updated configuration back to the file.
5. Write a function `export_config_string(config)` that uses `json.dumps()` to convert the configuration to a JSON string.
6. In your main program: 
   1. Read the initial configuration using `read_config()`.
   2. Update the “dark_mode” setting to True using `update_config()`.
   3. Save the updated configuration using `save_config()`.
   4. Export the configuration to a JSON string using `export_config_string()` and print it.
   5. Use `json.loads()` to parse the JSON string back into a Python object and verify it matches the updated configuration.
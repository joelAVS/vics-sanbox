import os

folder_path = 'provinces'  # Replace with the actual folder path
prefixes_to_delete = ['owner =', 'controller']
ignored_cities = ['Lisbon', 'Rome', 'Vienna', 'London', 'Barcelona', 'Paris', 'Berlin', 'Lucerne' ]

for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.txt') and not any(city in file_name for city in ignored_cities):
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()

                with open(file_path, 'w') as file:
                    for line in lines:
                        if not any(line.startswith(prefix) for prefix in prefixes_to_delete):
                            file.write(line)

                print(f"Processed: {file_path}")
            except Exception as e:
                print(f"Error processing file: {file_path}. Error message: {str(e)}")

import json
import requests
temp_log = []

response = requests.get("https://google.com")
print(response.elapsed.total_seconds())
while True:
    try:
        with open('log.json', 'r') as file_object:  
            data = json.load(file_object)  
    except:
        with open('log.json', 'w') as file_object:  #open the file in write mode
            json.dump(temp_log, file_object)
        continue
    break

new_data = list(data)
print(new_data)

new_data.append(response.elapsed.total_seconds())
with open('log.json', 'w') as file_object:  #open the file in write mode
 json.dump(new_data, file_object)

 print(new_data)

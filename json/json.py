import json as js
js_dict = {"name" : "John", "age": 38, "is_student" : False, "hobbies" : ["reading", "playing games", "construction"]}
json_string = js.dumps(js_dict)    # преобразуем в JSON-строку
print(json_string)                       
data = js.loads(json_string)        # обратно в Python-объект       
print(data["name"])     

import json

data = '''{
            "name":"Shalini",
            "age":"27",
            "company":"planview",
            "address":{
                "mumbai":"andheri",
                "kerala":"tvm",
                "bangalore":"marthahalli"
                }
}'''

list_data= '''[
                 {
                    "name":"shalini",
                    "id":"1"
                 },
                 {
                    "name":"vibhor",
                    "id":"2"
                 }
]'''


info = json.loads(data)
print(info)
print("name:", info["name"])
print("address: ", info["address"]["bangalore"])


info_list = json.loads(list_data)
print(info_list)
for item in info_list:
    print(item['name'], item['id'])
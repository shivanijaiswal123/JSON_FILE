import json 
dic={"name":"shivani","age":21}
#dumps() function converts dictionary data to json string
dic=json.dumps(dic)
print(type(dic))
print(dic)

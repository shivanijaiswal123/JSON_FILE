import json 

#we have a dictionary here
dic={"name":"shivani","age":21}

# we have to convert dictionary to json string because we need json string for convert json string to dictionary

json_string=json.dumps(dic)

# loads() function for convert json string to dictionary
dic2=json.loads(json_string)

#here the type of data
print type(dic2)




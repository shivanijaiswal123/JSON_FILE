import json
with open('users.json') as data_file:    
    data = json.load(data_file)

users = data['users']

for user in users:
  
  print "users full name is " + user['firstName'] +' '+ user['lastName'] 
  print "users mobile number is " +str( user['details']['mobileNo'])
  print "users age  is " + str(user['details']['age'])
  print "users city is " + user['details']['City']+"\n"
  
  
 

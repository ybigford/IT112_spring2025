#import the JSON package in Python script. The text in JSON is done through quoted-string which contains the value in key-value mapping within { }
import json

data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York, NY',
    'interests': ['Golf', 'Running', 'Football', 'Traveling'],
    'is_student': False
     
}

#The with statement works with the open() function to open a file. So, we can re-write the code we used in the open() function
with open('data.json','w') as json_file:
    
    
    #json.dump converts the Python objects into appropriate json objects
    #create a json file (json_file). Then, dump the python object (data) in there. 
    #argument 1 (data) is the python object (dictionary) to be dumped
    #argument 2 (json_file) is the json file where the input (python object) to be stored (dumpt the python object into it)
    #argument 3 is the indent value of data in json file to improve readability 
    json.dump(data,json_file,indent=4)


print("You have successfully written to data.json")

    
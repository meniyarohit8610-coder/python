# create dictionary to store 20 different detail about your ownself 
detail = {
    "name": "rohit meniya",
    "age": 19,
    "gender": "Male",
    "dob": "03-08-2006",
    "email": "meniyarohit8610@email.com",
    "phone": "9876543210",
    "address": "vallbhipur, bhavnagar",
    "nationality": "Indian",
    "marital_status": "Single",
    "occupation": "Software Engineer",
    "company": "none",
    "education": "Bca",
    "hobbies": ["Reading", "Traveling", "playing cricket"],
    "favorite_food": "khichdi",
    "favorite_color": "black",
    "blood_group": "O+",
    "height_cm": 175,
    "weight_kg": 55.01,
}

#for print dictionary
print(detail)

#print name, age, gender, dob 
print(detail['name'])
print(detail['age'])
print(detail['gender'])
print(detail['dob'])

# add key value pair pincode into dictionary 
detail['pincode']=364310
#detail.update({"pincode":364310})
print(detail)

#add key value pair to store your 5 favourite touriest destination 
detail.update({"favorite-destination": ["Goa","Manali","Paris","Dubai","Bali"]})
print(detail)

#print all the favourite touriest destination 
print(detail['favorite-destination'])

#use update method to add new key value pair in dictionary
detail.update({"dream":"codding"})
print(detail)

#use update method to change existing key value pair in dictionary
detail.update({"pincode":364001})
print(detail)

#use pop method to remove dob 
detail.pop("dob")
print(detail)

#use popitem item method to remove last item 
detail.popitem()
print(detail)

#dsplay all keys
print(detail.keys())

#display all values
print(detail.values())

#copy dictionary into another dictionary using copy function
detail2=detail.copy()
print(detail2)

#clear newly created dictionary
detail2.clear()
print(detail,detail2)

print(":) :) good byyy :) :) ")
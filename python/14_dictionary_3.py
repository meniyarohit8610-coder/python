course = {'name':'spoken english','fees':9999.99,'days':120,'certified':True}
print(course)
#display key value pair as object
print(course.items())
#disply keys 
print(course.keys())
print(course.values())

students = ['name','age','gender','weight']
#create dictionary using elements of list 
rohit = dict.fromkeys(students) 
print(rohit)
rohit['name'] = 'rohit'
rohit['gender'] = True 
rohit['age'] = 19
rohit['weight'] = 55.11
print(rohit)

#remove key value pair
rohit.pop('weight')
print(rohit)
#remove last key value pair 
rohit.popitem()
print(rohit)
rohit['city'] = 'Bhavnagar' #it will add new key value pair 
rohit.update({'pincode':364001})
print(rohit)
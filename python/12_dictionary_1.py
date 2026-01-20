student = {'name':'rohit meniya','age':19,'weight':57.25,'gender':True,'degree':None}
print(student)
print(student['name']) #rohit meniya
student['age'] = 20 #key value pair update
print(student['age']) # 20
del student['degree'] #remove key value pair
student['city'] = 'gandhinagar' #it will add new key value pair 
print(student)
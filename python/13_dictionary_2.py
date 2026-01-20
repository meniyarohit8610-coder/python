course = {'name':'english','fees':0.01,'days':120,'certified':True}
print(course)
print(course['name']) #spoken english
course['name'] = 'sanscrit' #update
course['trainer'] = 'rohit sharma' #new key value pair add 
print(course)
print(course.get('location')) #error 
# course2 = course #bad way to copy dictionary
course2 = course.copy() 
course2.clear() #remove all key value pair 
print(course,course2)
print("Good bye")
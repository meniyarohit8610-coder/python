hydra={"name":"rohit","age":19,"stream":"bca","sem":5,"state":"gujrat","district":"bhavnagar","village":"vallbhipur"}

print(hydra)

#for add pincode 
hydra['pincode']=364310
print(hydra)

#for updte name
hydra.update({"name":'hydra'})
print(hydra)

print(hydra['name'])
print(hydra['age'])
print(hydra['sem'])

hydra.update({"age":20})
print(hydra)

hydra.popitem()
print(hydra)

hydra.pop('age')
print(hydra)
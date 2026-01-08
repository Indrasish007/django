import pickle
f=open("student.pkl",'rb')
data=pickle.load(f)
f.close()
print(data)
print('name : ',data['name'])
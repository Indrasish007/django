## file open and write
f=open("Hello.txt",'w')
f.write("hello python")
f.write("\nfile handling")
f.close()
 
# file data printing

f=open("Hello.txt",'r')
data=f.read()
print(data)
f.close()

#append

f=open('Hello.txt','a')
f.write("\nrohosso")
f.close()

#pickle # these files are used to store the python objects like list , tuple etc
import pickle

data=[10,20,30,40]
f=open('data.pkl','wb')
pickle.dump(data,f)
f.close()

#pickle read
import pickle
f=open('data.pkl','rb')
s=pickle.load(f)
f.close()
print(s)

#new pickle with dictionary
import pickle

student={
    'name':'john',
    'age':20,
    'marks':85
}
f=open('student.pkl','wb')
pickle.dump(student,f)
f.close()
print("details saved successfully")



#new pickle 
import pickle
f=open("student.pkl",'rb')
data=pickle.load(f)
f.close()
print(data)
print('name : ',data['name'])

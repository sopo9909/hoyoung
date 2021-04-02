<<<<<<< HEAD
import pickle
name = "tom"
age = 24
address = "서울시 마포구"
scores={"python":90,"deeplearning":95,"database":85}

with open("data2.pkl","wb")as file:
    pickle.dump(name,file)
    pickle.dump(age,file)
    pickle.dump(address,file)
    pickle.dump(scores,file)

import pickle
with open("data2.pkl","rb")as file:
    name2=pickle.load(file)
    age2=pickle.load(file)
    address2=pickle.load(file)
    scores2=pickle.load(file)
=======
import pickle
name = "tom"
age = 24
address = "서울시 마포구"
scores={"python":90,"deeplearning":95,"database":85}

with open("data2.pkl","wb")as file:
    pickle.dump(name,file)
    pickle.dump(age,file)
    pickle.dump(address,file)
    pickle.dump(scores,file)

import pickle
with open("data2.pkl","rb")as file:
    name2=pickle.load(file)
    age2=pickle.load(file)
    address2=pickle.load(file)
    scores2=pickle.load(file)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
    print(name2)
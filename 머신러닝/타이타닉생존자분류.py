import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def changeAge(n):
    if n < 10:
        return '유아'
    elif n < 20:
        return '10대'
    elif n < 30:
        return '20대'
    elif n < 40:
        return '30대'
    elif n < 50:
        return '40대'
    elif n < 60:
        return '50대'
    elif n < 70:
        return '60대'
    else:
        return '노인'
plt.rc('font',family='Malgun Gothic')
titanic = pd.read_csv('titanic_train.csv')
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].mean())
titanic['Age_Range'] = titanic['Age'].apply(changeAge)
result = titanic.groupby('Age_Range')['Survived'].sum()
result = result.reindex(['유아','10대','20대','30대','40대','50대','60대','노인'])
plt.subplot(121)
plt.bar(result.index,result.values,color='g')
plt.title("나이대별 타이타닉 생존자")
plt.xlabel("나이")
plt.ylabel("생존자")
plt.show()

plt.subplot(122)
result_survive = titanic.groupby('Sex')['Survived'].sum()
plt.bar(result_survive.index,result_survive.values,color='g')
plt.title("성별별 타이타닉 생존자")
plt.xlabel("성별")
plt.ylabel("생존자")
plt.show()
import pandas as pd
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
titan_data = pd.read_csv('titanic_train.csv',index_col='PassengerId',header=0,sep=',')
titan_data['Age_Range'] = titan_data['Age'].apply(changeAge)
tdata=titan_data.groupby('Age_Range')['Survived'].sum()
plt.rc('font',family='Malgun Gothic')
plt.bar(['10대','20대','30대','40대','50대','60대','유아','노인'],[tdata[i] for i in range(len(tdata))])
plt.title('나이대별 타이타닉 생존자')
plt.xlabel('나이')
plt.ylabel('생존자')
plt.show()

result = titan_data.groupby('Sex')['Survived'].sum()
print(result)
#titan_data.groupby('Sex')['Survived'].sum()
plt.bar([result.index],[result.values])
plt.title('나이대별 타이타닉 생존자')
plt.xlabel('나이')
plt.ylabel('생존자')
plt.show()
import pandas as pd
data = pd.read_csv('ChatbotData.csv',header=0)
#data2 = pd.read_csv('ChatBotData copy.csv',header=0)
data3 = pd.read_csv('text_sort.csv',header=0)
print(len(data))
idx_num =data[data['Q']=='너 뭐하는 애야'].index
data = data.drop(idx_num)
idx_num =data[data['Q']=='넌 누구냐?'].index
data = data.drop(idx_num)
idx_num =data[data['Q']=='누구냐 넌?'].index
data = data.drop(idx_num)
idx_num =data[data['Q']=='누구세요?'].index
data = data.drop(idx_num)
idx_num =data[data['Q']=='누구야'].index
data = data.drop(idx_num)
idx_num =data[data['Q']=='똑똑!'].index
data = data.drop(idx_num)
idx_num =data[data['Q']=='뭐하는 분이세요?'].index
data = data.drop(idx_num)
idx_num =data[data['Q']=='이름 알려줘'].index
data = data.drop(idx_num)
idx_num =data[data['Q']=='이름이 뭐야'].index
data = data.drop(idx_num)
idx_num =data[data['Q']=='너 뭐니?'].index
data = data.drop(idx_num)
idx_num =data[data['Q']=='너 누구?'].index
data = data.drop(idx_num)
idx_num =data[data['Q']=='너 누구냐'].index
data = data.drop(idx_num)
idx_num =data[data['Q']=='너 누구니?'].index
data = data.drop(idx_num)
print(len(data))
print(len(data3))
#data=data.append(data2)
data=data.append(data3)
print(len(data))
data.to_csv("total_data.csv", mode='w',index = False)
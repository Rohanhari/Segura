import pandas as pd


gyroscope=open('gyroscope.txt')



gyro_list=list(gyroscope.readlines())


lengths=[len(gyro_list)]

p=min(lengths)


gyro_list=gyro_list[lengths[0]-p:]



gyro_list=[i.split(',') for i in gyro_list]

gyro_y=[float(i[0]) for i in gyro_list]
print('What is the class that you want to classify(string)')
a=input()
print('What is the numerical representation for the same?')
b=int(input())
classify=[a for i in range(p)]
num_classify=[b for i in range(p)]

print('Name the file accordingly')
name=input()
df=pd.DataFrame({'classify':classify,'num_classify':num_classify,'gyro_y':gyro_y})
df.to_csv(name+'.csv',index=False)

import pandas as pd
accelerometer=open('accelerometer.txt','r')

gyroscope=open('gyroscope.txt')
magnetometer=open('magnetometer.txt')


acc_list=list(accelerometer.readlines())
gyro_list=list(gyroscope.readlines())
mag_list=list(magnetometer.readlines())

lengths=[len(acc_list),len(gyro_list),len(mag_list)]

p=min(lengths)

acc_list=acc_list[lengths[0]-p:]
gyro_list=gyro_list[lengths[1]-p:]
mag_list=mag_list[lengths[2]-p:]

acc_list=[i.split(',') for i in acc_list ]
gyro_list=[i.split(',') for i in gyro_list]
mag_list=[i.split(',') for i in mag_list]
acc_x=[float(i[0]) for i in acc_list]
acc_y=[float(i[1]) for i in acc_list]
acc_z=[float(i[2]) for i in acc_list]
gyro_x=[float(i[0]) for i in gyro_list]
gyro_y=[float(i[1]) for i in gyro_list]
gyro_z=[float(i[2]) for i in gyro_list]
mag_x=[float(i[0]) for i in mag_list]
mag_y=[float(i[1]) for i in mag_list]
mag_z=[float(i[2]) for i in mag_list]
print('What is the class that you want to classify(string)')
a=input()
print('What is the numerical representation for the same?')
b=int(input())
classify=[a for i in range(p)]
num_classify=[b for i in range(p)]

print('Name the file accordingly')
name=input()
df=pd.DataFrame({'classify':classify,'num_classify':num_classify,'acc_x':acc_x,'acc_y':acc_y,'acc_z':acc_z,'gyro_x':gyro_x,'gyro_y':gyro_y,'gyro_z':gyro_z,'mag_x':mag_x,'mag_y':mag_y,'mag_z':mag_z})
df.to_csv(name+'.csv',index=False)

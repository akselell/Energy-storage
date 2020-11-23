import numpy as np
import xlrd
import matplotlib.pyplot as plt

data = xlrd.open_workbook('./Cyprus_timeseries_data.xlsx').sheet_by_index(0)
#data = xlrd.open_workbook('./Aeroe_timeseries_data.xlsx').sheet_by_index(0)

X = np.empty((8760, 9))

#Add xlsx file to matrix X
for i in range(0, 9):
    X[:, i] = np.asarray(data.col_values(i, 1, 8761))


#file1 = open("degree_hour_cyprus.txt","w")#write mode 

heating = 0


for i in X[:,4]:
#    file1.write(f"{max(18-i,0)} \n") 
    heating += max(18-i,0)

print(heating)
#file1.close()

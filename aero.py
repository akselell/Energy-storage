import numpy as np
import xlrd
import matplotlib.pyplot as plt

data = xlrd.open_workbook('./Aeroe_timeseries_data.xlsx').sheet_by_index(0)

actual_consump = 166076400
#actual_consump = 31773160
#actual_consump = 167239.4

attributenames = data.row_values(0, 0, 9)

X = np.empty((8760, 9))

#Add xlsx file to matrix X
for i in range(0, 9):
    X[:, i] = np.asarray(data.col_values(i, 1, 8761))


initial_storage = 0
consump = np.sum(X[:,1])
#find total production
prod = X[:,2] + X[:,3]
#find how much we need to scale cunsumption timeseries
diff = actual_consump/consump
print(consump, diff)
#scale timeseries
consump =  diff * X[:,1]
#find how much we need to scale production
diff2 = actual_consump / np.sum(prod)
#scale production
goal_prodseries = prod * diff2
#make time series over storing potential
storing_potential = goal_prodseries - consump

storage = np.zeros((8760))
#sum storage potential to storage
for i in range(len(prod)):
    if i == 0:
        storage[i] = storing_potential[i]
    else:
        storage[i] = storage[i-1] + storing_potential[i]


minimum = min(storage)
print(abs(minimum))
storage += abs(minimum)
print(f"max storage: {round(max(storage), 1)}kWh")

print(f"Max storing: {round(max(storing_potential))}kW, Max output: {round(abs(min(storing_potential)))}kW")


plt.plot(X[:,0], storage)
plt.show()
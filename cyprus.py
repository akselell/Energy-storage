import numpy as np
import xlrd
import matplotlib.pyplot as plt

data = xlrd.open_workbook('./Cyprus_timeseries_data.xlsx').sheet_by_index(0)

actual_consump = 18390204990
#actual_consump = 31773160
#actual_consump = 167239.4

attributenames = data.row_values(0, 0, 9)

X = np.empty((8760, 9))

j = 0
#for i, col_id in enumerate(range(0, 9)):
#    X[:, i] = np.asarray(data.col_values(col_id, 1, 8761))
for i in range(0, 9):
    X[:, i] = np.asarray(data.col_values(i, 1, 8761))


initial_storage = 0
consump = np.sum(X[:,1])
prod = X[:,2] + X[:,3]
diff = actual_consump/consump
print(consump, diff)
consump =  diff * X[:,1]
diff2 = actual_consump / np.sum(prod)
goal_prodseries = prod * diff2

storing_potential = goal_prodseries - consump

storage = np.zeros((8760))

for i in range(len(prod)):
    if i == 0:
        storage[i] = storing_potential[i]
    else:
        storage[i] = storage[i-1] + storing_potential[i]


minimum = min(storage)
#print(minimum)
storage += abs(minimum)
print(f"max storage: {round(max(storage), 1)}kWh")

plt.plot(X[:,0], storage)
plt.show()

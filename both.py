import numpy as np
import xlrd
import matplotlib.pyplot as plt

datas = ['./Cyprus_timeseries_data.xlsx', './Aeroe_timeseries_data.xlsx']

Islands = ['Cyprus', 'Aeroe']
actual_consumps = [18390204990, 166076400] 
storage_needs = []
flott = []

#for x, actual_consump in datas, actual_consumps:
for x, actual_consump in zip(datas, actual_consumps):
    print(x, actual_consump)

    data = xlrd.open_workbook(x).sheet_by_index(0)

    attributenames = data.row_values(0, 0, 9)

    X = np.empty((8760, 9))

    #Add xlsx file to matrix X
    for i in range(0, 9):
        X[:, i] = np.asarray(data.col_values(i, 1, 8761))

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

    storage_needs.append(max(storage))

    flott.append(storing_potential)

    plt.plot(X[:,0], storage/1000)
    plt.title('Storage')
    plt.ylabel('MWh')
    plt.xlabel('Hour')
    plt.show()

start = 3850
stop = 4000

plt.plot(X[start:stop,0], goal_prodseries[start:stop]/1000)
plt.plot(X[start:stop,0], consump[start:stop]/1000)
#plt.legend(['goal_prodseries','consump','storing_potential'])
plt.legend(['Real_prodseries','Real_consumpseries'])
plt.ylabel('MW')
plt.xlabel('Hour')
#plt.show()
plt.plot(X[start:stop,0], storing_potential[start:stop]/1000)
plt.plot(X[start:stop,0], np.zeros((stop-start)))
plt.legend(['Storage_potential'])
plt.ylabel('MW')
plt.xlabel('Hour')
plt.show()
plt.plot(X[start:stop,0], storage[start:stop])
#plt.show()
#plt.legend(['storing_potential'])

print(diff2)
from both import *

#li-ion batery:

for x, place in zip(storage_needs, Islands):
    storage_cost = 156*x
    print(f"The price to fulfill {place}'s storage needs is: {int(storage_cost)}$")

for x in flott:
    plt.figure()
    plt.hist(x, bins=100)
    plt.show()
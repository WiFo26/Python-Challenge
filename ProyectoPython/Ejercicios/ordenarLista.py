entryList = input().split(" ")
orderList = input().split(" ")
outterList = [0] * len(entryList)
for i,j in zip(orderList, entryList):
    outterList[int(i)] = j
print(outterList)
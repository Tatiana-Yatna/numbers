inputList = [45, 54, 87, 82, 56, 39, 32, 67, 77, 61]

#resultList = []

'''Нужно написать программу, 
которая в resultList помещает 3 
максимальных значения из inputList и 
выводит получившийся resultList в консоль 
'''


inputList.sort(reverse=True)
i = 0
while i<3:
    i=i+1
    print(inputList[i])


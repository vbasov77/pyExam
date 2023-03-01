from Note import *
import os
os.system('cls')


def printAllData(data):
    if len(data) > 0:
        for object in data:
            print(object.printNote())
    else:
        print("Записи отсутствуют!")


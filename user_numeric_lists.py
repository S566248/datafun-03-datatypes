"""
Creator: Tyler Stanton

44-608, Fundamentals of Data Analytics
Project 3 - Task 3

"""

# import some standard modules first - how many can you make use of?
import math
import statistics


# TODO: import from local util_datafun_logger.py 

from util_datafun_logger import setup_logger

# TODO: Call the setup_logger function to create a logger and get the log file name

logger, logname = setup_logger(__file__)

# TODO: Create some shared data lists if you like - or just create them in your functions

list1 = [28, 36, 93, 53, 67, 23, 17, 42, 47, 6, 70, 81, 57, 24, 92, 10, 94, 32, 4, 25]
listx = list(range(10))
listy = [1, 5, 11, 15, 19, 26, 30, 36, 42, 45]

# TODO: define some custom functions
mean1 = statistics.mean(list1)
median1 = statistics.median(list1)
mode1 = statistics.mode(list1)

meanY = statistics.mean(listy)
medianY = statistics.median(listy)
modeY = statistics.mode(listy)

var1 = statistics.variance(list1)
stdev1 = statistics.stdev(list1)

varY = statistics.variance(listy)
stdevY = statistics.stdev(listy)

lowest1 = min(list1)
highest1 = max(list1)
lowestY = min(listy)
highestY = max(listy)

length1 = len(list1)
sum1 = sum(list1)
average1 = sum1 / length1
set1 = set(list1)
sort1 = sorted(list1)
sort1_T = sorted(list1, reverse = True)

lengthY = len(listy)
sumY = sum(listy)
averageY = sumY / lengthY
setY = set(listy)
sortY = sorted(listy)
sortY_T = sorted(listy, reverse = True)

lst = [1, 18, 7, 16, 2, 12, 4]

lst.append(1)
print(lst)
lst.extend([5, 2, 25])
print(lst)
lst.insert(6, 21) 
print(lst)
lst.remove(5)
print(lst)
print(lst.count(2))
lst.sort()
print(lst)
lst.sort(reverse = True)
print(lst)
copied_lst = lst.copy()
print(copied_lst)
lst.pop(0)
print(lst)
lst.pop()
print(lst)

def evens(x):
    return x % 2 == 0

even_lst = list(filter(evens, lst))
print(even_lst)

map_lst = list(map(lambda x: math.cbrt(x), lst))
print(map_lst)

def x_less_than_50():
    logger.info(f"{list1 = }")
    values_under_50 = list(filter(lambda x: x < 50, list1))
    logger.info(f"Values under 50: {values_under_50}")

def x_times_3():
    values_times_3 = list(map(lambda x: x * 3, list1))
    logger.info(f"list1 times 3 equals: {values_times_3}")

def x_squared():
    values_squared = list(map(lambda x: x * x, list1))
    logger.info(f"list1 squared equals: {values_squared}")

# -------------------------------------------------------------

if __name__ == "__main__":

    logger.info(f"mean of list1 = {mean1:.2f}")  
    logger.info(f"median of list1 = {median1:.2f}")
    logger.info(f"mode of list1 = {mode1:.2f}")

    logger.info(f"mean of listy = {meanY:.2f}")  
    logger.info(f"median of listy = {medianY:.2f}")
    logger.info(f"mode of listy = {modeY:.2f}")

    logger.info("var of list1 = " + str(var1))
    logger.info("stdev of list1 = " + str(stdev1))
    logger.info("lowest of list1 = " + str(lowest1))
    logger.info("highest of list1 = " + str(highest1))

    logger.info("var of listy = " + str(varY))
    logger.info("stdev of listy = " + str(stdevY))
    logger.info("lowest of listy = " + str(lowestY))
    logger.info("highest of listy = " + str(highestY))

    x_less_than_50()
    x_times_3()
    x_squared()
    

"""
print(lengthY)
print(sumY)
print(averageY)
print(setY)
print(sortY)
print(sortY_T)
"""



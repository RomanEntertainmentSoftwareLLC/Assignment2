# Jacob Roman
# 6343800
# 9/11/2022
# Net Centric Programming
# CNT4713 RVC 1228
# Assignment 2: Basic Python Programming

import math
import socket

class Assignment2:
    def __init__(self, year:int):
        self.year = year

    def tellAge(self, currentYear:int):
        result = currentYear - self.year
        print("Your age is " + str(result))

    def listAnniversaries(self):
        currentYear = 2022
        decadesApart = int(math.floor((currentYear - self.year) / 10))
        myList = []

        for x in range(decadesApart):
            myList.append((x + 1) * 10)
        return myList

    def modifyYear(self, n:int):
        strYear = str(self.year)
        first2 = strYear[:2]
        repeats = ""

        for x in range(n):
            repeats += first2

        oddRepMultiplier = str(self.year * n)
        oddChar = ""
        for index in range(len(oddRepMultiplier)):
            if (index % 2 == 0): # even numbers only to get odd characters...weird
                oddChar += oddRepMultiplier[index]

        result = repeats + oddChar

        return result

    @staticmethod
    def checkGoodString(string:str):

        hasDigit = False

        for chr in string:
            if chr.isdigit():
                hasDigit = True
            else:
                hasDigit = False

        if(len(string) >= 9 and string[0].islower() and hasDigit):
            return True
        else:
            return False

    @staticmethod
    def connectTcp(host:str, port:int):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            print("Error: Failed to connect to socket! " .format(e))
            return False

        try:
            s.connect((host, port))
        except socket.error as e:
            print("Error: Failed to connect to host! " .format(e))
            return False

        return True

a = Assignment2(1981)
a.tellAge(2022)
print(str(a.listAnniversaries()))
print(a.modifyYear(5))
print(Assignment2.checkGoodString("abcdefgh1"))
if (Assignment2.connectTcp("www.google.com", 80)):
    print("Connection established correctly")
else:
    print("Some error")

#Author : Rahul Gaikwad
#Date : 12/11/2015
#File : F.py
from m import M

class F(M):
    def __init__(self, mediaCn, mediaTi, mediaSu, di, yr, mediaNts):
        super(F, self).__init__(mediaCn, mediaTi, mediaSu, mediaNts)
        self.director = di
        self.year = yr
    
    def display(self):
        print("-------------------Type : F--------------------")
        super(F, self).display()
        print("director : " + self.director)
        print("year     : " + self.year)
        print("--------------------------------------------------")
    
    def compare_other(self, searchString):
        if(super(F, self).compare_other(searchString)):
            return True
        if (self.director.find(searchString) != -1):
            return True
        elif(self.year.find(searchString) != -1):
            return True

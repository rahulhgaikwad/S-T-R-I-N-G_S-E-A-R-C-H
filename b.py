#Author : Rahul Gaikwad
#Date : 12/11/2015
#File : B.py
from m import M

class B(M):
    def __init__(self, mediaCn, mediaTi, mediaSu, au, ds, pb, ct, yr, sr, mediaNts):
        super(B, self).__init__(mediaCn, mediaTi, mediaSu, mediaNts)
        self.author = au
        self.description = ds
        self.publication = pb
        self.city = ct
        self.year = yr
        self.series = sr
    
    def display(self):
        print("-------------------Type : B--------------------")
        super(B, self).display()
        print("author       : " + self.author)
        print("description  : " + self.description)
        print("publication  : " + self.publication)
        print("city         : " + self.city)
        print("year         : " + self.year)
        print("series       : " + self.series)
        print("--------------------------------------------------")
    
    def compare_other(self, searchString):
        if(super(B, self).compare_other(searchString)):
            return True
        if (self.description.find(searchString) != -1):
            return True
        elif(self.year.find(searchString) != -1):
            return True;

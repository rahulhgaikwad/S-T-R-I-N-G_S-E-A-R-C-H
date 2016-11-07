#Author : Rahul Gaikwad
#Date : 12/11/2015
#File : V.py
from m import M

class V(M):
    def __init__(self, mediaCn, mediaTi, mediaSu, ds,
                 dst, mediaNts, sr, lb):
        super(V, self).__init__(mediaCn, mediaTi, mediaSu, mediaNts)
        self.description = ds
        self.distributor = dst
        self.series = sr
        self.label = lb
    
    def display(self):
        print("----------------Type : Periodic-------------------")
        super(V, self).display()
        print("description  : " + self.description)
        print("distributor  : " + self.distributor)
        print("series       : " + self.series)
        print("label        : " + self.label)
        print("--------------------------------------------------")
    
    def compare_other(self, searchString):
        if(super(V, self).compare_other(searchString)):
            return True
        if (self.description.find(searchString) != -1):
            return True
        elif(self.distributor.find(searchString) != -1):
            return True

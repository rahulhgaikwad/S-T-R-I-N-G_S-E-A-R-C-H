#Author : Rahul Gaikwad
#Date : 12/11/2015
#File : P.py
from m import M

class P(M):
    def __init__(self, mediaCn, mediaTi, mediaSu, au, ds,
                 pb, pbh, sr, mediaNts,
                 relti, othfrmti, gvdno):
        super(P, self).__init__(mediaCn, mediaTi, mediaSu, mediaNts)
        self.author = au
        self.description = ds
        self.publication = pb
        self.publicationHistory = pbh
        self.series = sr
        self.relatedTitles = relti
        self.otherFormsOfTitle = othfrmti
        self.govtDocNumber = gvdno
    
    def display(self):
        print("----------------Type : P-------------------")
        super(P, self).display()
        print("author               : " + self.author)
        print("description          : " + self.description)
        print("publisher            : " + self.publication)
        print("publishing History   : " + self.publicationHistory)
        print("series               : " + self.series)
        print("related Titles       : " + self.relatedTitles)
        print("other Forms of Title : " + self.otherFormsOfTitle)
        print("govt Doc Number      : " + self.govtDocNumber)
        print("--------------------------------------------------")
    
    def compare_other(self, searchString):
        if(super(P, self).compare_other(searchString)):
            return True
        if (self.description.find(searchString) != -1):
            return True
        elif(self.series.find(searchString) != -1):
            return True
        elif(self.relatedTitles.find(searchString) != -1):
            return True


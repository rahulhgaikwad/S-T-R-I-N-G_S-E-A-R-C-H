#Author : Rahul Gaikwad
#Date : 12/11/2015
#File : M.py
class M(object):
    def __init__(self, mediaCn, mediaTi, mediaSu, mediaNts):
        self.call_number = mediaCn
        self.title = mediaTi
        self.subject = mediaSu
        self.notes = mediaNts
    
    def display(self):
        print("call_number  : " + self.call_number)
        print("title        : " + self.title)
        print("subject      : " + self.subject)
        print("notes        : " + self.notes)
    
    def compare_title(self, searchString):
        if(self.title.find(searchString) != -1):
            return True
    
    def compare_call_number(self, searchString):
       if(self.call_number.find(searchString) != -1):
           return True

    def compare_subject(self, searchString):
        if(self.subject.find(searchString) != -1):
            return True

    def compare_other(self, searchString):
        if(self.notes.find(searchString) != -1):
            return True

#Author : Rahul Gaikwad
#Date : 12/11/2015
#File : SE.py
from b import B
from f import F
from v import V
from p import P

class SE:
    listMedia = []
    
    def __init__(self):

        flBook = open("b.txt",'r')
        for line in flBook:
            bk = line.split('|')
            call_number = bk[0]
            title = bk[1]
            subject = bk[2]
            author = bk[3]
            description = bk[4]
            publication = bk[5]
            city = bk[6]
            year = bk[7]
            series = bk[8]
            notes = bk[9]
            self.listMedia.append(B(call_number, title, subject, author,
                                       description, publication,
                                       city, year, series, notes))
        flBook.close()
        
        flFilm = open("f.txt",'r')
        for line in flFilm:
            fm = line.split('|')
            call_number = fm[0]
            title = fm[1]
            subject = fm[2]
            director = fm[3]
            notes = fm[4]
            year = fm[5]
            self.listMedia.append(F(call_number, title, subject,
                                       director, notes, year))
        flFilm.close()

        flVideo = open("v.txt",'r')
        for line in flVideo:
            vd = line.split('|')
            call_number = vd[0]
            title = vd[1]
            subject = vd[2]
            description = vd[3]
            distributor = vd[4]
            notes = vd[5]
            series = vd[6]
            label = vd[7]
            self.listMedia.append(V(call_number, title, subject,
                                        description, distributor, notes,
                                        series, label))
        flVideo.close()

        flPeriodic = open("p.txt",'r')
        for line in flPeriodic:
            pd = line.split('|')
            call_number = pd[0]
            title = pd[1]
            subject = pd[2]
            author = pd[3]
            description = pd[4]
            publisher = pd[5]
            publishingHistory = pd[6]
            series = pd[7]
            notes = pd[8]
            relatedTitles = pd[9]
            otherFormsOfTitle = pd[10]
            govtDocNumber = pd[11]
            self.listMedia.append(P(call_number, title, subject, author,
                                           description, publisher,
                                           publishingHistory, series, notes,
                                           relatedTitles, otherFormsOfTitle,
                                           govtDocNumber))
        flPeriodic.close()

    def search_by_call_number(self, searchString):
        results = []
        for medium in self.listMedia:
            if medium.compare_call_number(searchString):
                results.append(medium)

        if results:
            return results
        else:
            print ("String Not Found!!!")

    def search_by_title(self, searchString):
        results = []
        for medium in self.listMedia:
            if medium.compare_title(searchString):
                results.append(medium)

        if results:
            return results
        else:
            print ("String Not Found!!!")

    def search_by_subject(self, searchString):
        results = []
        for medium in self.listMedia:
            if medium.compare_subject(searchString):
                results.append(medium)

        if results:
            return results
        else:
            print ("String Not Found!!!")

    def search_by_other(self, searchString):
        results = []
        for medium in self.listMedia:
            if medium.compare_other(searchString):
                results.append(medium)
    
        if results:
            return results
        else:
            print ("String Not Found!!!")

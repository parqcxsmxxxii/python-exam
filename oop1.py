class Student:
    sec = 11 # Class attribute/class member
    def __init__(self,name1,rollnum1):
        self.name = name1
        self.rollnum = rollnum1
    
    def displayStudent(self):
        print("Secion is ", self.sec)
    
    def marks(self,p,c,m):
        self.phy = p
        self.chem = c
        self.math = m

    def percent(self):
        marks = self.phy +self.chem+self.math
        percent = marks/100
        print("Youy percentage is ", self.percent)

dunu = Student("dunu baccha",12)
stuti = Student("stuti",10)


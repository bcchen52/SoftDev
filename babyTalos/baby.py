class Student():
    def __init__(self,name,id):
        self.name = name
        self.id = id

    schedule = {}


    rankings = {'AP':[],'math':[],'english':[],'history':[],'gym':[],'science':[],}
    subject_info = {'math':[{}],'english':[{}],'history':[{}],'science':[{}],}
    # {subject:[<subject avg>,{'<taken course>':<avg>, '<taken course>':<avg>}]}

class Class():
    def _init(self,name,id):
        self.name = name
        self.id = id

    sections = [[]]

    def create(rm,pd):
        sections += [rm,pd]


    

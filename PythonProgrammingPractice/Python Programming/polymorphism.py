class school:
    def __init__(self):
        self.name = "River Heights Intermediate"
        self.studentcount = 968
    
    def classroom(self):
        print(self.name, self.studentcount)
    

class teacher(school):
    def __init__(self):
        self.teacherscount = 43
        self.name = "Foothills"
        self.studentcount = 547
    
    def classroom(self):
        print(self.teacherscount)
        print(self.name, self.studentcount)



class parent(school):
    def __init__(self):
        self.name = "Parent"
    
    def classroom(self):
        print(self.name, self.studentcount)


class principal(school, parent):
    obj = parent()
    obj.classroom()



# obj = school()
# obj.classroom()

# obj2 = teacher()
# obj2.classroom()     # Guess is that it prints teacherscount (43) on one line, and then name (Foothills) and studentcount (547) on second line

obj3 = principal()
obj3.classroom()
# Parent 547
# 547
# River Heights Intermediate 547
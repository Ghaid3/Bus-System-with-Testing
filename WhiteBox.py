
"""
COMP4402/ Spring 23/ Project/Part4/Dynamic Testing
Ruaa Alrashdi - ID:129245
Ghaidaa Alrawahi - ID: 131760
Submitted to: prof. Yocef Baghdadi 

-- Whit Box Testing --

"""
import dataBaseService as db
import unittest

#%%
# bus Sys Classes
class Supervisor:
    def enter(self, ID_entry):
        if self.verifyID(ID_entry): 
            #self.statement.config(text="Student entered the bus at " + strftime('%H:%M:%S %p'),fg="green")
            db.updateStudent(ID_entry,1)
            return True
        return False
    
    def Exit(self,ID_entry):
        if self.verifyID():
            #self.statement.config(text="Student exit the bus at " +strftime('%H:%M:%S %p') ,fg='green')
            db.updateStudent(ID_entry,0)
            return True
        else:
            return False
    
    def verifyID(self,s_id):
        students = db.getAllStudents()
        for student in students:
            if student[0]==s_id:
                return True
        return False

class Parent:
    def check(self,s_id):
        students = db.getAllStudents()
        for student in students:
            if student[0]==s_id and student[3]==1:
                #self.state.config(text="Yes {} is in the bus".format(student[1]),fg="green")
                return True
        #self.state.config(text="No, student with ID: {} not in the bus.".format(s_id),fg='red')
        return False

#%%
#Test Class
class TestEnter(unittest.TestCase):
    
    def test_Case1(self):
        supervisor1 = Supervisor()
        flag = supervisor1.enter(4)
        self.assertTrue(flag, "")
        
    def test_Case2(self):
        supervisor1 = Supervisor()
        flag = supervisor1.Exit(11)
        self.assertTrue(flag, "")
        
    def test_Case3(self):
        Parent1 = Parent()
        flag = Parent1.check(4)
        self.assertTrue(flag, "")
    
    def test_Case4(self):
        Parent1 = Parent()
        flag = Parent1.check(11)
        self.assertFalse(flag, "")
    
    def test_Case5(self):
        Parent1 = Parent()
        flag = Parent1.check(22)
        self.assertFalse(flag, "")
    
    def test_Case6(self):
        Parent1 = Parent()
        flag = Parent1.check(15)
        self.assertFalse(flag, "")
    
    def test_Case7(self):
        Parent1 = Parent()
        flag = Parent1.check(1)
        self.assertFalse(flag, "")
    
        
if __name__ == '__main__':
    
    unittest.main()
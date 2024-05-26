# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 15:41:36 2022

@author: ruaa
"""

import tkinter as tk
from time import strftime
from tkinter import *
import dataBaseService as db
import unittest
from datetime import datetime


class Supervisor:
    def supervisor_main_screen(self):

        self.supervisor_screen = tk.Toplevel(main_screen)
        self.supervisor_screen.geometry("500x400")
        self.supervisor_screen.title("Student Screen")
        self.supervisor_screen.configure(bg="#c5e0db")
        self.timeLabel = tk.Label(self.supervisor_screen,font = ('Times New Roman', 40, 'bold'),background = '#5e7a78')
        self.statement = tk.Label(self.supervisor_screen, text="",bg="#c5e0db")
        self.timeLabel.pack()
        self.clock()
        tk.Label(self.supervisor_screen,text="Please enter the student id: ", width="300", height="2", font=("Calibri", 20),bg="#c5e0db").pack() 
        self.ID_entry = tk.Entry(self.supervisor_screen,bg='#EBE4E4')
        self.ID_entry.pack()
        tk.Label(self.supervisor_screen,text="",bg="#c5e0db").pack() 
        tk.Button(self.supervisor_screen,text="Enter", height="2", width="30" ,bg='#5e7a78', command=self.attend).pack() 
        tk.Label(self.supervisor_screen,text="",bg="#c5e0db").pack() 
        tk.Button(self.supervisor_screen,text="Exit", height="2", width="30" ,bg='#5e7a78', command=self.leave).pack()
        tk.Label(self.supervisor_screen,text="",bg="#c5e0db").pack()
        self.statement.pack()
        tk.Label(self.supervisor_screen,text="",bg="#c5e0db").pack() 
        tk.Button(self.supervisor_screen,text="Exit", height="2", width="20" ,bg='#5e7a78', command=self.SupExit).pack(side= "top", anchor="w") 
        self.supervisor_screen.mainloop()
    def clock(self):
        string = strftime('%H:%M:%S %p')
        self.timeLabel.config(text = string)
        self.timeLabel.after(1000,self.clock)
    def attend(self):
        if self.verifyID(): 
            self.statement.config(text="Student entered the bus at " + strftime('%H:%M:%S %p'),fg="green")
            self.db.updateStudent(int(self.ID_entry.get()),1)
           
    def leave(self):
        if self.verifyID():
            self.statement.config(text="Student exit the bus at " +strftime('%H:%M:%S %p') ,fg='green')
            db.updateStudent(int(self.ID_entry.get()),0)
            
    def verifyID(self):
        students = db.getAllStudents()
        s_id=int(self.ID_entry.get())
        for student in students:
 
            if student[0]==s_id:
                return True
        self.statement.config(text="There is no student with {} ID.".format(s_id) ,fg='black')
        return False
                
  
    def SupExit(self):
        self.supervisor_screen.destroy()    
        
        
class Parent:
    
    def countStudents(self):
        count = 0
        students = db.countStudentsInBus()
        for u in students:
            count += 1
        return count
      
    
    def parentScreen(self):
        self.parent_screen = tk.Toplevel(main_screen)
        self.parent_screen.geometry("500x400")
        self.parent_screen.title("Parent Screen")
        self.parent_screen.configure(bg="#c5e0db")
        tk.Label(self.parent_screen,text="Please enter your son/daughter id: ", width="300", height="2", font=("Calibri", 20),bg="#c5e0db").pack() 
        self.student_id = tk.Entry(self.parent_screen,bg='#EBE4E4')
        self.student_id.pack()
        tk.Label(self.parent_screen,text="",bg="#c5e0db").pack() 
        tk.Button(self.parent_screen,text="Check if my son/daughter inside the Bus", height="2", width="40" ,bg='#5e7a78', command=self.check).pack()  
        tk.Label(self.parent_screen,text="",bg="#c5e0db").pack()  
        self.state = tk.Label(self.parent_screen,text="",bg="#c5e0db")
        self.state.pack()
        
        studentsNum = self.countStudents()
        tk.Label(self.parent_screen,text="The number of students in the Bus is: {}".format(studentsNum),bg="#c5e0db", fg="black").pack()
        
        self.parent_screen.mainloop()
        
    def check(self):
        students = db.getAllStudents()
        for student in students:
            s_id=int(self.student_id.get())
            if student[0]==s_id and student[3]==1:
                self.state.config(text="Yes {} is in the bus".format(student[1]),fg="green")
                return 
        self.state.config(text="No, student with ID: {} not in the bus.".format(s_id),fg='red')
        

class TestAttend(unittest.TestCase):
    
    def setUp(self):
        self.db = Database()
        self.student1 = Student(1, "ruaa", "saleh")
        self.db.addStudent(self.student1)
    
    def tearDown(self):
        self.db.deleteAllStudents()
    
    def test_valid_student_id_exists_in_db(self):
        # Test with a valid student ID that exists in the database
        self.assertTrue(self.db.attend(1))
        self.assertEqual(self.db.statement.cget("text"), "Student entered the bus")
        self.assertEqual(self.db.statement.cget("fg"), "green")
    
    def test_valid_student_id_does_not_exist_in_db(self):
        # Test with a valid student ID that does not exist in the database
        self.assertFalse(self.db.attend(2))
        self.assertEqual(self.db.statement.cget("text"), "There is no student with 2 ID.")
        self.assertEqual(self.db.statement.cget("fg"), "black")
    
    def test_invalid_input(self):
        # Test with an empty string
        self.assertFalse(self.db.attend(""))
        self.assertEqual(self.db.statement.cget("text"), "Invalid input")
        self.assertEqual(self.db.statement.cget("fg"), "black")
        # Test with a non-integer string
        self.assertFalse(self.db.attend("abc"))
        self.assertEqual(self.db.statement.cget("text"), "Invalid input")
        self.assertEqual(self.db.statement.cget("fg"), "black")
        # Test with a negative integer value
        self.assertFalse(self.db.attend(-1))
        self.assertEqual(self.db.statement.cget("text"), "Invalid input")
        self.assertEqual(self.db.statement.cget("fg"), "black")
    
if __name__ == '__main__':
    unittest.main()

class TestVerifyID(unittest.TestCase):
    
    def setUp(self):
        self.db = Database()
        self.student1 = Student(1292, "ruaa", 93981595 , 1)
        self.student2 = Student(1301, "ghaida", 99999888 , 1)
        self.db.createStudent(self.student1)
        self.db.createStudent(self.student2)
    
    
    def test_valid_student_id(self):
        # Test with a valid student ID
        self.assertTrue(self.db.verifyID(1))
    
    def test_invalid_student_id(self):
        # Test with an invalid student ID
        self.assertFalse(self.db.verifyID(2))
    
    def test_invalid_input(self):
        # Test with an empty string
        self.assertFalse(self.db.verifyID(""))
        # Test with a non-integer string
        self.assertFalse(self.db.verifyID("abc"))
        # Test with a negative integer value
        self.assertFalse(self.db.verifyID(-1))
    
if __name__ == '__main__':
    unittest.main()

class TestClock(unittest.TestCase):
    
    def setUp(self):
        self.clock = Clock()
    
    def test_minimum_time_value(self):
        # Set the current time to before midnight
        self.clock.timeLabel.config(text="00:00:00 AM")
        self.clock.clock()
        # Verify that the timeLabel text is set to the minimum time value
        self.assertRegex(self.clock.timeLabel.cget("text"), "^00:00:00 AM$")
    
    def test_maximum_time_value(self):
        # Set the current time to after midnight
        self.clock.timeLabel.config(text="11:59:59 PM")
        self.clock.clock()
        # Verify that the timeLabel text is set to the maximum time value
        self.assertRegex(self.clock.timeLabel.cget("text"), "^11:59:59 PM$")
    
    def test_normal_time_value(self):
        # Set the current time to a normal time value
        self.clock.clock()
        # Verify that the timeLabel text is set to a valid time string
        self.assertRegex(self.clock.timeLabel.cget("text"), "^\d{2}:\d{2}:\d{2} (AM|PM)$")
    
if __name__ == '__main__':
    unittest.main()


class TestBus(unittest.TestCase):
    
    def setUp(self):
        self.bus = Bus()
        self.bus.ID_entry.insert(0, "12345")
    
    def test_leave_valid_id(self):
        expected_statement = "Student exit the bus at " + datetime.now().strftime('%H:%M:%S %p')
        self.bus.leave()
        self.assertEqual(self.bus.statement.cget("text"), expected_statement)
        self.assertEqual(self.bus.statement.cget("fg"), "green")
        self.assertEqual(db.getStudent(12345)[1], 0)
    
    def test_leave_invalid_id(self):
        self.bus.ID_entry.delete(0, END)
        self.bus.ID_entry.insert(0, "111")
        with self.assertRaises(ValueError):
            self.bus.leave()
    
    def test_leave_invalid_id_from_invalid_state(self):
        self.bus.ID_entry.delete(0, END)
        self.bus.ID_entry.insert(0, "404")
        with self.assertRaises(ValueError):
            self.bus.leave()
    
    def test_leave_invalid_id_from_valid_state(self):
        self.bus.ID_entry.delete(0, END)
        self.bus.ID_entry.insert(0, "404")
        with self.assertRaises(ValueError):
            self.bus.leave()

if __name__ == '__main__':
    unittest.main()

                
        
class Main:
    
    def main(self):
        global main_screen
        main_screen = tk.Tk()
        main_screen.state("zoomed")

        try:
            tk.PhotoImage(file='bus.png')
          
        except:
            pass
        main_screen.geometry("800x600") 
        main_screen.configure(bg="#c5e0db") 
        main_screen.title("Bus system")
        tk.Label(text="Bus system", width="300", height="2",bg='#c5e0db', font=("Times New Roman", 30)).pack() 
        tk.Label(text="",bg="#c5e0db").pack() 
        tk.Label(text="",bg='#c5e0db').pack() 
        tk.Button(text="I'm Parent", height="2", width="30" ,bg='#5e7a78', command=self.parentScreen).pack() 
        tk.Label(text="",bg='#c5e0db').pack() 
        tk.Button(text="I'm bus supervisor", height="2", width="30" ,bg='#5e7a78', command=self.supervisorScreen).pack()
        main_screen.mainloop()
   
        
    def supervisorScreen(self):
        supervisor = Supervisor()
        supervisor.supervisor_main_screen()
    
    def parentScreen(self):
        parent = Parent()
        parent.parentScreen()
            
manager = Main()
manager.main()

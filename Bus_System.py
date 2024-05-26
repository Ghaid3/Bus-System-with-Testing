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
        tk.Button(self.supervisor_screen,text="Enter", height="2", width="30" ,bg='#5e7a78', command=self.enter).pack() 
        tk.Label(self.supervisor_screen,text="",bg="#c5e0db").pack() 
        tk.Button(self.supervisor_screen,text="Exit", height="2", width="30" ,bg='#5e7a78', command=self.Exit).pack()
        tk.Label(self.supervisor_screen,text="",bg="#c5e0db").pack()
        self.statement.pack()
        tk.Label(self.supervisor_screen,text="",bg="#c5e0db").pack() 
        tk.Button(self.supervisor_screen,text="Exit", height="2", width="20" ,bg='#5e7a78', command=self.SupExit).pack(side= "top", anchor="w") 
        self.supervisor_screen.mainloop()
    def clock(self):
        string = strftime('%H:%M:%S %p')
        self.timeLabel.config(text = string)
        self.timeLabel.after(1000,self.clock)
    def enter(self):
        if self.verifyID(): 
            self.statement.config(text="Student entered the bus at " + strftime('%H:%M:%S %p'),fg="green")
            db.updateStudent(int(self.ID_entry.get()),1)
            return True
        return False
           
    def Exit(self):
        if self.verifyID():
            self.statement.config(text="Student exit the bus at " +strftime('%H:%M:%S %p') ,fg='green')
            db.updateStudent(int(self.ID_entry.get()),0)
            return True
        else:
            return False

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
        s_id=int(self.student_id.get())
        for student in students:
            if student[0]==s_id and student[3]==1:
                self.state.config(text="Yes {} is in the bus".format(student[1]),fg="green")
                return True 
        self.state.config(text="No, student with ID: {} not in the bus.".format(s_id),fg='red')
        return False
        
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
unittest.main()
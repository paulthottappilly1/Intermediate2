# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

class Student:
    # constructor for Student
    def __init__(s, name, gpa):
        s.name = name
        s.gpa = gpa
    # returns a string with the name and GPA
    def report_gpa(s):
        return(s.name + " has a GPA of " + str(s.gpa))
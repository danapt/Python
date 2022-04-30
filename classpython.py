# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:41:01 2021

@author: daniel.apetri
"""

class Dog:
    
    species = "test familiarie"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self,sound):
        return f"{self.name} says {sound}"
    
    
a =  Dog("test",1)
print (a.name)
print(a.age)    
print(a.species)

print(a)
print(a.speak("caca maca"))    
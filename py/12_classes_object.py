
#Classes
#Basic class defination 
class Person: 
    #Class attribute (shared by all instances)
    species = "Homo sapiens"

    #Constructor method 
    def__init__(self, name, age):
        #Instance attributes
        self.name = name 
        self.age = age 

    #Instance method
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    #Methos with parameters
    def have_birthday(self)
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age}."
    
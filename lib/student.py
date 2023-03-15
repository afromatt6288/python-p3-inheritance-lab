#!/usr/bin/env python

from user import User

knowledge = []
new_information = "New information"

class Student(User):
    def __init__(self, first_name, last_name,):        
        super().__init__(first_name, last_name)
        self.knowledge = knowledge
    
    def learn(self, new_informaton):
        self.new_information = new_information
        self.knowledge.append(self.new_information)
        pass
# Create a class called Student
class Student:
    
    # Initialise student
    def __init__(self, input_name, input_cohort):
        self.name = input_name
        self.cohort = input_cohort


    # Define talk function
    def talk(self):
        return "I can talk!"


    # Define favourite languate
    def say_favourite_language(self, language):
        return "I love " + language
        # return f"I love {language}"

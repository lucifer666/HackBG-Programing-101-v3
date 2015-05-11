import re

class EmailError(Exception):
    pass

class Panda:

    def __init__(self, name, email, gender):
        self.__name = name
        self.__email = email
        self.__gender = gender

    def name(self):
        return self.__name

    def gender(self):
        return self.__gender

    def email(self):
        return self.__email

    def is_valid_email(self):
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if not email_regex.match(self.__email):
              raise EmailError

    def isMale(self):
        if self.__gender == "male":
            return True
        elif self.__gender == "female":
            return False

    def isFemale(self):
       if self.__gender == "female":
            return True
       elif self.__gender == "male":
            return False

    def __eq__(self, other_panda):
        equal_names = self.__name == other_panda.__name
        equal_emails = self.__email == other_panda.__email
        equal_gender = self.__gender == other_panda.__gender
        return equal_names and equal_emails and equal_gender

    def __str__(self):
        result = "I am {}. My email is {}. My gender is {}."
        return result.format(self.__name, self.__email, self.__gender)

    def __hash__(self):
        return hash(self.__name + self.__email + self.__gender)









PROJECT TITLE: 0x00. AirBnB clone - The console

What is the AirBnB clone? - Well... Here's what we know, the AirBnB is website for vacation bookings accross the world. Therefore we were tasked to create a clone of such a website. Where one is able to book a specific logding place of choice. 
So this project looks at both the front-end and back-end of a project. 
Here's a quick run-through
1. The console
Here, we created our base model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)

2. Files and Directories
In this case:
- models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- tests directory will contain all unit tests.
console.py file is the entry point of our command interpreter.
- models/base_model.py file is the base class of all our models. It contains common elements:
    - attributes: id, created_at and updated_at
    - methods: save() and to_json()
- models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.
 For example: 
 class Student():
    def __init__(self, name):
        self.name = name

students = reload() # recreate the list of Student objects from a file
s = Student("John")
students.append(s)
save(students) # save all Student objects to a file

3. File storage == JSON serialization
For this first step, you have to write in a file all your objects/instances created/updated in your command interpreter and restore them when you start it. You can’t store and restore a Python instance of a class as “Bytes”, the only way is to convert it to a serializable data structure:

   - convert an instance to Python built in serializable data structure (list, dict, number and string) - for us it will be the method my_instance.to_json() to retrieve a dictionary
   - convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us it will be a my_string = JSON.dumps(my_dict)
   - write this string to a file on disk

   4. datetime
   datetime is a Python module to manipulate date, time etc…
   Example: 
   a_dict = { 'my_date': date_now }
print(type(a_dict['my_date'])) # <class 'datetime.datetime'>
print(a_dict) # {'my_date': datetime.datetime(2017, 6, 8, 20, 42, 42, 170922)}

When all this has been done and properly implemented, then we are able to use the website.

Thank You! 



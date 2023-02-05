**THE AirBnB Clone**
**01 - Creating the Console Support for Line-Oriented Command Interpreter AirBnB Clone**

**The Console for the AirBnB Clone**

The AirBnB Clone project allows you to manage and replicate your own bookings and listings on AirBnB.
The purpose of this project is to provide practice with Python and 
demonstrate how to use an Object-Relational Mapping (ORM) system to handle data.

**Getting Started**

To get started with the AirBnB Clone project, follow these steps:

Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/YOUR_USERNAME/AirBnB_clone.git
Navigate to the project's root directory:
bash
Copy code
cd AirBnB_clone
Launch the console by entering the following command on your terminal:
javascript
Copy code
./console.py
Writing a Command Interpreter
Writing a command interpreter is a crucial first step in managing your AirBnB objects. This will allow you to use the things you create for this project in all subsequent projects, such as the database store, API, front-end in HTML/CSS, etc.

Using the Console
The AirBnB data model may be accessed using the console. The following fundamental commands are available:

create <class name> - creates a new instance of the specified class and saves it to the JSON file
sql
Copy code
create User
show <class name> <object id> - displays the string representation of the specified object
sql
Copy code
show User 1
all <class name> - displays all instances of the specified class, or all objects if no class name is provided
sql
Copy code
all User
destroy <class name> <object id> - deletes the specified object
sql
Copy code
destroy User 1
update <class name> <object id> <attribute name> "<attribute value>" - updates the specified object with the new attribute value
sql
Copy code
update User 1 name "John Doe"
Built With
Python - The programming language used
JSON - Data serialization format

**Recognized Classes**

Class Name	Description

Basemodel	The base model class, provides common attributes and methods for all other classes
User	Represents a user, who can create bookings and listings on the platform
State	Represents a state, where places are located
Amenity	Represents an amenity, that a place can offer
Review	Represents a review, written by a user about a place
Place	Represents a place, that can be booked on the platform
City	Represents a city, where places are located

**Example Code for Recognized Classes**

# Define the Basemodel class
class Basemodel:
    def __init__(self, id, created_at, updated_at):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

# Define the User class
class User(Basemodel):
    def __init__(self



**AUTHORS.**
Nwalahnjie Anye <akumawahanye@gmail.com>
Shema Fred <fredshema24@gmail.com>



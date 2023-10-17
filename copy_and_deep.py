"""
Task 5: Use shallow copy and deep copy.
Imagine you have a list of students, where each student is represented as a dictionary.
 You want to duplicate the list of students, but you don't need to create new dictionaries for each student;
  you only want to copy references to the same student dictionaries.
Imagine you have a nested configuration object for a software application,
and you want to create a duplicate configuration for testing purposes.
You want to ensure that changes to the test configuration don't affect the production configuration.

"""

import copy

# Original list of students
students = [
    {"name": "abc", "age": 20},
    {"name": "xyz", "age": 22},
    {"name": "klm", "age": 21}
]

# Create a shallow copy of the list
shallow_copy_students = copy.copy(students)

# Modify the copied list
shallow_copy_students[0]["name"] = "yasodha"
#print(id(shallow_copy_students),id(students),id(shallow_copy_students[0]["name"]),id(students[0]["name"]))

# Verify that changes affect the original list as well
print(students[0]["name"])  # Output: Alicia

print(shallow_copy_students)
print(students)


import copy

# Original configuration object
original_config = {
    "app_name": "MyApp",
    "database": {
        "host": "localhost",
        "port": 3306
    }
}

# Create a deep copy of the configuration
deep_copy_config = copy.deepcopy(original_config)

# Modify the copied configuration
deep_copy_config["database"]["host"] = "testdb.example.com"

# Verify that changes to the copied config do not affect the original config
print(original_config["database"]["host"])  # Output: localhost
print(deep_copy_config)
print(original_config)

l=[12,[1,2,3],[4,5]]

#l1=copy.copy(l)
l1=copy.deepcopy(l)
l1[1][2]=4
print("--",id(l1[1]))
print("--",id(l[1]))

print("----",id(l1[0]))
print("----",id(l[0]))
print(l1)
print(l)
#print(l)




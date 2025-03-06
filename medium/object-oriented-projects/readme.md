# School Catalogue

This exercise is part of the Codecademy Python Course: Learn Intermediate Python 3 - Object-Oriented Programming. The goal is to create a digital school catalog for the New York City Department of Education. The catalog will hold quick reference material for each school in the city.

## Classes

We need to create classes for primary and high schools. These classes will inherit from a parent `School` class. The parent and child classes have the following properties, getters, setters, and methods:

### School

- **Properties**:
  - `name` (string)
  - `level` (one of three strings: 'primary', 'middle', or 'high')
  - `numberOfStudents` (integer)
- **Getters**:
  - All properties have getters
- **Setters**:
  - The `numberOfStudents` property has a setter
- **Methods**:
  - `__repr__` method that displays information about the school

### Primary

- **Includes**:
  - Everything in the `School` class
- **Additional Property**:
  - `pickupPolicy` (string, like "Pickup after 3pm")

### Middle

- **Includes**:
  - Everything in the `School` class
- **Additional Properties or Methods**:
  - None

### High

- **Includes**:
  - Everything in the `School` class
- **Additional Property**:
  - `sportsTeams` (list of strings, like ['basketball', 'tennis'])

## Example Usage

```python
# Creating instances of each school type
a = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(a)

b = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(b)

c = MiddleSchool("Codecademy", 300)
print(c)
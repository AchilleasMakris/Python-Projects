# Base class for all types of schools
class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  # Getter for the name property
  def get_name(self):
    return self.name

  # Getter for the level property
  def get_level(self):
    return self.level
  
  #Getter for the numberOfStudents property
  def get_numberOfStudents(self):
    return self.numberOfStudents

  # Setter for the numberOfStudents property
  def set_numberOfStudents(self, numberOfStudents):
    self.numberOfStudents = numberOfStudents

  # String representation of the School object
  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "Primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + ". The pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)


class MiddleSchool(School):
  def __init__(self, name, numberOfStudents):
    super().__init__(name, "Middle", numberOfStudents)


class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "High", numberOfStudents)
    self.sportsTeams = sportsTeams

  def get_sportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    parent_repr = super().__repr__()
    return f"{parent_repr}. The sports teams are: {', '.join(self.sportsTeams)}."


a = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(a)

b = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(b)

c = MiddleSchool("Codecademy", 300)
print(c)

from fireo.models import Model
from fireo.fields import TextField, NumberField

class Person(Model):
    name = TextField()
    age = NumberField()

# Create a new person
new_person = Person(name="John Doe", age=30)
new_person.save()

# Query persons older than 25
query_result = Person.collection.filter("age", ">", 25).fetch()

# Update a person's age
person_to_update = query_result[0]
person_to_update.age = 31
person_to_update.update()

# Delete a person
person_to_delete = query_result[1]
person_to_delete.delete()


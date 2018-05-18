class Cat():
    def __init__(self, breed, age):
        """Initialization method to auto-populate an instance"""

        self.breed = breed
        self.age = age

    def cat_age(self):
        """Get the cat's age"""

        return self.age

    def breed(self):
        """Get the type of cat, e.g. short hair, long hair, etc."""
        
        return self.breed

    def __repr__(self):
            """Return string representation of Cat object.

            Without this method, only the object's memory address will be printed.
            """
            return "{breed}, {age}".format(breed = self.breed, age = self.age)

@classmethod # This is required
    def type(cls):
        """
        Class method, available only to classes.

        Notice that 'cls' is the argument, as opposed to 'self'
        """

        if cls.__name__ == "Cat":
            return "Some sort of domestic cat."
        else:
            return cls.__name__

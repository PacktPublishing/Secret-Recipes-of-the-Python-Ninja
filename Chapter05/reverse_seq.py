class Reverse_Seq:
    """Iterator to loop backwards through a sequence."""
    def __init__(self, data_in):
        self.data = data_in
        self.index = len(data_in)  # Go to last element
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:  # No more elements
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]  # Return element at index

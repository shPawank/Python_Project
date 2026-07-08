#Magic/Dunder Methods in Python 

class employees:
    name="Pawan"
    def __len__(self):
        i=0
        for c in  self.name:
            i=i+1
        return i


    # def __str__(self):
    #     return f"Employee name is {self.name}"

    def __repr__(self):
            return f"Employee name is ('{self.name}') repr"

    def __call__(self):
        return f"Employee name is {self.name} call"


e=employees()
print(e)  # Output: Employee name is Pawan
print(repr(e))  # Output: Employee name is Pawan
print(callable(e))  # Output: True
# print(e.name)  # Output: Pawan
# print(len(e))
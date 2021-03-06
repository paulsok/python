class Vector:
    def __init__(self, *args):
        self.values = []
        [self.values.append(i) for i in args if type(i) is int]

    def __str__(self):
        if not self.values:
            return "Пустой вектор"
        return f"Вектор{tuple(sorted(self.values))}"


v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"

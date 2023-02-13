class Ponto:
    def __init__(self, x: int, y: int, z: str):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Para desenvolvedores saberem como remontar o seu objeto
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'

p1 = Ponto(1, 2, 'uma string')
p2 = Ponto(978, 876, 'Outra String')

print(p1)
# como chamar o __repr__ após ter definido o __str__
print(repr(p2))
# ou
print(f'{p2!r}')
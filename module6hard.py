import math

class Figure:
    def __init__(self, color, *sides):
        self.sides_count = 0
        self._sides = [1] * self.sides_count  # Изначально стороны — это список из единиц
        self.__color = list(color)  # RGB цвета должны быть списком
        self.filled = False

        if self.__is_valid_sides(*sides):
            self._sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)  # Периметр фигуры

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):

    def __init__(self, color, *sides):
        self.sides_count = 1
        super().__init__(color, *sides)

        if len(sides) == 0:
            self._sides = [1]
        elif len(sides) == 1:
            self._sides = [sides[0]]
        else:
            self._sides = [1]  # Если передано больше сторон, устанавливаем по умолчанию

        self.__radius = self._sides[0] / (2 * math.pi)  # Рассчитываем радиус

    def get_square(self):
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):

    def __init__(self, color, *sides):
        self.sides_count = 3
        super().__init__(color, *sides)

        if len(sides) < 3:
            self._sides = [1] * 3  # По умолчанию 1, 1, 1
        elif len(sides) == 3:
            self._sides = list(sides)
        else:
            self._sides = [1] * 3  # Если передано больше сторон

    def get_square(self):
        a, b, c = self._sides
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 12
        super().__init__(color, *sides)

        if len(sides) == 0:
            self._sides = [1] * 12
        elif len(sides) == 1:
            self._sides = [sides[0]] * 12
        else:
            self._sides = [1] * 12  # Если передано больше сторон

    def get_volume(self):
        side = self._sides[0]
        return side ** 3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
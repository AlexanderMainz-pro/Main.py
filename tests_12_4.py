import unittest
import logging


logging.basicConfig(
    level=logging.INFO,
    mode='w',
    filename='runner_tests.log',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)

class Runner:
    def __init__(self, name, speed=5):  # Исправлено "init" на "__init__"
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("TestRunner", -10)
        except ValueError:
            logging.warning("Неверная скорость для Runner")
        else:
            runner.walk()
            self.assertEqual(runner.distance, 10)
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(123, 10)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
        else:
            runner.run()
            self.assertEqual(runner.distance, 20)
            logging.info('"test_run" выполнен успешно')


if __name__ == '__main__':
    unittest.main()
import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
                    break
        return finishers

def frozen_test(f):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print('Тесты в этом кейсе заморожены')
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return f(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @frozen_test
    def test_run(self):
        runner = Runner("TestRunner", 10)
        runner.run()
        self.assertEqual(runner.distance, 20)

    @frozen_test
    def test_walk(self):
        runner = Runner("TestRunner", 10)
        runner.walk()
        self.assertEqual(runner.distance, 10)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @frozen_test
    def test_first_tournament(self):
        runner1 = Runner("Усэйн", speed=10)
        runner2 = Runner("Андрей", speed=9)
        tournament = Tournament(20, runner1, runner2)
        results = tournament.start()
        self.assertEqual(len(results), 2)

    @frozen_test
    def test_second_tournament(self):
        runner = Runner("Усэйн", speed=10)
        tournament = Tournament(20, runner)
        results = tournament.start()
        self.assertEqual(len(results), 1)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
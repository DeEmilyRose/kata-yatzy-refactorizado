class Yatzy:

    FIFTY = 50
    ZERO = 0

    @staticmethod
    def chance(*dice):
        return sum(dice)

    @staticmethod
    def yatzy(*dice):
        list_of_numbers = []

        for die in dice:
            if die not in list_of_numbers:
                list_of_numbers.append(die)
        if len(list_of_numbers) != 1:
            return Yatzy.ZERO
        else:
            return Yatzy.FIFTY

    @staticmethod
    def ones(*dice):
        list_of_ones = []

        for die in dice:
            if die == 1:
                list_of_ones.append(die)
        return sum(list_of_ones)

    @staticmethod
    def twos(*dice):
        list_of_twos = []

        for die in dice:
            if die == 2:
                list_of_twos.append(die)
        return sum(list_of_twos)

    @staticmethod
    def threes(*dice):
        list_of_threes = []

        for die in dice:
            if die == 3:
                list_of_threes.append(die)
        return sum(list_of_threes)

    def __init__(self, d1=0, d2=0, d3=0, d4=0, _5=0):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    def fours(*dice):
        list_of_fours = []

        for die in dice:
            if die == 4:
                list_of_fours.append(die)
        return sum(list_of_fours)

    def fives(*dice):
        list_of_fives = []

        for die in dice:
            if die == 5:
                list_of_fives.append(die)
        return sum(list_of_fives)

    def sixes(*dice):
        list_of_sixes = []

        for die in dice:
            if die == 6:
                list_of_sixes.append(die)
        return sum(list_of_sixes)

    def score_pair(*dice):
        for die in range(6, 0, -1):
            if dice.count(die) >= 2:
                return die * 2
        return 0

    @staticmethod
    def two_pair(*dice):
        list_two_pair = []

        for die in range(6, 0, -1):
            if dice.count(die) >= 2:
                list_two_pair.append(die)
            if len(list_two_pair) == 2:
                return sum(list_two_pair) * 2
        return 0

    @staticmethod
    def four_of_a_kind(*dice):
        for die in range(6, 0, -1):
            if dice.count(die) >= 4:
                return die * 4
        return 0

    @staticmethod
    def three_of_a_kind(*dice):
        for die in range(6, 0, -1):
            if dice.count(die) >= 3:
                return die * 3
        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
class Yatzy:

    FIFTY = 50
    ZERO = 0

    def __init__(self, *dice):
        self.dice = (dice)
       
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
    
    @staticmethod
    def fours(*dice):
        list_of_fours = []

        for die in dice:
            if die == 4:
                list_of_fours.append(die)
        return sum(list_of_fours)
    
    @staticmethod
    def fives(*dice):
        list_of_fives = []

        for die in dice:
            if die == 5:
                list_of_fives.append(die)
        return sum(list_of_fives)
    
    @staticmethod
    def sixes(*dice):
        list_of_sixes = []

        for die in dice:
            if die == 6:
                list_of_sixes.append(die)
        return sum(list_of_sixes)

    @staticmethod
    def score_pair(*dice):
        for die in range(6, 0, -1):
            if dice.count(die) >= 2:
                return die * 2
        return Yatzy.ZERO

    @staticmethod
    def two_pair(*dice):
        list_two_pair = []

        for die in range(6, 0, -1):
            if dice.count(die) >= 2:
                list_two_pair.append(die)
            if len(list_two_pair) == 2:
                return sum(list_two_pair) * 2
        return Yatzy.ZERO

    @staticmethod
    def three_of_a_kind(*dice):
        for die in range(6, 0, -1):
            if dice.count(die) >= 3:
                return die * 3
        return Yatzy.ZERO
    
    @staticmethod
    def four_of_a_kind(*dice):
        for die in range(6, 0, -1):
            if dice.count(die) >= 4:
                return die * 4
        return Yatzy.ZERO

    @staticmethod
    def smallStraight(*dice):
        dice_set_small = set(dice)

        if dice_set_small == {1, 2, 3, 4, 5}:
            return 15
        return Yatzy.ZERO

    @staticmethod
    def largeStraight(*dice):
        dice_set_larges = set(dice)

        if dice_set_larges == {2, 3, 4, 5, 6}:
            return 20
        return Yatzy.ZERO

    @staticmethod
    def fullHouse(*dice):
        if Yatzy.score_pair(*dice) and Yatzy.three_of_a_kind(*dice):
            return Yatzy.score_pair(*dice) + Yatzy.three_of_a_kind(*dice)
        else:
            return Yatzy.ZERO

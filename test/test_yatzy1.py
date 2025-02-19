from src.yatzy1 import Yatzy
import pytest

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


@pytest.mark.chance
def test_chance():
    assert 15 == Yatzy.chance(2, 3, 4, 5, 1)
    assert 15 == Yatzy.chance(2, 3, 4, 5, 1)
    assert 16 == Yatzy.chance(3, 3, 4, 5, 1)
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)


@pytest.mark.yatzy
def test_yatzy():
    assert 50 == Yatzy.yatzy(4, 4, 4, 4, 4)
    assert 50 == Yatzy.yatzy(6, 6, 6, 6, 6)
    assert 0 == Yatzy.yatzy(6, 6, 6, 6, 3)
    assert 50 == Yatzy.yatzy(1, 1, 1, 1, 1)
    assert 0 == Yatzy.yatzy(1, 1, 1, 2, 1)


@pytest.mark.ones
def test_ones():
    assert 1 == Yatzy.ones(1, 2, 3, 4, 5)
    assert 2 == Yatzy.ones(1, 2, 1, 4, 5)
    assert 0 == Yatzy.ones(6, 2, 2, 4, 5)
    assert 4 == Yatzy.ones(1, 2, 1, 1, 1)
    assert 0 == Yatzy.ones(3, 3, 3, 4, 5)
    assert 5 == Yatzy.ones(1, 1, 1, 1, 1)


@pytest.mark.twos
def test_twos():
    assert 4 == Yatzy.twos(1, 2, 3, 2, 6)
    assert 10 == Yatzy.twos(2, 2, 2, 2, 2)
    assert 0 == Yatzy.twos(3, 3, 3, 4, 5)
    assert 4 == Yatzy.twos(2, 3, 2, 5, 1)


@pytest.mark.threes
def test_threes():
    assert 6 == Yatzy.threes(1, 2, 3, 2, 3)
    assert 12 == Yatzy.threes(2, 3, 3, 3, 3)
    assert 0 == Yatzy.threes(1, 1, 1, 1, 1)
    assert 9 == Yatzy.threes(3, 3, 3, 4, 5)


@pytest.mark.fours
def test_fours():
    assert 8 == Yatzy.fours(4, 5, 6, 4, 5)
    assert 12 == Yatzy.fours(4, 4, 4, 5, 5)
    assert 8 == Yatzy.fours(4, 4, 5, 5, 5)
    assert 4 == Yatzy.fours(4, 5, 5, 5, 5)


@pytest.mark.fives
def test_fives():
    assert 10 == Yatzy.fives(4, 5, 6, 4, 5)
    assert 10 == Yatzy.fives(4, 4, 4, 5, 5)
    assert 15 == Yatzy.fives(4, 4, 5, 5, 5)
    assert 20 == Yatzy.fives(4, 5, 5, 5, 5)


@pytest.mark.sixes
def test_sixes():
    assert 6 == Yatzy.sixes(4, 5, 6, 4, 5)
    assert 0 == Yatzy.sixes(4, 4, 4, 5, 5)
    assert 6 == Yatzy.sixes(4, 4, 6, 5, 5)
    assert 18 == Yatzy.sixes(6, 5, 6, 6, 5)


@pytest.mark.one_pair
def test_one_pair():
    assert 8 == Yatzy.score_pair(3, 3, 3, 4, 4)
    assert 12 == Yatzy.score_pair(1, 1, 6, 2, 6)
    assert 6 == Yatzy.score_pair(3, 3, 3, 4, 1)
    assert 6 == Yatzy.score_pair(3, 3, 3, 3, 1)
    assert 0 == Yatzy.score_pair(1, 2, 3, 4, 5)
    assert 6 == Yatzy.score_pair(3, 4, 3, 5, 6)
    assert 10 == Yatzy.score_pair(5, 3, 3, 3, 5)
    assert 12 == Yatzy.score_pair(5, 3, 6, 6, 5)


@pytest.mark.two_pairs
def test_two_Pair():
    assert 8 == Yatzy.two_pair(1, 1, 2, 3, 3)
    assert 0 == Yatzy.two_pair(1, 1, 2, 3, 4)
    assert 6 == Yatzy.two_pair(1, 1, 2, 2, 2)
    assert 0 == Yatzy.two_pair(1, 2, 3, 4, 5)
    assert 0 == Yatzy.two_pair(4, 4, 4, 4, 5)
    assert 16 == Yatzy.two_pair(3, 3, 5, 4, 5)
    assert 18 == Yatzy.two_pair(3, 3, 6, 6, 6)
    assert 0 == Yatzy.two_pair(3, 3, 6, 5, 4)


@pytest.mark.three_of_a_kind
def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 0 == Yatzy.three_of_a_kind(3, 3, 4, 5, 6)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 1)
    assert 0 == Yatzy.three_of_a_kind(1, 2, 3, 4, 5)
    assert 15 == Yatzy.three_of_a_kind(5, 3, 5, 4, 5)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 5)


@pytest.mark.four_of_a_kind
def test_four_of_a_knd():
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 5)
    assert 0 == Yatzy.four_of_a_kind(2, 2, 2, 5, 5)
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 2)
    assert 0 == Yatzy.four_of_a_kind(1, 2, 3, 4, 5)
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 5)
    assert 20 == Yatzy.four_of_a_kind(5, 5, 5, 4, 5)
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 3)
    assert 0 == Yatzy.four_of_a_kind(3, 3, 3, 2, 1)


@pytest.mark.smallstraight
def test_smallStraight():
    assert 0 == Yatzy.smallStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.smallStraight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.smallStraight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.smallStraight(1, 2, 3, 4, 6)
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.smallStraight(2, 3, 4, 5, 1)
    assert 0 == Yatzy.smallStraight(1, 2, 2, 4, 5)


@pytest.mark.largestraight
def test_largeStraight():
    assert 20 == Yatzy.largeStraight(6, 2, 3, 4, 5)
    assert 20 == Yatzy.largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 2, 4, 5)
    assert 0 == Yatzy.largeStraight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.largeStraight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.largeStraight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 3, 4, 6)


@pytest.mark.fullhouse
def test_fullHouse():
    assert 18 == Yatzy.fullHouse(6, 2, 2, 2, 6)
    assert 0 == Yatzy.fullHouse(2, 3, 4, 5, 6)
    assert 8 == Yatzy.fullHouse(1, 1, 2, 2, 2)
    assert 0 == Yatzy.fullHouse(2, 2, 3, 3, 4)
    assert 0 == Yatzy.fullHouse(4, 4, 4, 4, 4)
    assert 0 == Yatzy.fullHouse(4, 4, 4, 1, 2)

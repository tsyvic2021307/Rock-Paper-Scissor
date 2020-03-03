import pytest
import rps_modules
import getpass

# Weapons Testing
@pytest.mark.set1
def test_weapons1():
    assert rps.weaponChoice("Player")[1] == "------------------------------------------\r\nPlayer, please choose your weapon:\r\n1. Rock\r\n2. Paper\r\n3. Scissors\r\nEnter your choice (use the appropriate number): "

# Check Testing
#@pytest.mark.parametrize("in1, in2, out", [(2, 2, 0), (2, 1, 1), (1, 2, 2)])
def test_checkingExpected2(in1, in2, out):
    assert rps.checking(in1, in2) == out

def test_checkingUnexpected1():
    assert rps.checking(1, 5) == 3

# Congrats Testing
def test_congrats():
    assert rps.congrats("Player") == print("Player, you've won this round!")

# Winner Testing
def test_winner():
    assert rps.congrats("Player") == print("Congratulations Player, you won the game!!
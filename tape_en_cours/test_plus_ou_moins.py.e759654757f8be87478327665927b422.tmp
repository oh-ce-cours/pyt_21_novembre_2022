# pylint: disable=redefined-outer-name
import pytest
from plus_ou_moins import game_logic, game, random
import unittest.mock as mock


@pytest.fixture
def expected_value():
    return 50


def test_nombre_entre_plus_grand_qu_attendu(expected_value):
    input_value = 80
    result = game_logic(input_value, expected_value)
    to_print, continue_ = result

    assert to_print == "c'est moins"
    assert not continue_


def test_nombre_entre_plus_petit_qu_attendu(expected_value):
    input_value = 10
    result = game_logic(input_value, expected_value)
    to_print, continue_ = result

    assert to_print == "c'est plus"
    assert not continue_


def test_nombre_entre_egal_attendu(expected_value):
    input_value = 50
    result = game_logic(input_value, expected_value)
    to_print, continue_ = result

    assert to_print == "c'est bon"
    assert continue_


def test_game(monkeypatch, capfd):
    def random_42(*args, **kwargs):
        return 42

    responses = ["43", "41", "42"]
    expected = "".join(["c'est moins\n", "c'est plus\n", "c'est bon\n"])

    def fake_input(args):
        try:
            return responses.pop(0)
        except IndexError:
            return None

    monkeypatch.setattr(random, "randint", random_42)
    monkeypatch.setattr("builtins.input", fake_input)

    game()
    out, _ = capfd.readouterr()
    assert out == expected

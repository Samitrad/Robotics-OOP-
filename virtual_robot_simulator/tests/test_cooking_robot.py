import pytest
from src.robots.base_robot import Robot
from src.robots.cleaning_robot import CleaningRobot
def cooking_robot():
    return CookingRobot(name="ChefBot", batterylvl=100, skill="Baking")

def test_initialization(cooking_robot):
    assert cooking_robot.name == "ChefBot"
    assert cooking_robot.batterylvl == 100
    assert cooking_robot.skill == "Baking"

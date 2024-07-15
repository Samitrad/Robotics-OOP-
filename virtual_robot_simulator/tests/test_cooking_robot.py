import pytest
from src.robots.base_robot import Robot
from src.robots.cooking_robot import CookingRobot
def cooking_robot():
    return CookingRobot(name="ChefBot", batterylvl=100, skill="Baking")

def test_initialization(cooking_robot):
    assert cooking_robot.name == "ChefBot"
    assert cooking_robot.batterylvl == 100
    assert cooking_robot.skill == "Baking"

def test_work_with_sufficient_battery(cooking_robot):
    cooking_robot.work()
    assert cooking_robot.status == "Cooking"
    assert cooking_robot.batterylvl == 70  # Assuming work decreases battery by 30%

def test_work_with_low_battery(cooking_robot):
    cooking_robot.batterylvl = 10  # Set a low battery level
    cooking_robot.work()
    assert cooking_robot.status != "Cooking"  # Robot should not be cooking with low battery
    assert cooking_robot.batterylvl == 10  # Battery level should remain unchanged

def test_self_diagnose(cooking_robot):
    diagnosis = cooking_robot.self_diagnose()
    assert "Battery OK" in diagnosis  # Example assertion for battery status

def test_report_status(cooking_robot, capsys):
    cooking_robot.report_status()
    captured = capsys.readouterr()
    assert "ChefBot" in captured.out
    assert "Battery:" in captured.out
    assert "Status:" in captured.out

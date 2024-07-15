# tests/test_cleaning_robot.py
import pytest
from src.robots.base_robot import Robot
from src.robots.cleaning_robot import CleaningRobot

def cleaning_robot():
    return CleaningRobot(name="CleanerBot", batterylvl=100, tool="Vacuum")

def test_initialization(cleaning_robot):
    assert cleaning_robot.name == "CleanerBot"
    assert cleaning_robot.batterylvl == 100
    assert cleaning_robot.tool == "Vacuum"

def test_work_with_sufficient_battery(cleaning_robot):
    cleaning_robot.work()
    assert cleaning_robot.status == "Cleaning"
    assert cleaning_robot.batterylvl == 80  # Assuming work decreases battery by 20%

def test_work_with_low_battery(cleaning_robot):
    cleaning_robot.batterylvl = 10  # Set a low battery level
    cleaning_robot.work()
    assert cleaning_robot.status != "Cleaning"  # Robot should not be cleaning with low battery
    assert cleaning_robot.batterylvl == 10  # Battery level should remain unchanged

def test_self_diagnose(cleaning_robot):
    diagnosis = cleaning_robot.self_diagnose()
    assert "Battery OK" in diagnosis  # Example assertion for battery status

def test_report_status(cleaning_robot, capsys):
    cleaning_robot.report_status()
    captured = capsys.readouterr()
    assert "CleanerBot" in captured.out
    assert "Battery:" in captured.out
    assert "Status:" in captured.out

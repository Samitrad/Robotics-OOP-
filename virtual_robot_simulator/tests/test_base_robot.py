import pytest
from src.robots.base_robot import Robot

@pytest.fixture
def robot():
    return Robot(name="TestBot", batterylvl=100)

def test_initialization(robot):
    assert robot.name == "TestBot"
    assert robot.batterylvl == 100

def test_report_status(robot, capsys):
    robot.report_status()
    captured = capsys.readouterr()
    assert "TestBot" in captured.out
    assert "Battery: 100%" in captured.out
    assert "Status: idle" in captured.out

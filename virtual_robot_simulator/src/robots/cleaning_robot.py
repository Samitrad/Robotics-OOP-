from .base_robot import Robot

class CleaningRobot(Robot):
    def __init__(self, name: str, batterylvl: int, tool: str):
        """
        Initializes a CleaningRobot instance.

        Args:
            name (str): The name of the robot
            tool (str): The tool used for cleaning (e.g., vacuum, mop)
        """
        super().__init__(name, batterylvl)
        self.tool = tool

    def work(self):
        """
        Implements the cleaning behavior.

        Decreases the battery level by 20 for each cleaning session if the robot is charged
        """
        if self.batterylvl >= 20:
            self.batterylvl -= 20
            self.status="Cleaning"
        else:
            print("The robot needs to be recharged")
    def self_diagnose(self) -> str:
        """Perform self-diagnosis and report any issues specific to CleaningRobot"""
        issues = []
        issues.append(self.check_battery(self.batterylvl))
    
        return "\n".join(issues)
    

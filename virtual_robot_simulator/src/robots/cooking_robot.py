from .base_robot import Robot

class CookingRobot(Robot):
    def __init__(self, name: str, batterylvl: int, skill: str):
        """
        A robot designed for cooking tasks.

        Attributes:
            cooking_skill (str): The tool used for cooking
        """
        super().__init__(name, batterylvl)
        self.skill = skill

    def skill(self) -> str:
        return self._skill

    
    def skill(self, new_skill: str):
        self._skill = new_skill    

    def work(self):
        """
        Implements the cooking behavior.

        Decreases the battery level by 30 for each cooking session if the robot is charged
        """
        if self.batterylvl >= 30:
            self.batterylvl -= 30
            self.status="Cooking"
        else:
            print("The robot needs to be recharged")
    def self_diagnose(self) -> str:
        """Perform self-diagnosis and report any issues specific to CleaningRobot"""
        issues = []
        issues.append(self.check_battery(self.batterylvl))
        
        return "\n".join(issues)        

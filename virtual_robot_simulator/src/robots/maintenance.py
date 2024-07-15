from .cooking_robot import CookingRobot
from .cleaning_robot import CleaningRobot
from .base_robot import Robot
class MaintenanceRobot(CleaningRobot, CookingRobot):
    def __init__(self, name, batterylvl, tool, skill):
        
        Robot.__init__(self, name, batterylvl)  # Call Robot's __init__ method
        self.tool = tool
        self.skill = skill


    def multi_task(self):
        # Perform a cleaning task
        self.work() # Calls CleaningRobot's work method because it is the first one 
        self.report_status()

        # Perform a cooking task
        CookingRobot.work(self) # Calls CookingRobot's work method
        self.report_status()

    def work_cleaning(self):
        print(f"{self.name} is cleaning with {self.tool}.")

    def work_cooking(self):
        print(f"{self.name} is cooking with skill {self.skill}.")

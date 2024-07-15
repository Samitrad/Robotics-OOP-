from robots.cooking_robot import CookingRobot
from robots.cleaning_robot import CleaningRobot
from robots.maintenance import MaintenanceRobot

def main():
    cleaner = CleaningRobot(name="CleanBot", batterylvl=50, tool="vacuum")
    cooker = CookingRobot(name="CookBot", batterylvl=90, skill="expert")
    

    cleaner.work()
    cleaner.report_status()

    cooker.work()
    cooker.report_status()

    cleaner.work()
    cleaner.report_status()

    cooker.work()
    cooker.report_status()
    
    cleaner.work()
    cleaner.report_status()

    maintenance_robot = MaintenanceRobot("MaintBot", 80, "vaccum", "intermediate")
    maintenance_robot.multi_task()

    print(f"{cleaner.name},{cleaner.self_diagnose()}")
    print(f"{cooker.name},{cooker.self_diagnose()}")

if __name__ == "__main__":
    main()

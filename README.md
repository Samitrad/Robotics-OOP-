# Robotics-OOP-
1. MRO Definition: MRO defines the order in which Python searches base classes when a method is called in a class with multiple inheritance. It ensures consistent behavior and avoids conflicts.
2. MRO in MaintenanceRobot: MaintenanceRobot inherits from both CleaningRobot and CookingRobot. MRO dictates which parent class's method is found first when a method is called in MaintenanceRobot.
3. MRO Impact: MRO ensures:
    Priority is given to methods from the immediate superclass (either CleaningRobot or CookingRobot based on inheritance order).
    The super() function, used for calling parent class methods, respects the MRO to avoid issues.
4. Benefits of MRO: By understanding and applying MRO, the MaintenanceRobot achieves:
    Performing both cleaning and cooking tasks.
    Maintaining a consistent state and method hierarchy.

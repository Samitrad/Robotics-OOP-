# Robotics-OOP-
1. MRO Definition: MRO defines the order in which Python searches base classes when a method is called in a class with multiple inheritance. It ensures consistent behavior and avoids conflicts.
2. MRO in MaintenanceRobot: MaintenanceRobot inherits from both CleaningRobot and CookingRobot. MRO dictates which parent class's method is found first when a method is called in MaintenanceRobot.
3. MRO Impact: MRO ensures:
    Priority is given to methods from the immediate superclass (either CleaningRobot or CookingRobot based on inheritance order).
    The super() function, used for calling parent class methods, respects the MRO to avoid issues.
4. Benefits of MRO: By understanding and applying MRO, the MaintenanceRobot achieves:
    Performing both cleaning and cooking tasks.
    Maintaining a consistent state and method hierarchy.

Getters and Setters:
    Purpose: Getters and setters are used to encapsulate attributes within classes, providing controlled access to class attributes while protecting internal data integrity.
Class Methods:
    Purpose: Class methods are used to define methods that operate on the class itself rather than instances of the class. They can be used for utility functions that are related to the class but do not require access to instance-specific data.
Static Methods:
    Purpose: Static methods are similar to class methods but do not have access to class or instance data. They are primarily used for utility functions that are logically related to the class but do not modify class or instance state.
Abstract Base Classes (ABCs):
    Purpose: ABCs are used to define a blueprint for other classes, ensuring that they implement specific methods or properties. They enforce a contract that subclasses must follow to be considered valid implementations of the base class.

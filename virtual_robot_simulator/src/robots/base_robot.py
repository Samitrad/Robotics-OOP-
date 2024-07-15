class Robot:
    def __init__(self, name: str, batterylvl: int):
        self.name = name
        self.batterylvl = batterylvl
        self.status = "idle"

    def charge(self):
        self.batterylvl = 100
        self.status = "charged"

    def work(self):
        pass
    
    def check_battery(cls, batterylvl: int) -> str:
        """Class method to check battery level"""
        if batterylvl < 20:
            return "Low battery"
        else:
            return "Battery OK"
    def self_diagnose(self) -> str:
        """Abstract method to perform self-diagnosis"""
        pass
    

    def report_status(self):
        print(f"{self.name}, Battery: {self.batterylvl}%, Status: {self.status}")
        
  

"""
FEEDBACK
1. check line 34
2. You hardcoded values instead of leveraging on setters and getters
3. You have not done any data validation, your system falls apart if user supplies the wrong type of data
4. You have not done any error handling
5. Location points are given in pairs of longitude and latitude, your code has not taken that into consideration
"""
class Location:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance  # distance in miles


class Machine:
    def __init__(self, speed):
        self.speed = speed  # speed in miles per hour


class TravelSimulator:
    def __init__(self, machine, location_a, location_b):
        self.machine = machine
        self.location_a = location_a
        self.location_b = location_b

    def calculate_expected_time(self):
        return self.location_a.distance / self.machine.speed
    
    def get_actual_travel_time(self):
        # Simulate obtaining actual travel time from an external module
        # Replace this with actual implementation that fetches the time
        return 0  # Placeholder value for demonstration

    def check_obstructions(self):
        expected_time = self.calculate_expected_time()
        actual_time = self.get_actual_travel_time()

        return actual_time > expected_time + 60


    


# Example usage
if __name__ == "__main__":
    machine_speed = 60  # miles per hour
    location_a = Location("Point A", 100)
    location_b = Location("Point B", 200)
    machine = Machine(machine_speed)
    
    travel_simulator = TravelSimulator(machine, location_a, location_b)
    has_obstruction = travel_simulator.check_obstructions()
    
    if has_obstruction:
        print("There is an impenetrable obstruction.")
    else:
        print("No obstructions found.")

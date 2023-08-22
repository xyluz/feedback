'''
FEEDBACK
1. Check line 23
2. Using geodesic is against the rule, you used a package/library
3. Check other people's implementation in the feedback repo
'''
from geopy.distance import geodesic

class Detector:
    def __init__(self, speed):
        self.speed = speed

    def expected_time(self, distance):
        return distance / self.speed

    def check_obstructions(self, distance, expected_time, max_delay=60):
        simulated_time = self.expected_time(distance)
        time_difference = simulated_time - expected_time
        
        if time_difference <= 0:
            return False  # No obstructions

        return time_difference > max_delay:

        


# Simulated speed value
speed_of_machine = 50  # miles per hour

# Actual coordinates for point A and point B
point_a = (53.5872, -2.4138)
point_b = (53.474, -2.2388)

# Calculate distance using geopy's geodesic function
distance_a_to_b = geodesic(point_a, point_b).miles

# Calculate time duration in minutes
time_duration_hours = distance_a_to_b / speed_of_machine
time_duration_minutes = time_duration_hours * 60

# Simulated expected time (you can calculate this using the speed and distance)
expected_time_a_to_b = distance_a_to_b / speed_of_machine

obstruct_detector = Detector(speed_of_machine)
obstruct_detected = obstruct_detector.check_obstructions(distance_a_to_b, expected_time_a_to_b)

print(f"TimeDuration Module determines that it will take {time_duration_minutes:.0f} mins from Point A to Point B.")
print(f"YourModule determines expected time from Point A to Point B is {expected_time_a_to_b:.1f} mins.")

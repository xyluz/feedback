"""
    FEEDBACK:
    1. There is a difference between simulated and hardcoded
    2. Location is given in list of [long,lat], your code did not cater for that
    3. There is no validation or error handling, your module will crash if wrong data is sent and users will not know why
    4. Check line 28
    5. Check line 41

"""

class ObstructionDetector:
    def __init__(self, speed, distance) -> None:
        """
        initialize instance of ObstructionDetector with the speed of the
            machine and the distance between points A and B

        :param speed: Speed of the machine in miles per minute
        :param distance: Distance between points A and B in miles
        """
        self.speed = speed
        self.distance = distance

    def calculate_expected_time(self) -> float:
        """
        calculate the expected time to travel from point A to point B based on
            the speed and distance

        :return:    Expected time in minutes
        """
        return self.distance / self.speed

    def check_obstruction(self, time_from_TimeDuration) -> bool:
        """
        check for obstructions between points A and B

        :param time_from_TimeDuration: Time calculated from the TimeDuration
            module in minutes

        :return:    True or False
        """

        return  time_from_TimeDuration > self.calculate_expected_time()

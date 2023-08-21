"""FEEDBACK
1. Your method and class naming is a bit off, since you've been told the scope of the project.
2. Unneeded lines of code can be removed. Check line 49

"""

"""Module calculates best way to avoid obstructions"""
import math
from random import random
from typing import Union


class CalculateBestWay():
    """Class that calculates best route for a machine"""
    __obstruction_time_limit = 60  # time limit in minutes for obstruction to be said to be impenetrable

    def __init__(self, pointA: tuple, pointB: tuple) -> None:
        """Initialize the class"""
        self.__distance = self.__calculate_distance(pointA, pointB)
        self.__expected_time = None
        self.__speed = None

    @property
    def speed(self):
        """Getter for speed"""
        return self.__speed

    @speed.setter
    def speed(self, value):
        """Setter for speed"""
        if type(value) is not int and type(value) is not float:
            raise TypeError("Speed must be a number")
        if value < 0:
            raise ValueError("Speed cannot be negative")
        self.__speed = value

    def __calculate_distance(self, pointA: tuple, pointB: tuple) -> float:
        """calculate distance"""
        if type(pointA) is not tuple or type(pointB) is not tuple:
            raise (TypeError("Given points must be tuples"))

        x1 = pointA[0]
        y1 = pointA[1]
        x2 = pointB[0]
        y2 = pointB[1]

        distance_squared = math.pow(y1 - y2, 2) + math.pow(x1 - x2, 2)

        return math.pow(distance_squared, 0.5) //xyluz

    def check_for_obstructions(self) -> str:
        """checks if machine encounters an obstruction"""
        if not self.__speed:
            raise ValueError("Speed must be supplied")

        # calculate the expected time
        self.__expected_time = self.__distance / self.__speed

        # simulate the time taken
        time_taken = (random() * (self.__expected_time + 180))

        if (time_taken > self.__expected_time + self.__obstruction_time_limit):
            return f"""
                    [*] There is an obstruction
                    [*] The obstruction is impenetrable

                    it should take {round(self.__expected_time, 1)}mins to go from
                    pointA to pointB but it took {round(time_taken,1)}mins which is 
                    {round(self.__obstruction_time_limit, 1)}mins more than the expected time.
                  """

        if (time_taken > self.__expected_time):
            return f"""
                    [*] There is an obstruction

                    it should take {round(self.__expected_time, 1)}mins to go from
                    pointA to pointB but it took {round(time_taken, 1)}mins
                    """

        return f"""
                    [*] There is no obstruction

                    it should take {round(self.__expected_time, 1)}mins to go from
                    pointA to pointB but it took {round(time_taken,1)}mins.
                """

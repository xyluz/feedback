'''  FEEDBACK

1. This is way too lean and does not take all parameters into consideration. 
2. You didn't do any form of validation, what if the user sends the wrong type of data to initialize the module, then the module fails.
3. You have not done any form of error handling, what if the TimeDuration module fails, it means your module fails
4. Parameters for each point is given as a liste of latitude and longitude, your code did not cater for that
5. Your code assumes i already know the distance and real time


"""

'''FEEDBACK:


'''
This is a basic task to test your understanding of Object Oriented Programming. There are no right or wrong ways to do this, your main focus should be:

1. Make sure to use OOP

2. Use as many OOP concepts as possible without irrelevant methods or functions

3. Add comments and documentation within your code to expalin your thought process

4. Show example of how the class will be used.

5. No external APIs, No libraries, no frameworks, keep it lean and simple.
'''

class Obstruction:
    '''
    defines the obstruction
    '''
    def __init__(self, speed: float, distance: float) -> None:
        """
        initiaalize class obj with speed and distance
        """
        self.speed = speed
        self.distance = distance
    def impenetrable(self, real_time: float) -> bool:
        '''
        Logic:
            Calculate the expected time by dividing distance by speed,
            subtract the expected time from the actual time taken
        Return
            - True: if the subtracted value is grater than 60
            - False: otherwise
        '''
        return (real_time - (self.distance / self.speed)) > 60

"""
    FEEDBACK:
    1. expected_time should not be hardcoded
    2. Class naming and function naming should be better descriptive partaining to what you are building
    3. Distance is given in list of [long,lat], your code did not cater for that
    4. It appears you did not test your module, as there are many errors - you always test
    5. This is way too lean for the task, you didn't cater for all required points
    6. Check line 47
"""
"""
This an example of a Python Object Oriented Programming (OOP). 
where the Time of distance over speed is calculated, if there are obstructions
there will be a 60second added time """

# Given Expected Time
expected_time= 2.24

# Class model to define/assign the parameters
class OOP_TASK():
    def __init__(self,speed,obstruction):
        self.speed=speed
        self.obstruction=obstruction
        
# method for distance a to b
    def distance(self, a, b):
        result=False
        self.a=a
        self.b=b
        return b-a
    

        
    
#  defining and assigning parameters to our object   
object= OOP_TASK(50,60)

#Difference in distance, between a to b
distance_diff=object.distance(120, 232)


# Time duration calculations
TimeDuration= distance_diff / object.speed + object.obstruction
print(TimeDuration , 'seconds' )

#Results based on obstructions or not
def result():
    return TimeDuration> expected_time:

    
print(result(),'-Obstruction')
        






            







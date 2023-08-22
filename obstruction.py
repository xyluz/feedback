''' FEEDBACK:
1. Check the feedback repo for ideas on how others solved the problem
2. Check line  13
'''
class OBS:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b
        self.distance = self.a - self.b
    
    def there_is_or_no_obstruction(self, speed):

        return (self.distance / speed) >= 60

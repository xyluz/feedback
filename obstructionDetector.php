<?php

/**
 * FEEDBACK
 * 1. PHP 8 allows type hint, it makes your code more readable and easier
 * to understand - plus, since you are connecting with other modules,
 * type hinting makes your code more strict with requirements (Your code is written in php5.6)
 * 2. Check line 13: By declaring the parameter, scope and type in the constructor, the parameter becomes available throughout the class.
 * 3. Readonly because those values are supplied by user or another module, hence you don't want to change them.
 * 4. Your class is also readonly because it doesn't change the values of the parameters. (Check line 12)
 * 5. Check line 23 and 24
 * 6. Check line 36, the advantage of using descriptive variable names is that it makes your code more readable and easier to understand.
 * And you can avoid unnecessary lines of code
 * 7. Location is give in array of coordinates [x,y], your code did not cater for that
 */
readonly class ObstructionDetector {

    public function __construct(private int|float $speed, private int|float $distance) {
    }


    /**
     * Calculate the expected time to travel from point
     *  A to point B based on speed and distance
     * @return float|int
     */
    
    public function calculateExpectedTime(): float|int
    {
        return ($this->distance / $this->speed) * 60;
    }

    /**
     * Check for obstructions and determine if they are
     *  impenetrable based on actual time taken
     *
     * @param $actualTime
     * @return bool
     */

    public function checkObstructions($actualTime): bool
    {
        return ($actualTime - $this->calculateExpectedTime()) > 60;
    }

}

/**
 * Simulated values gotten from another module  
 */ 

 $machineSpeed = 20; // miles per hour
 $distance_A_B = 10; // miles
 $actualTravelTime = 78; // minutes

 // Creating an instance of the ObstructionDetector class
 $diggingModule = new ObstructionDetector($machineSpeed, $distance_A_B);

 // Check for obstructions and impenetrable obstructions
 $obstructionResult = $diggingModule->checkObstructions($actualTravelTime);

 // Display the result based on obstruction detection
 if($obstructionResult){
    echo "There is na obstruction, and it's impenetrable";
 } else {
    echo "No obstruction";
 }

?>
/**
 * FEEDBACK
 * 1. check line 23
 * 2. Check line 35
 * 3. Your code has no validation or error handling
 * 4. Your solution is too lean and does not cater for all the conditions of the tas
 * 5. Location is given in [x,y] coordinates, you did not cater for this
 */
class ObstructionDetector {
    constructor(speed, distance) {
        /**
         * Initialize the ObstructionDetector with speed and distance.
         *
         * @param {number} speed - Speed of the machine in miles per minute.
         * @param {number} distance - Distance between points A and B in miles.
         */
        this.speed = speed;
        this.distance = distance;
    }

    calculateExpectedTime() {
        /**
         * Calculate the expected time to travel from point A to point B.
         *
         * @return {number} Expected time in minutes.
         */
        return this.distance / this.speed;

    }

    checkObstruction(actualTime) {
        /**
         * Check for obstructions and determine if they are impenetrable.
         *
         * @param {number} actualTime - Actual time taken to travel from point A to point B in minutes.
         * @return {boolean} True if there is an impenetrable obstruction, false otherwise.
         */
        return actualTime > this.calculateExpectedTime()+60;

    }
}

// Example usage
const actualTime = 78;  // minutes

// Create an instance of ObstructionDetector with speed and distance
const speedOfMachine = 4;  // miles per minute
const distanceAToB = 10;   // miles
const detector = new ObstructionDetector(speedOfMachine, distanceAToB);

// Determine if there is an obstruction and if it's impenetrable
const isImpenetrableObstruction = detector.checkObstruction(actualTime);

if (isImpenetrableObstruction) {
    console.log("There is an impenetrable obstruction.");
} else {
    console.log("There are no impenetrable obstructions.");
}

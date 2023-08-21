/**
 * FEEDBACK:
 *
 * 1. This is way too lean
 * 2. You didn't do any validations
 * 3. You didn't do any error handling
 * 4. You didn't do any logging
 * 5. Check line 17
 * 6. Check line 25
 * 7. You did not leverage on OOP concepts such as setters and getters, instead you hard coded the values
 *
 */
class ObstructionDetector {
    constructor(speed, distance) {
        this.speed = speed;
        this.distance = distance;
    }

    calculateExpectedTime() {
        return this.distance / this.speed;
    }

    hasImpenetrableObstruction(actualTime, tolerance = 60) {
        const expectedTime = this.calculateExpectedTime();
        const timeDifference = actualTime - expectedTime;

        return timeDifference > tolerance;

    }
}

// Example usage
const actualTime = 78; // Simulated time from another module (in minutes)
const speed = 0.1; // Speed of the machine (in miles per minute)
const distance = 5.0; // Distance between points A and B (in miles)

// Create an instance of the ObstructionDetector class
const obstructionDetector = new ObstructionDetector(speed, distance);

// Check for impenetrable obstructions
const isImpenetrable = obstructionDetector.hasImpenetrableObstruction(actualTime);

if (isImpenetrable) {
    console.log("There is an impenetrable obstruction.");
} else {
    console.log("There is no impenetrable obstruction.");
}

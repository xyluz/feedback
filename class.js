/**
 * FEEDBACK:
 * 1. Check line 50,
 * 2. Check line 33
 * 3. detectObstruction returns either string or bool, this is not a good practice. Your return type should be consistent.
 * 4. Check line 62
 */
class ObstructionDetector {
  /**
   * A class to detect obstructions in the route between two locations.
   *
   * @param {number} speed - The speed of the machine used for digging in miles per hour.
   * @param {number} distance - The distance between location A and location B in miles.
   * @param {number} expectedTime - The expected time it will take to travel from A to B based on speed and distance.
   */
  constructor(speed, distance, expectedTime) {
      this.speed = speed;
      this.distance = distance;
      this.expectedTime = expectedTime;
  }

  /**
   * Detects if there is an obstruction between location A and location B.
   *
   * @returns {boolean|string} False if no obstruction is detected. "impenetrable" if an obstruction is detected and it's impenetrable. True if an obstruction is detected but not impenetrable.
   */
  detectObstruction() {
      // Simulate time taken from another module
      const timeDurationModuleResult = this.simulateTimeDurationModule(this.speed, this.distance);

      // Calculate difference between expected time and actual time
      const timeDifference = Math.abs(this.expectedTime - timeDurationModuleResult);

      return timeDurationModuleResult > this.expectedTime && timeDifference > 60 // This is a better way to write it. Check that it works and refactor accordingly

  }

  /**
   * Simulates the result from the time duration module.
   *
   * @param {number} speed - Speed of the machine in miles per hour.
   * @param {number} distance - Distance between location A and location B in miles.
   * @returns {number} Simulated time duration in minutes.
   */
  simulateTimeDurationModule(speed, distance) {
      // Simulate the calculation, here we assume some formula to calculate time duration
      // based on speed and distance
      return (distance / speed) * 60;
  }
}

// Example values for demonstration purposes
const correctedSpeed = 0.16; // miles per hour (approximately)
const correctedDistance = 0.21; // miles (approximately)
const expectedTime = 15.2; // minutes

// Create an instance of ObstructionDetector with corrected values
const obstructionDetector = new ObstructionDetector(correctedSpeed, correctedDistance, expectedTime);

// Detect obstruction
const obstructionResult = obstructionDetector.detectObstruction();

console.log(obstructionResult ? "There is an impenetrable obstruction." : "No obstructions.")



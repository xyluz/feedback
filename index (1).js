/**
 * FEEDBACK
 * 1.Check line 11
 * 2. Check line 15
 * 3. Your code has no validation or error handling
 * 4. Your solution is too lean and does not cater for all the conditions of the tas
 * 5. Location is given in [x,y] coordinates, you did not cater for this
 */
class detectObstruction {
  constructor(machineSpeed) {
    this.machineSpeed = machineSpeed;
  }

  calculateExpectedTime(distance) {
    return (distance / this.machineSpeed) * 60;
  }

  checkObstruction(actualTime, expectedTime) {
    return actualTime > expectedTime + 60;
  }
}

// Example usage
const machineSpeed = 30; // miles per hour
const distanceAB = 10; // miles
const actualTravelTime = 78; // minutes
const expectedTravelTime = new detectObstruction(
  machineSpeed
).calculateExpectedTime(distanceAB);

// Create an instance of detectObstruction
const detector = new detectObstruction(machineSpeed);

// Check for obstructions
const isObstruction = detector.checkObstruction(
  distanceAB,
  actualTravelTime,
  expectedTravelTime
);

if (isObstruction) {
  console.log("There is an impenetrable obstruction.");
} else {
  console.log("No obstruction detected.");
}

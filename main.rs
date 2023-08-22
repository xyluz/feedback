/** FEEDBACK
    1. Check line 20
    2. Check line 43
**/

/// Represents a geographical location with latitude and longitude.
struct Location {
    lat: f64,
    long: f64,
}

/// The RouteAnalyzer struct helps in determining obstructions and their impenetrability.
struct RouteAnalyzer {
    machine_speed: f64,
}

impl RouteAnalyzer {
    /// Creates a new RouteAnalyzer with the given machine speed.
    fn new(machine_speed: f64) -> Self {
        Self { machine_speed }
    }

    /// Calculates the expected time to travel between two locations.
    fn expected_time(&self, distance: f64) -> f64 {
        distance / self.machine_speed
    }

    /// Determines if there's an obstruction based on the difference between expected and actual time.
    fn is_obstruction(&self, expected_time: f64, actual_time: f64) -> bool {
        actual_time > expected_time
    }

    /// Determines if an obstruction is impenetrable.
    fn is_impenetrable(&self, expected_time: f64, actual_time: f64) -> bool {
        actual_time - expected_time > 60.0
    }

    /// Analyzes the route for obstructions.
    fn analyze_route(&self, distance: f64, actual_time_from_module: f64) -> (bool, bool) {
        let expected = self.expected_time(distance);
        let obstruction = self.is_obstruction(expected, actual_time_from_module);
        let impenetrable = obstruction && self.is_impenetrable(expected, actual_time_from_module);

        (obstruction, impenetrable)
    }
}

fn main() {
    // Example usage
    let analyzer = RouteAnalyzer::new(0.1);  // Assuming the machine speed is 0.1 miles per minute
    let distance_ab = 5.2; // For example purpose, usually calculated using another module.
    let actual_time_from_module = 78.0;

    let (obstruction, impenetrable) = analyzer.analyze_route(distance_ab, actual_time_from_module);
    println!("Is there an obstruction? {}", obstruction);
    println!("Is the obstruction impenetrable? {}", impenetrable);
}

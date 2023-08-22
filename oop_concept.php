<?php
/**
 * FEEDBACK
 * 1. Type int, PHP allows type hint, makes your code neater and less prone to error especially since you are collaborating with others
 * 2. Your constructor parameter becomes available throughout the class if you add scope - check line 8
 * 3. Add return type to your methods
 * 4. Check line 12
 * 5. Check line 19
 * 6. Check line 26
 */
    class obstructionDetector {
        public function __construct(public float|int $speed){
        }
        public function calculateExpectedTime(float | int $distance): float | int{
            return $distance / $this->speed;
        }

        public function detectObstruction($point_A, $point_B, $timeDuration): bool{

            $expectedTime = $this->calculateExpectedTime($this->calculateDistance($point_A, $point_B));
            return $timeDuration > ($expectedTime + 60);

        }

        private function calculateDistance(float $point_A, float $point_B){
            return sqrt(pow($point_B[0] - $point_A[0], 2) + pow($point_B[1] - $point_A[1], 2));
        }
        
    }

    $obstructionDetected = new obstructionDetector(50);

    $point_A = [53.5872, -2.4138];
    $point_B = [53.474, -2.2388];

    $timeDuration = 78;
    $obstructionDetected = $obstructionDetected->detectObstruction($point_A, $point_B, $timeDuration);

    if($obstructionDetected) {
        echo "obstruction detected. Impenetrate obstruction!";
    } else{
        echo "No obstruction Detected";
    }

    ?>
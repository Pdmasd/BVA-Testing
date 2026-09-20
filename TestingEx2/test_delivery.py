import unittest
from delivery import DeliveryFee

class TestDelivery(unittest.TestCase):

    all_passed = True
    test_count = 0

    def check_result(self, time, distance, actual, expected, name):
        TestDelivery.test_count += 1
        status = "PASS" if actual == expected else "FAIL"

        print(
            "TC-"
            f"{TestDelivery.test_count} | "
            f"[{status}] {name} | "
            f"Time={time}, Distance={distance} | "
            f"Expected={expected} | Actual={actual}"
        )

        if actual != expected:
            TestDelivery.all_passed = False

    def test_time_boundaries(self):
        nom_distance = 3

        self.check_result(
            -0.1, nom_distance,
            DeliveryFee.calculate(-0.1, nom_distance),
            "Invalid",
            "Time boundary"
        )

        self.check_result(
            0.0, nom_distance,
            DeliveryFee.calculate(0.0, nom_distance),
            25000,
            "Time boundary"
        )

        self.check_result(
            0.1, nom_distance,
            DeliveryFee.calculate(0.1, nom_distance),
            25000,
            "Time boundary"
        )

        self.check_result(
            5.9, nom_distance,
            DeliveryFee.calculate(5.9, nom_distance),
            25000,
            "Time boundary"
        )

        self.check_result(
            6.0, nom_distance,
            DeliveryFee.calculate(6.0, nom_distance),
            15000,
            "Time boundary"
        )

        self.check_result(
            6.1, nom_distance,
            DeliveryFee.calculate(6.1, nom_distance),
            15000,
            "Time boundary"
        )

        self.check_result(
            21.9, nom_distance,
            DeliveryFee.calculate(21.9, nom_distance),
            15000,
            "Time boundary"
        )

        self.check_result(
            22.0, nom_distance,
            DeliveryFee.calculate(22.0, nom_distance),
            25000,
            "Time boundary"
        )

        self.check_result(
            22.1, nom_distance,
            DeliveryFee.calculate(22.1, nom_distance),
            25000,
            "Time boundary"
        )

        self.check_result(
            23.9, nom_distance,
            DeliveryFee.calculate(23.9, nom_distance),
            25000,
            "Time boundary"
        )

        self.check_result(
            24.0, nom_distance,
            DeliveryFee.calculate(24.0, nom_distance),
            "Invalid",
            "Time boundary"
        )

        self.check_result(
            24.1, nom_distance,
            DeliveryFee.calculate(24.1, nom_distance),
            "Invalid",
            "Time boundary"
        )

    def test_distance_boundaries(self):
        nom_time = 8.0

        self.check_result(
            nom_time, -1,
            DeliveryFee.calculate(nom_time, -1),
            "Invalid",
            "Distance boundary"
        )

        self.check_result(
            nom_time, 0,
            DeliveryFee.calculate(nom_time, 0),
            "Invalid",
            "Distance boundary"
        )

        self.check_result(
            nom_time, 1,
            DeliveryFee.calculate(nom_time, 1),
            15000,
            "Distance boundary"
        )

        self.check_result(
            nom_time, 4,
            DeliveryFee.calculate(nom_time, 4),
            15000,
            "Distance boundary"
        )

        self.check_result(
            nom_time, 5,
            DeliveryFee.calculate(nom_time, 5),
            15000,
            "Distance boundary"
        )

        self.check_result(
            nom_time, 6,
            DeliveryFee.calculate(nom_time, 6),
            20000,
            "Distance boundary"
        )

        self.check_result(
            nom_time, 49,
            DeliveryFee.calculate(nom_time, 49),
            235000,
            "Distance boundary"
        )

        self.check_result(
            nom_time, 50,
            DeliveryFee.calculate(nom_time, 50),
            240000,
            "Distance boundary"
        )

        self.check_result(  
            nom_time, 51,
            DeliveryFee.calculate(nom_time, 51),
            "Invalid",
            "Distance boundary"
        )

    def test_nominal_case(self):
        time = 8.0
        distance = 3

        self.check_result(
            time, distance,
            DeliveryFee.calculate(time, distance),
            15000,
            "Nominal case"
        )


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDelivery)

    runner = unittest.TextTestRunner(
        verbosity=0,
        stream=open('nul', 'w')
    )

    runner.run(suite)

    if TestDelivery.all_passed:
        print("\nALL TESTS PASSED")

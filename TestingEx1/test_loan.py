import unittest
from loan_processor import LoanProcessor

class TestLoan(unittest.TestCase):

    all_passed = True

    def check_result(self, age, income, actual, expected, name):
        status = "PASS" if actual == expected else "FAIL"

        print(
            f"[{status}] {name} | "
            f"Age={age}, Income={income} | "
            f"Expected={expected} | Actual={actual}"
        )

        if actual != expected:
            TestLoan.all_passed = False

    def test_income_boundaries(self):
        nom_age = 25

        self.check_result(
            nom_age, 9.9,
            LoanProcessor.evaluate_loan(nom_age, 9.9),
            "Rejected",
            "Income boundary"
        )

        self.check_result(
            nom_age, 10.0,
            LoanProcessor.evaluate_loan(nom_age, 10.0),
            "Low Approval",
            "Income boundary"
        )

        self.check_result(
            nom_age, 10.1,
            LoanProcessor.evaluate_loan(nom_age, 10.1),
            "Low Approval",
            "Income boundary"
        )

        self.check_result(
            nom_age, 29.9,
            LoanProcessor.evaluate_loan(nom_age, 29.9),
            "Low Approval",
            "Income boundary"
        )

        self.check_result(
            nom_age, 30.0,
            LoanProcessor.evaluate_loan(nom_age, 30.0),
            "High Approval",
            "Income boundary"
        )

        self.check_result(
            nom_age, 30.1,
            LoanProcessor.evaluate_loan(nom_age, 30.1),
            "High Approval",
            "Income boundary"
        )

    def test_age_boundaries(self):
        nom_income = 20.0

        self.check_result(
            17, nom_income,
            LoanProcessor.evaluate_loan(17, nom_income),
            "Rejected",
            "Age boundary"
        )

        self.check_result(
            18, nom_income,
            LoanProcessor.evaluate_loan(18, nom_income),
            "Low Approval",
            "Age boundary"
        )

        self.check_result(
            19, nom_income,
            LoanProcessor.evaluate_loan(19, nom_income),
            "Low Approval",
            "Age boundary"
        )

        self.check_result(
            64, nom_income,
            LoanProcessor.evaluate_loan(64, nom_income),
            "Low Approval",
            "Age boundary"
        )

        self.check_result(
            65, nom_income,
            LoanProcessor.evaluate_loan(65, nom_income),
            "Low Approval",
            "Age boundary"
        )

        self.check_result(
            66, nom_income,
            LoanProcessor.evaluate_loan(66, nom_income),
            "Rejected",
            "Age boundary"
        )

    def test_nominal_case(self):
        age = 25
        income = 20.0

        self.check_result(
            age, income,
            LoanProcessor.evaluate_loan(age, income),
            "Low Approval",
            "Nominal case"
        )


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLoan)

    runner = unittest.TextTestRunner(
        verbosity=0,
        stream=open('nul', 'w')
    )

    runner.run(suite)

    if TestLoan.all_passed:
        print("\nALL TESTS PASSED")
class LoanProcessor:

    @staticmethod
    def evaluate_loan(age: int, income: float) -> str:
        if age < 18 or age >= 65:
            return "Rejected"
        if income < 10.0:
            return "Rejected"
        elif income < 30.0:
            return "Low Approval"
        else:
            return "High Approval"
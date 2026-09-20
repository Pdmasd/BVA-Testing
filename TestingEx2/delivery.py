class DeliveryFee:

    @staticmethod
    def calculate(time: float, distance: float):
        if time < 0.0 or time >= 24.0 or distance <= 0 or distance > 50:
            return "Invalid"
        if 6.0 <= time <= 22.0:
            if distance <= 5:
                return 15000
            else:
                return 15000 + 5000 * (distance - 5)
        else:
            if distance <= 5:
                return 25000
            else:
                return 25000 + 5000 * (distance - 5)
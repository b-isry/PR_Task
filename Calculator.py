class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        """
        Divides a by b.
        
        Args:
            a (float): Numerator.
            b (float): Denominator.
        
        Returns:
            float: The result of division.
        
        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError('Error: Division by zero is not allowed.')
        return a / b

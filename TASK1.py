# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.

class Calculator:
    

    def __init__(self):
        # Define supported operators and their corresponding functions
        self.operations = {
            '+': self._add,
            '-': self._subtract,
            '*': self._multiply,
            'x': self._multiply, # Alternate for multiplication operation
            '/': self._divide
        }

    def _add(self, a, b):
        return a + b

    def _subtract(self, a, b):
        return a - b

    def _multiply(self, a, b):
        return a * b

    def _divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not possible."
        return a / b

    def process_expression(self, expression_str):
        """
        Analyzes the input string, performs the calculation, and returns the result.
        Handles various input and calculation errors.
        """
        parts = expression_str.strip().split()

        # Validate input format length
        if len(parts) != 3:
            return "Error: Invalid format. Please use 'a operator b'."

        try:
            a = float(parts[0])      
            op = parts[1].lower()    
            b = float(parts[2])      
        except ValueError:
            return "Error: Please ensure 'a' and 'b' are valid numbers."

        # Check if the operator is supported
        if op not in self.operations:
            return f"Error: Invalid operator '{op}'. Supported operators are {', '.join(self.operations.keys())}."

        # Perform the operation
        result = self.operations[op](a, b) # Only Use a, b, and op

        return result

    def run(self):
        """
        Let's start the interactive calculator session.
        """
        print("\nWELCOME TO THE SIMPLE CALCULATOR :)")
        print("Enter expressions like '5 + 3', '10 / 2', '7 x 4' to get perfect results.")
        print("Type 'exit' to quit.")

        while True:
            user_input = input("Enter expression: ").strip()

            if user_input.lower() == 'exit':
                print("Exiting calculator. It was a pleasure crunching numbers with you. Goodbye")
                break

            calculation_result = self.process_expression(user_input)

            if isinstance(calculation_result, str) and calculation_result.startswith("Error:"):
                print(calculation_result) # It Print error messages directly
            else:
                # Reconstruct expression for clear output using the original parts
                parts = user_input.strip().split()
                if len(parts) == 3: # Only if valid parts were initially parsed
                    print(f"Result: {parts[0]} {parts[1]} {parts[2]} = {calculation_result}")
                else:
                    print(f"Result: {calculation_result}") 

            print("-" * 30) # Separator for next input

if __name__ == '__main__':
    calc_app = Calculator()
    calc_app.run()
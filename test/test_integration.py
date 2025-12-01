import unittest
from src import calculator

class TestIntegration(unittest.TestCase):
    """Integration tests - testing combined function workflows."""
    
    def test_workflow_1_basic_calculations(self):
        """Test basic workflow: add, subtract, multiply."""
        # Add two numbers
        sum_result = calculator.fun1(5, 3)
        self.assertEqual(sum_result, 8)
        
        # Subtract from result
        diff_result = calculator.fun2(sum_result, 2)
        self.assertEqual(diff_result, 6)
        
        # Multiply by 2
        mult_result = calculator.fun3(diff_result, 2)
        self.assertEqual(mult_result, 12)
    
    def test_workflow_2_advanced_operations(self):
        """Test workflow with advanced functions."""
        # Start with base number
        base = calculator.fun5(100, 2)  # 50
        self.assertEqual(base, 50.0)
        
        # Add a number
        added = calculator.fun1(base, 50)  # 100
        self.assertEqual(added, 100.0)
        
        # Take power
        powered = calculator.fun6(2, added / 50)  # 2^2 = 4
        self.assertEqual(powered, 4)
    
    def test_workflow_3_combined_math(self):
        """Test complex calculation workflow."""
        # (10 + 5) * 2 - 3 = 27
        step1 = calculator.fun1(10, 5)
        step2 = calculator.fun3(step1, 2)
        step3 = calculator.fun2(step2, 3)
        self.assertEqual(step3, 27)
    
    def test_workflow_4_with_modulo_and_sqrt(self):
        """Test workflow with modulo and square root."""
        # Get remainder
        remainder = calculator.fun8(20, 6)  # 2
        self.assertEqual(remainder, 2)
        
        # Add to make perfect square
        sum_result = calculator.fun1(remainder, 14)  # 16
        self.assertEqual(sum_result, 16)
        
        # Get square root
        sqrt_result = calculator.fun7(sum_result)  # 4
        self.assertEqual(sqrt_result, 4.0)
    
    def test_error_handling_integration(self):
        """Test error handling in workflows."""
        # Division by zero should raise error
        with self.assertRaises(ValueError):
            calculator.fun5(10, 0)
        
        # Square root of negative should raise error
        with self.assertRaises(ValueError):
            calculator.fun7(-5)
        
        # Modulo by zero should raise error
        with self.assertRaises(ValueError):
            calculator.fun8(10, 0)

if __name__ == '__main__':
    unittest.main()

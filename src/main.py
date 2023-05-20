import unittest

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

class CelsiusToFahrenheitTestCase(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):

        celsius = 0
        expected_result = 32
        self.assertEqual(celsius_to_fahrenheit(celsius), expected_result)

        celsius = -40
        expected_result = -40
        self.assertEqual(celsius_to_fahrenheit(celsius), expected_result)

        celsius = 100
        expected_result = 212
        self.assertEqual(celsius_to_fahrenheit(celsius), expected_result)

if __name__ == '__main__':
    unittest.main()

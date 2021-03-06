import unittest

class ExampleTests(unittest.TestCase):
    output = []
    for n in range(100):
        output.append(str(f(n) + "\n"))

    expected = open("fizzbuzz-output.txt", "r")
    i = 0
    for line in expected:
        if line == output[i]:
            print("Success!")
            i += 1
        else:
            print("Nope. Try Again.")

if __name__ == "__main__":
    unittest.main()
    
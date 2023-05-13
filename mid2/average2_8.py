""" Modify the test-averaging algorithm of
Exercise 3 so that it reads in 15 test scores
rather than 4. There are 14 regular tests and a
final examination, which counts twice as much
as a regular test. Use a loop to input and sum
the scores. """

num_tests = 15
regular_tests = num_tests - 1

total_score = 0

for i in range(regular_tests):
    score = float(input(f"Enter the marks for test {i+1}: "))
    total_score += score

final = float(input("Enter the final test marks: "))

test_average = total_score / regular_tests

average = (test_average * 0.4) + (final * 0.6)

print("The average of 15 tests is: ", average)
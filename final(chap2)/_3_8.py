""" 
write an algorithm that it reads in 15 test scores
rather than 4. There are 14 regular tests and a
final examination, which counts twice as much
as a regular test. Use a loop to input and sum
the scores. """

num_of_test = 15
regular_test = num_of_test - 1
total_score = 0

for i in range(regular_test):
    score = float(input(f"Enter the score for test {i+1}: "))
    total_score += score

final_exam = float(input("Enter the score for final exam: "))

total_score += (final_exam*2)

avg = total_score / (regular_test+2) 

print("The average of 15 tests is : ", avg)
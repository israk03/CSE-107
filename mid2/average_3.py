""" write an algorithm that gets
four numbers corresponding to scores received
on three semester tests and a final examination.
Your algorithm should compute and display
the average of all four tests, weighting the final
exam twice as heavily as a regular test. """

s1 = float(input("Enter the marks for test 1: "))
s2 = float(input("Enter the marks for test 2: "))
s3 = float(input("Enter the marks for test 3: "))
s4 = float(input("Enter the marks for final test: "))

average = ((s1 + s2 + s3) / 3) * 0.4 + (s4  * 0.6)

print("The average of all four test is: ", average)
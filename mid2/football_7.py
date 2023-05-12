""" Write an code that uses a loop (1) to
input 10 pairs of numbers, where each pair
represents the score of a football game with
the Computer State University (CSU) score
listed first, and (2) for each pair of numbers,
to determine whether CSU won or lost. After
reading in these 10 pairs of values, print the
won/lost/tie record of CSU. In addition, if
this record is a perfect 10-0, then print the
message ‘Congratulations on your undefeated
season’. """

wins = 0
losses = 0
ties = 0

for i in range(10): 
    csu, opp = map(int,input(f"Enter the scores for game {i+1}: ").split())

    if csu>opp:
        wins += 1
        print("CSU win.")
    elif csu<opp:
        losses += 1
        print("CSU lost.")
    else:
        print("It's tie.")

print(f"CSU's record is {wins}-{losses}-{ties}.")

if wins == 10:
    print("Congratulations on your undefeated season")
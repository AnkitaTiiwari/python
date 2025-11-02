#now we are playing rock paper scissor game
import random, sys

print("Rock Papaer Scissor")

win = 0
lose = 0
tie = 0

while True:
    print(f'Wins: {win}, Losses: {lose}, Ties: {tie} ')

    while True:
        print("Enter your move: rock(r), paper(p), scissor(s) or quit(q) to exit")
        player_move = input()

        if player_move == 'q':
            sys.exit()
        elif player_move not in ['r', 'p', 's']:
            print("Invalid move. Please try again.")
            continue

        if player_move == 'r':
            print("Rock vs ...")
        elif player_move == 'p':
            print("Paper vs ...")
        elif player_move == 's':
            print("Scissor vs ...")

        #computer is guess now
        computer_move = random.choice(['r', 'p', 's'])
        if computer_move == 'r':
            print("Rock")
        elif computer_move == 'p':
            print("Paper")
        elif computer_move == 's':
            print("Scissor")

        #now actually we compare the moves
        if player_move == computer_move:
            print("It's a tie!")
            tie += 1
        elif (player_move == 'r' and computer_move == 's') or \
            (player_move == 'p' and computer_move == 'r') or \
            (player_move == 's' and computer_move == 'p'):
            print("You win!")
            win += 1
        else:
            print("You lose!")
            lose += 1           
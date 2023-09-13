def ResetGame():
    global player1
    global player2
    player1=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player2=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def PlayHole(hole, score1, score2):
    try:
        ent=int(hole) - 1
        player1[ent] = score1
        player2[ent] = score2
        if int(player1[ent]) > 5:
           player1[ent]=5
        if int(player2[ent]) > 5:
           player2[ent]=5
        print('\n            Your scores are in.')
    except:
        print("""
        Please make sure you start new game or
        load a previous saved game to start entering scores""")

def TotalScore(player1, player2):
    player1 = [int(x) for x in player1]
    total1 = sum(player1)
    player2 = [int(x) for x in player2]
    total2 = sum(player2)

    if total1 > total2:
        print ("Player 2 is in the lead with a score of", total2,
               "beating Player 1's score of",total1)
    if total2 > total1:
        print ("Player 1 is in the lead with a score of", total1,
               "beating Player 2's score of",total2)
    if total1 == total2:
        print ("Both Players are tied at", total1,"points.")

def ShowScores():
    print ('Player 1:',*player1)
    print ('Player 2:',*player2)

def SaveGame():
    save = player1 + player2
    game = open("Golf.txt","w")
    for count in save:
        game.writelines(str(f'{count}\n'))
    game.close

def LoadGame():
    ResetGame()
    game= open("Golf.txt", "r")
    for i, line in enumerate(game):
        number = int(line.strip())
        if i < 18:
            player1[i] = number
        else:
            player2[i-18] = number
    game.close
    

def main():
    choice= int(input("""
1. Start New Game
2. Play a hole
3. Show current scores
4. Save game
5. Load last saved game
6. Exit Game
"""))
    if choice == 1:
        ResetGame()
        print('\n         The scores were reset. You are ready to play.')
        main()
    if choice == 2:
        hole = int(input('Which hole would you like to play 1 to 18? '))
        if hole > 18:
            print("Sorry. that is not a valid hole number. Please try again.")
            main()
        score1 = input('How many stroke did player one take? ')
        score2 = input('How many strokes did player two take? ')
        PlayHole(hole, score1, score2)
        main()
    if choice == 3:
        TotalScore(player1, player2)
        ShowScores()
        main()
    if choice == 4:
        SaveGame()
        print ('\n      Save Complete')
        main()
    if choice == 5:
        LoadGame()
        print('\n       Game Loaded')
        main()
    if choice == 6:
        print ('\n      You have exited')
    
main()    

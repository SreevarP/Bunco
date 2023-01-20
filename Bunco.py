#imports random for dice, colorama for colored text, and time to trick the user into thinking the program is actually doing something
import random
import colorama
from colorama import Back, Fore, Style
import time
#⚀⚁⚂⚃⚄⚅
#colorama.init(autoreset=True) - initalizes colorama class and autoreset just turns text back to default colors after meathods are applied. 
colorama.init(autoreset=True)
#Normalizes score turn and wins too zero 
player1_score = 0
player2_score = 0
player_turn = 0
player1_wins = 0
player2_wins = 0

#given a int roll displayRollChar returns the roll on the face of a die. 
def displayRollChar(roll):
  if roll == 6:
    return '⚅'
  elif roll == 5:
    return '⚄'
  elif roll == 4:
    return '⚃'
  elif roll == 3:
    return '⚂'
  elif roll == 2:
    return '⚁'
  else:
    return '⚀'

#displayRoll takes in 8 parameters which help it display the roll with the correct colored text. 
def displayRoll(roll1, roll2, roll3, bunco, allSame, roll1_hit, roll2_hit,
                roll3_hit):
  if bunco:
    print(Back.BLACK + Fore.GREEN + displayRollChar(roll1) + " " + displayRollChar(roll2) +
        " " + displayRollChar(roll3))
    # if a bunco is hit then all roll are colored green
  elif allSame:
    print(Back.BLACK + Fore.GREEN + displayRollChar(roll1) + " " + displayRollChar(roll2) +
        " " + displayRollChar(roll3))
    #if all are the same rolls are also colored green
  elif roll1_hit or roll2_hit or roll3_hit:
    #if any of the rolls are a hit check for two combinations of rolls
    if roll1_hit and roll2_hit:
      print(Back.BLACK + Fore.GREEN +     displayRollChar(roll1) + " " + Fore.GREEN+displayRollChar(roll2) +
        " " + Fore.RED + displayRollChar(roll3))
      #if roll1 and roll2 are a hit color the first and second roll green and the thrid red

    elif roll2_hit and roll3_hit:
      print(Back.BLACK + Fore.RED + displayRollChar(roll1) + " " + Fore.GREEN + displayRollChar(roll2) +
        " " + Fore.GREEN + displayRollChar(roll3))
      #if roll2 and roll3 are a hit color the second and thrid roll green and the first red
      
    elif roll3_hit and roll1_hit:
      print(Back.BLACK + Fore.GREEN + displayRollChar(roll1) + " " + Fore.RED + displayRollChar(roll2) +
        " " + Fore.GREEN + displayRollChar(roll3))
      #if roll1 and roll3 are a hit color the first and thrid roll green and the second red
      
    elif roll1_hit:
      #if none of those are true then check for indivual rolls
      print(Back.BLACK + Fore.GREEN + displayRollChar(roll1) + " " + Fore.RED + displayRollChar(roll2) + " " + Fore.RED +displayRollChar(roll3))
      #if roll one is hit, just color roll1 green and the rest red
    
    elif roll2_hit:
      print(Back.BLACK + Fore.RED + displayRollChar(roll1) + " " + Fore.GREEN + displayRollChar(roll2) +
        " " + Fore.RED + displayRollChar(roll3))
      #if roll two is hit, just color roll2 green and the rest red
     
    elif roll3_hit:
      print(Back.BLACK + Fore.RED + displayRollChar(roll1) + " " + Fore.RED + displayRollChar(roll2) +
        " " + Fore.GREEN + displayRollChar(roll3))
      #if roll three is hit, just color roll3 green and the rest red
  else:
    print(Back.BLACK + Fore.RED + displayRollChar(roll1) + " " + Fore.RED + displayRollChar(roll2) +
        " " + Fore.RED + displayRollChar(roll3))
    #else just color all rolls red because there is no hit
  


def turn(round, player):
  #boolean varible to check if player scored
  player1_scored = False
  player2_scored = False
  #net gain of points 1-21
  player1_net_gain = 0
  player2_net_gain = 0
  #global varibles 
  global player1_score
  global player2_score
  global player_turn
  #Generate three rolls
  roll1 = random.randint(1, 6)
  roll2 = random.randint(1, 6)
  roll3 = random.randint(1, 6)
  #boolean varibles check if any of the outcomes are true;
  bunco = False
  allSame = False
  roll1_hit = False
  roll2_hit = False
  roll3_hit = False
  #checks if bunco
  if roll1 == round and roll1 == roll2 == roll3:
    #if true prints cool colored text
    print(f"{Back.RED}B{Back.GREEN}U{Back.CYAN}N{Back.BLUE}C{Back.MAGENTA}O{Back.RED}!")
    print()
    #checks which player it is and adjusts accordingly
    if player == 0:
      player1_score += 21
      player1_scored = True
      player1_net_gain = 21
      bunco = True
      #adds 21 points to score 

    else:
      player2_score += 21
      player2_scored = True
      player2_net_gain = 21
      bunco = True

  elif roll1 != round and roll1 == roll2 == roll3:
    #checks if all are the same but does not match the round number. 
    if player == 0:
      player1_score += 5
      player1_scored = True
      player1_net_gain = 5
      allSame = True
      #adds 5 points to score

    else:
      player2_score += 5
      player2_scored = True
      player2_net_gain = 5
      allSame = True

  elif roll1 == round or roll2 == round or roll3 == round:
    #if any of the rolls are a hit then check how many are a hit 
    match_count = 0
    if roll1 == round:
      roll1_hit = True
      match_count += 1
    if roll2 == round:
      match_count += 1
      roll2_hit = True
    if roll3 == round:
      match_count += 1
      roll3_hit = True

    # add the points to the spefic player
    if player == 0:
      player1_score += match_count
      player1_scored = True
      player1_net_gain = match_count

    else:
      player2_score += match_count
      player2_scored = True
      player2_net_gain = match_count

  else:
    #if player doesn't score any points then player_turn is updated by one so it is the next player's turn. But notice this only happens when the player doesn't score any points so this way a player can go agian if they scored. 
    player_turn += 1
    #checks which player it is 
    if player == 0:
      player1_scored = False
      player1_net_gain = 0

    else:
      player2_scored = False
      player2_net_gain = 0

    # all boolean values are reset and normalized 
    roll1_hit = False
    roll2_hit = False
    roll3_hit = False
    bunco = False
    allSame = False
  # probably should have put this in a meathod, it just displays text with the apporiate coloring based on the outcome
  if bunco:
    #if bunco is true then the round number is green and the rolls are green and the displayRoll function is called with the local paramters and will display the rolls are green
    print(
      f"{Back.BLACK}Round Number: {Fore.GREEN}{round}{Fore.WHITE}, Player {player+1} rolled a {Fore.GREEN}{roll1}, {roll2}, {roll3}"
    )
    displayRoll(roll1, roll2, roll3, bunco, allSame, roll1_hit, roll2_hit, roll3_hit)
  elif allSame:
    #if all are the same round number is displayed as red but rolls are displayed as green
    print(
      f"{Back.BLACK}Round Number: {Fore.RED}{round}{Fore.WHITE}, Player {player+1} rolled a {Fore.GREEN}{roll1}, {roll2}, {roll3}"
    )
    displayRoll(roll1, roll2, roll3, bunco, allSame, roll1_hit, roll2_hit, roll3_hit)
  elif roll1_hit or roll2_hit or roll3_hit:
    if roll1_hit and roll2_hit:
      #checks for hits then combinations
      print(
        f"{Back.BLACK}Round Number: {Fore.GREEN}{round}{Fore.WHITE}, Player {player+1} rolled a {Fore.GREEN}{roll1}, {Fore.GREEN}{roll2}, {Fore.RED}{roll3}"
      )
      #if roll1 and roll2 are a hit color the first and second roll green and the thrid red
      displayRoll(roll1, roll2, roll3, bunco, allSame, roll1_hit, roll2_hit, roll3_hit)
    elif roll2_hit and roll3_hit:
      print(
        f"{Back.BLACK}Round Number: {Fore.GREEN}{round}{Fore.WHITE}, Player {player+1} rolled a {Fore.RED}{roll1}, {Fore.GREEN}{roll2}, {Fore.GREEN}{roll3}"
      )
      displayRoll(roll1, roll2, roll3, bunco, allSame, roll1_hit, roll2_hit, roll3_hit)
      #if roll2 and roll3 are a hit color the second and thrid roll green and the first red
    elif roll3_hit and roll1_hit:
      print(
        f"{Back.BLACK}Round Number: {Fore.GREEN}{round}{Fore.WHITE}, Player {player+1} rolled a {Fore.GREEN}{roll1}, {Fore.RED}{roll2}, {Fore.GREEN}{roll3}"
      )
      displayRoll(roll1, roll2, roll3, bunco, allSame, roll1_hit, roll2_hit, roll3_hit)
      #if roll1 and roll3 are a hit color the first and thrid roll green and the second red
    elif roll1_hit:
      # check for indivdual rolls 
      print(
        f"{Back.BLACK}Round Number: {Fore.GREEN}{round}{Fore.WHITE}, Player {player+1} rolled a {Fore.GREEN}{roll1}, {Fore.RED}{roll2}, {Fore.RED}{roll3}"
      )
      displayRoll(roll1, roll2, roll3, bunco, allSame, roll1_hit, roll2_hit, roll3_hit)
      #if roll one is hit, just color roll1 green and the rest red
      
    elif roll2_hit:
      print(
        f"{Back.BLACK}Round Number: {Fore.GREEN}{round}{Fore.WHITE}, Player {player+1} rolled a {Fore.RED}{roll1}, {Fore.GREEN}{roll2}, {Fore.RED}{roll3}"
      )
      #if roll two is hit, just color roll2 green and the rest red
      displayRoll(roll1, roll2, roll3, bunco, allSame, roll1_hit, roll2_hit, roll3_hit)
    elif roll3_hit:
      print(
        f"{Back.BLACK}Round Number: {Fore.GREEN}{round}{Fore.WHITE}, Player {player+1} rolled a {Fore.RED}{roll1}, {Fore.RED}{roll2}, {Fore.GREEN}{roll3}"
      )
      displayRoll(roll1, roll2, roll3, bunco, allSame, roll1_hit, roll2_hit, roll3_hit)
      #if roll three is hit, just color roll3 green and the rest red
  else:
    print(
      f"{Back.BLACK}Round Number: {Fore.RED}{round}{Fore.WHITE}, Player {player+1} rolled a {Fore.RED}{roll1}, {Fore.RED}{roll2}, {Fore.RED}{roll3}"
    )
    displayRoll(roll1, roll2, roll3, bunco, allSame, roll1_hit, roll2_hit, roll3_hit)
    #else all are red no hits
  
  print()
  # checks if player one or two scored then prints the total score in green and the net gain in green if the scored and in normal text and red net gain if they didn't
  if player1_scored:
    print(
      f'{Back.BLACK}{Fore.GREEN}Player 1 Total score: {player1_score} (+{player1_net_gain})'
    )
  else:
    print(
      f"{Back.BLACK}Player 1 Total score: {player1_score} {Fore.RED}(+ {player1_net_gain})"
    )
  if player2_scored:
    print(
      f"{Back.BLACK}{Fore.GREEN}Player 2 Total score: {player2_score} (+{player2_net_gain})"
    )
  else:
    print(
      f"{Back.BLACK}Player 2 Total score: {player2_score} {Fore.RED}(+{player2_net_gain})"
    )
  
  print()
  #reduntant but i wanted it to say, ' player gets to roll agian after displaying the total score.  
  if player1_scored:
    print(f"{Back.BLACK}{Fore.GREEN}Player 1 gets to roll agian!")
    print()
  if player2_scored:
    print(f"{Back.BLACK}{Fore.GREEN}Player 2 gets to roll agian!")
    print()

  
  
def simulateThreeRounds():
  #grabs globall varibles and normalizes them because simulate is called multiple times
  global player1_score
  global player2_score
  global player1_wins
  global player2_wins
  global player_turn
  player1_score = 0
  player2_score = 0
  player_turn = 0
  player1_wins = 0
  player2_wins = 0
  #simulates three rounds
  for i in range(1, 4):
    # as long as the scores no not exceed 21 the round continues
    while player1_score < 21 and player2_score < 21:
      turn(i, player_turn % 2)

    #checks to see who won and then adds it to there wins,and diplays it in bold text 
    if player1_score >= 21:
      player1_wins += 1
      print(f"{Back.BLACK}\033[1mPlayer 1 wins Round {i}.\033[0m ")
    elif player2_score >= 21:
      player2_wins += 1
      print(f"{Back.BLACK}\033[1mPlayer 2 wins Round {i}.\033[0m")
    #scores, and turn is rest for the next round and end of round message is displayed 
    player1_score = 0
    player2_score = 0
    player_turn = 0
    print(f"{Back.BLACK}\033[1mEnd of Round {i}.\033[0m")
    #as long the round is not 3 or the last round display a message telling the user to press any key to continue
    if i != 3:
      input(f"{Back.BLACK}Press any key to continue ... ")
      time.sleep(2)
      #time.sleep is like the scratch wait block

  print()
  #checks who won out of the three rounds
  if player1_wins > player2_wins:
    print(
      f"{Back.BLACK}{Fore.GREEN}Player 1 wins: {player1_wins}, {Fore.RED}Player 2 wins: {player2_wins}"
    )
    print(f"{Back.BLACK}{Fore.GREEN}PLAYER 1 WINS!")
  else:
    print(
      f"{Back.BLACK}{Fore.RED}Player 1 wins: {player1_wins}, {Fore.GREEN}Player 2 wins: {player2_wins}"
    )
    print(f"{Back.BLACK}{Fore.GREEN}PLAYER 2 WINS!")
  print()

#if the user does not know the rules
def showRules():
  print(f"{Back.BLACK}Bunco is a six round three-dice game that gives points based on the number of die matching the current round number (shown below)\n")
  print()
  print(f"""{Back.BLACK}ROUND NUMBER 6 | ⚅⚅⚅ | BUNCO ALL SAME AND MATCHES ROUND NUMBER | +21 POINTS\n
ROUND NUMBER 6 | ⚄⚄⚄ | ALL SAME BUT DOES NOT MATCH ROUND NUMBER | +5 POINTS\n
ROUND NUMBER 6 | ⚄⚅⚅ | TWO 6'S ONE 5 | +1 POINT FOR EACH MATCH\n
ROUND NUMBER 6 | ⚄⚄⚂ | NO MATCHES OR ALL SAME | +0 POINTS\n""")
  print(f"{Back.BLACK}If a player scores on a roll, he or she gets to roll until they don't score or until they reach at least 21 points.")
  print()
  print(f"{Back.BLACK} For futher information please vist {Fore.BLUE}https://en.wikipedia.org/wiki/Bunco")
  print(f"{Back.BLACK} Good Luck!")
  qoutes = ['A face on a lover with a fire in his heart, A man under cover, but you tore me apart', "Oh, I don't lose. People who bet on me to lose lose. And they lose big.", "100 percent of gamblers quit just when they're about to win.", "You know, you're half smart, Ocean."]
  print()
  #picks random qoute to display from Ocean's 13
  print(Back.BLACK + '“' + f"{random.choice(qoutes)}" + '”')
  print()

print(f"{Back.RED}                                          ")
#in case i need the title elsewhere
TITLE = f'''{Back.RED}{Fore.BLACK}██████╗░██╗░░░██╗███╗░░██╗░█████╗░░█████╗░
██╔══██╗██║░░░██║████╗░██║██╔══██╗██╔══██╗
██████╦╝██║░░░██║██╔██╗██║██║░░╚═╝██║░░██║
██╔══██╗██║░░░██║██║╚████║██║░░██╗██║░░██║
██████╦╝╚██████╔╝██║░╚███║╚█████╔╝╚█████╔╝
╚═════╝░░╚═════╝░╚═╝░░╚══╝░╚════╝░░╚════╝░'''
print(TITLE)
print(f"{Back.RED}                                          ")
print()
#user input asks if they want to exit, simulate, or read the rules
query = input(
  f"{Back.BLACK}\033[1mWould you like to simulate Bunco or read the rules?\nEnter 'rules' for rules and 'simulate' to simulate three rounds. To exit the game enter 'exit'.\033[0m "
)
print()

while query != 'exit':
  if query == 'simulate':
    #if user inputs simualte then simulate the three rounds
    simulateThreeRounds()
  if query == 'rules':
    #if the user inputs 'rules' display the rules of the game
    showRules()
  #keep asking until the user enters exit
  query = input(
  f"{Back.BLACK}\033[1mWould you like to stimulate Bunco or read the rules?\nEnter 'rules' for rules and 'simulate' to simulate three rounds. To exit the game enter 'exit'.\033[0m "
)
  print()

import random 
 
def play():
  user = input(" 'r' for Rock 'p' for Paper 's' for scissor : ")
  computer = random.choice(['r','p','s'])
  
  if user == computer:
    return "it/'s a Tie"
    
  if win(user, computer):
    return "You Won !"
  
  # if win(computer, user):   appernetly we dont need this line because if the upper two conditions are wrong it will automatically be right
  return " You lose !"
  
  
def win(player , oppnent):
  # r > s, s > p, p > r
  if (player == 'r' and oppnent == 's') or (player == 's' and oppnent == 'p') or (player == 'p' and oppnent == 'r'):
    return True

print(play())
  
  
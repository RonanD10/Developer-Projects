import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

guesses = []
word = random.choice(word_list)
characters = [l for l in word]
hidden = ['_' for l in word]
length = len(characters)
lives = 6 

print('Welcome to hangman!')
print(logo)

while lives > 0: 

  letter = input('Enter a letter: ')
  
  if letter in guesses:
    print('Letter already chosen!')
    continue
  guesses.append(letter)
  
  correct = 0 
  for i in range(length):
    if letter == characters[i]:
      hidden[i] = letter
      correct += 1
  
  if correct == 0:
    lives -= 1
    print('Incorrect! Lives remaining: {}'.format(lives))
    print(stages[lives])
  
  else:
    display = ''
    for l in hidden:
      display += l + ' ' 
    print(display)
  
  if "_" not in hidden:
    print('Congratulations! You win. The word is {}'.format(word))


print('No lives remaining! Please try again.')
  
  
    
    
    
    
  
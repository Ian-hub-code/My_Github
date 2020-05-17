# This is my edited version of pygame, with 3 enemies and a prize that wins you the game!

import pygame # Game Library for specific functions.
import random # Importing function to generate random numbers. 

# Initializing pygame modules to start.

pygame.init() 

# Setting the screen width and height

screen_width = 1440
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen with the provided width and height above
pygame.display.set_caption("Ian's Pygame!")

# This creates the player, enemies and prize and gives it the images found in the folder 

player = pygame.image.load("image.png")
enemy = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("enemy.png") 
enemy3 = pygame.image.load("enemy.png") 
prize = pygame.image.load("prize.jpg")
prize = pygame.transform.scale(prize, (100, 50)) # Making the prize smaller so that it is not too easy to get to it

# Getting the width and height of the images in order to do boundary detection 

image_height = player.get_height()  # Player height
image_width = player.get_width()    # Player width
enemy_height = enemy.get_height()   # Enemy height  
enemy_width = enemy.get_width()     # Enemy width
enemy2_height = enemy2.get_height() # Enemy 2 height
enemy2_width = enemy2.get_width()   # Enemy 2 width
enemy3_height = enemy3.get_height() # Enemy 3 height
enemy3_width = enemy3.get_width()   # Enemy 3 width
prize_height = prize.get_height() # Prize height
prize_width = prize.get_width()   # Prize width

# Printing the sizes of the images loaded into the game

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))
print("This is the height of the enemy image: " +str(enemy_height))
print("This is the width of the enemy image: " +str(enemy_width))
print("This is the height of the enemy2 image: " +str(enemy2_height))   
print("This is the width of the enemy2 image: " +str(enemy2_width))     
print("This is the height of the enemy3 image: " +str(enemy3_height))   
print("This is the width of the enemy3 image: " +str(enemy3_width))
print("This is the height of the prize image: " +str(prize_height))   
print("This is the width of the prize image: " +str(prize_width)) 

# Storing the positions of the player, enemies so that it can be changed throughout the game.

playerXPosition = 720
playerYPosition = 450

# The prize position is randomly generated but fixed once generated for the duration of the game.

prizeXPosition = 30
prizeYPosition = 750

#prizeXPosition = random.randint(0,screen_width - image_width - prize_width)
#prizeYPosition = random.randint(0,screen_height - image_height - prize_height)

# Making the enemy start off screen and at a random y position, this enemy will come from the right of the player.

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)

# Making the second enemy also start off at a random y position, this enemy will come from the left of the player.

enemy2XPosition =  0                                                
enemy2YPosition =  random.randint(0, screen_height - enemy_height)

# Making the third enemy start off at a random x position, this enemy will be coming from above the player.

enemy3XPosition =  random.randint(0, screen_width - enemy3_width)   
enemy3YPosition =  0

# This checks if the up, down, left or right key is pressed.
# Right now they are not so they are set to the boolean value of False 

keyUp= False
keyDown = False
keyLeft = False    
keyRight = False   

# This is the game loop.
# The logic runs over and over again.
# The screen is refreshed to provide a real time gameplay experience

while 1: ### This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting) 1 represent a True booelan value, 0 represent a False boolean value.  

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied.
    screen.blit(enemy, (enemyXPosition, enemyYPosition)) # This draws the enemy image to the screen at the postion specfied.
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition)) # This draws the enemy2 image to the screen at the postion specfied.
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition)) # This draws the enemy3 image to the screen at the postion specfied.
    screen.blit(prize, (prizeXPosition, prizeYPosition)) # This draws the prize image to the screen at the postion specfied.

        
    pygame.display.flip()# This updates the screen. 
    
    # Loops through events in the game
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True

            if event.key == pygame.K_LEFT:  # LEFT
                keyLeft = True              
            if event.key == pygame.K_RIGHT: #RIGHT
                keyRight = True             
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:    # UP
                keyUp = False
            if event.key == pygame.K_DOWN:  # DOWN
                keyDown = False
            if event.key == pygame.K_LEFT:  # LEFT
                keyLeft = False            
            if event.key == pygame.K_RIGHT: # RIGHT
                keyRight = False          
            
    # After the for loop above hte key values are set, next the keys are checked and the player is moved according to the keys pressed   
    # The player position is changed by adding or subtracting from the x and y axis range
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:  # This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    if keyRight == True:
        if playerXPosition > 0 and playerXPosition < screen_width + image_width :   # This makes sure that the user does not move the player beyond the window in X axis (RIGHT)
            playerXPosition += 1

    if keyLeft == True:
        if playerXPosition > 0 and playerXPosition < screen_width + image_width:    # This makes sure that the user does not move the player beyond the window in X axis (LEFT)
            playerXPosition -= 1
            
    # The next steps is to check for collision of the enemy with the player and also to check the collision of the player and the prize
    # To do this we need bounding boxes around the images of the player, enemies and the prize  
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position, this makes sure that the box stays around the image through the game 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    # Bounding box for enemy 2:
    
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition
    
    # Bounding box for enemy 3:
    
    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    # Bounding box for the prize:

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemyBox) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
    
        # Display losing status to the user: 
        
        print("You collided with an enemy, GAME OVER!")
        game_over = pygame.image.load("game_over.jpg")
        screen.blit(game_over, (360, 225))
        pygame.display.update()
        pygame.quit()
        exit(0)
     
    elif playerBox.colliderect(prizeBox):

        print("Prize found, you win!")
        winner = pygame.image.load("great_success.png")
        screen.blit(winner, (360, 225))
        pygame.display.update()
        pygame.quit()
            
        # Quite game and exit window: 
         
        exit(0)
        
        
    # If the enemy is off the screen the user wins the game:
    
    if enemyXPosition < 0 - enemy_width or enemy2XPosition > screen_width+ enemy2_width or enemy3YPosition > screen_width + image_width:
    
        # Display wining status to the user: 
        
        print("You evaded the enemies, you win!")
        sneak = pygame.image.load("sneak.jpg")
        screen.blit(sneak, (360, 225))
        pygame.display.update()
        pygame.quit()
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
      
    # Make enemy approach the player.
    
    enemyXPosition -= 0.15
    enemy2XPosition += 0.15
    enemy3YPosition += 0.15

 # The game loop logic ends here.
  

import pygame
pygame.init()
white = (255,255,255)
black = (0,0,0)
(width, height) = (600, 620)
screen = pygame.display.set_mode((width, height))
list_of_selected_boxes = []
list_of_player_choices = []
player_turn = 0
screen.fill(white)

def draw_lines():
  pygame.draw.line(screen,black,(0,200),(600,200))
  pygame.draw.line(screen,black,(0,400),(600,400))
  pygame.draw.line(screen,black,(200,0),(200,600))
  pygame.draw.line(screen,black,(400,0),(400,600))
draw_lines()

def draw_shape(position):
  global player_turn
  if(player_turn%2==0):
    pygame.draw.circle(screen, black, position, 40)
  else:
    pygame.draw.circle(screen, (255,0,0), position, 40)
  player_turn += 1

def draw_text():
  myfont = pygame.font.SysFont("monospace", 16)
  scoretext = myfont.render("TIC-TAC-TOE", 1, (0,0,0))
  screen.blit(scoretext, (250, 600))
draw_text()

def winner():
  for i in range(0,2):
    if (1,i) in list_of_player_choices:
      if (2,i) in list_of_player_choices:
        if (3,i) in list_of_player_choices:
          return i
    if (4,i) in list_of_player_choices:
      if (5,i) in list_of_player_choices:
        if (6,i) in list_of_player_choices:
          return i
    if (7,i) in list_of_player_choices:
      if (8,i) in list_of_player_choices:
        if (9,i) in list_of_player_choices:
          return i
    if (1,i) in list_of_player_choices:
      if (4,i) in list_of_player_choices:
        if (7,i) in list_of_player_choices:
          return i
    if (2,i) in list_of_player_choices:
      if (5,i) in list_of_player_choices:
        if (8,i) in list_of_player_choices:
          return i
    if (3,i) in list_of_player_choices:
      if (6,i) in list_of_player_choices:
        if (9,i) in list_of_player_choices:
          return i
    if (1,i) in list_of_player_choices:
      if (5,i) in list_of_player_choices:
        if (9,i) in list_of_player_choices:
          return i   
    if (3,i) in list_of_player_choices:
      if (5,i) in list_of_player_choices:
        if (7,i) in list_of_player_choices:
          return i
running = True
while running:
  pygame.display.flip()
  pos = pygame.mouse.get_pos()

  if pygame.mouse.get_pressed() == (1,0,0):
    if((pos[0]>0 and pos[0]<200)and(pos[1]>0 and pos[1]<200)):
      if(1 not in list_of_selected_boxes):
        list_of_selected_boxes.append(1)
        list_of_player_choices.append((1,player_turn%2))
        draw_shape((100,100))
        print(1)
    elif((pos[0]>200 and pos[0]<400)and(pos[1]>0 and pos[1]<200)):
      if(2 not in list_of_selected_boxes):
        list_of_selected_boxes.append(2)
        list_of_player_choices.append((2,player_turn%2))
        draw_shape((300,100))
        print(2)
    elif((pos[0]>400 and pos[0]<600)and(pos[1]>0 and pos[1]<200)):
      if(3 not in list_of_selected_boxes):
        list_of_selected_boxes.append(3)
        list_of_player_choices.append((3,player_turn%2))
        draw_shape((500,100))
        print(3)
    elif((pos[0]>0 and pos[0]<200)and(pos[1]>200 and pos[1]<400)):
      if(4 not in list_of_selected_boxes):
        list_of_selected_boxes.append(4)
        list_of_player_choices.append((4,player_turn%2))
        draw_shape((100,300))
        print(4)
    elif((pos[0]>200 and pos[0]<400)and(pos[1]>200 and pos[1]<400)):
      if(5 not in list_of_selected_boxes):
        list_of_selected_boxes.append(5)
        list_of_player_choices.append((5,player_turn%2))
        draw_shape((300,300))
        print(5)
    elif((pos[0]>400 and pos[0]<600)and(pos[1]>200 and pos[1]<400)):
      if(6 not in list_of_selected_boxes):
        list_of_selected_boxes.append(6)
        list_of_player_choices.append((6,player_turn%2))
        draw_shape((500,300))
        print(6)
    elif((pos[0]>0 and pos[0]<200)and(pos[1]>400 and pos[1]<600)):
      if(7 not in list_of_selected_boxes):
        list_of_selected_boxes.append(7)
        list_of_player_choices.append((7,player_turn%2))
        draw_shape((100,500))
        print(7)
    elif((pos[0]>200 and pos[0]<400)and(pos[1]>400 and pos[1]<600)):
      if(8 not in list_of_selected_boxes):
        list_of_selected_boxes.append(8)
        list_of_player_choices.append((8,player_turn%2))
        draw_shape((300,500))
        print(8)
    elif((pos[0]>400 and pos[0]<600)and(pos[1]>400 and pos[1]<600)):
      if(9 not in list_of_selected_boxes):
        list_of_selected_boxes.append(9)
        list_of_player_choices.append((9,player_turn%2))
        draw_shape((500,500))
        print(9)
  win = winner()
  if win != None:
    print(win+1)
    if win == 0:screen.fill((0,0,0))
    else:screen.fill((255,0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print(list_of_player_choices)
      
      running = False
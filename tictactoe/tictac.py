import pygame, random, time

class Square():

    def __init__(self, img, pos, cube, list_x, list_o):
        self.status = "white"
        self.img = img
        self.pos = pos
        self.coordinates = cube
        self.list_x = list_x
        self.list_o = list_o



    def draw(self, window):

        dis_rect = self.img.get_rect(topleft=self.pos)
        window.blit(self.img, dis_rect)

    def change_pic(self, img, status):
        self.img = img
        self.status = status

    def work(self, event, SQUAREIMGX, SQUAREIMGO, x, y, player1, player2):
        if self.img.get_rect(topleft = self.pos).collidepoint(x, y):
            if self.status == 'white':
                if player1:
                    self.change_pic(SQUAREIMGX, "x")
                    self.list_x.append([self.coordinates, self.status])

                else:
                    self.change_pic(SQUAREIMGO, "o")
                    self.list_o.append([self.coordinates, self.status])



class Button():

    def __init__(self, img, pos, window):
        self.img = img
        self.pos = pos
        self.font = pygame.font.SysFont("comicssans", 50)
        self.label = self.font.render(f"Turn of X", 1, (255, 0, 0))
        window.blit(self.img, self.pos)
        window.blit(self.label, (130, 520))


    def draw(self, window, text):
        window.blit(self.img, self.pos)
        self.label = self.font.render(text, 1, (255, 0, 0))
        window.blit(self.label, (130, 520))




def run():
    pygame.init()
    WIDTH, HEIGHT = 460, 750
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("TIcTacToe")
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    list_x = []
    list_o = []


    CURRENT_DIRECOTRY = 'C:\\Users\\azimc\\IdeaProjects\\Atomprojects\\tictactoe'
    SQUAREIMG = pygame.image.load(CURRENT_DIRECOTRY + "\\pics\\white.png").convert()
    SQUAREIMGX = pygame.image.load(CURRENT_DIRECOTRY + "\\pics\\x.png").convert()
    SQUAREIMGO = pygame.image.load(CURRENT_DIRECOTRY + "\\pics\\o.png").convert()

    BUTTON = pygame.image.load(CURRENT_DIRECOTRY + "\\pics\\button.png")

    SQUARE1 = Square(SQUAREIMG, (10,10), (0, 0), list_x, list_o)
    SQUARE2 = Square(SQUAREIMG, (160,10), (0, 1), list_x, list_o)
    SQUARE3 = Square(SQUAREIMG, (310,10), (0, 2), list_x, list_o)
    SQUARE4 = Square(SQUAREIMG, (10,160), (1, 0), list_x, list_o)
    SQUARE5 = Square(SQUAREIMG, (160,160),(1, 1), list_x, list_o)
    SQUARE6 = Square(SQUAREIMG, (310,160), (1, 2), list_x, list_o)
    SQUARE7 = Square(SQUAREIMG, (10,310), (2, 0), list_x, list_o)
    SQUARE8 = Square(SQUAREIMG, (160,310), (2, 1), list_x, list_o)
    SQUARE9 = Square(SQUAREIMG, (310,310), (2, 2), list_x, list_o)
    BUTTON1 = Button(BUTTON, (10, 470), WIN)
    player1 = True
    player2 = False
    game = True


    while run:
        clock.tick(FPS) # Creates 60 FPS per second
        SQUARE1.draw(WIN)
        SQUARE2.draw(WIN)
        SQUARE3.draw(WIN)
        SQUARE4.draw(WIN)
        SQUARE5.draw(WIN)
        SQUARE6.draw(WIN)
        SQUARE7.draw(WIN)
        SQUARE8.draw(WIN)
        SQUARE9.draw(WIN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if game:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                    x, y = event.pos

                    SQUARE1.work(event, SQUAREIMGX, SQUAREIMGO, x, y, player1, player2)
                    SQUARE2.work(event, SQUAREIMGX, SQUAREIMGO, x, y, player1, player2)
                    SQUARE3.work(event, SQUAREIMGX, SQUAREIMGO, x, y, player1, player2)
                    SQUARE4.work(event, SQUAREIMGX, SQUAREIMGO, x, y, player1, player2)
                    SQUARE5.work(event, SQUAREIMGX, SQUAREIMGO, x, y, player1, player2)
                    SQUARE6.work(event, SQUAREIMGX, SQUAREIMGO, x, y, player1, player2)
                    SQUARE7.work(event, SQUAREIMGX, SQUAREIMGO, x, y, player1, player2)
                    SQUARE8.work(event, SQUAREIMGX, SQUAREIMGO, x, y, player1, player2)
                    SQUARE9.work(event, SQUAREIMGX, SQUAREIMGO, x, y, player1, player2)

                    if player1:
                        player1 = False
                        player2 = True
                        BUTTON1.draw(WIN, 'Turn of O')
                    else:
                        player1 = True
                        player2 = False
                        BUTTON1.draw(WIN, 'Turn of X')

                    print("----------------")
                    print(list_x)
                    print(list_o)

                    try:
                        if list_x[0][0][1] % 3 == list_x[1][0][1] % 3== list_x[2][0][1] % 3:
                            BUTTON1.draw(WIN, 'Victory of X')
                            game = False

                        if list_x[0][0][0] % 3 == list_x[1][0][0] % 3== list_x[2][0][0] % 3:
                            BUTTON1.draw(WIN, 'Victory of X')
                            game = False

                        count_left = 0
                        for number in range(len(list_x)):
                            if (0, 0) in list_x[number]:
                                count_left += 1
                            if (1, 1) in list_x[number]:
                                count_left += 1
                            if (2, 2) in list_x[number]:
                                count_left += 1


                        if count_left == 3:
                            BUTTON1.draw(WIN, 'Victory of X')
                            game = False


                        count_right = 0
                        for number in range(len(list_x)):
                            if (0, 2) in list_x[number]:
                                count_right += 1
                            if (1, 1) in list_x[number]:
                                count_right += 1
                            if (2, 0) in list_x[number]:
                                count_right += 1


                        if count_right == 3:
                            BUTTON1.draw(WIN, 'Victory of X')
                            game = False
                    except:
                        pass

                    try:
                        if list_o[0][0][1] % 3 == list_o[1][0][1] % 3== list_o[2][0][1] % 3:
                            BUTTON1.draw(WIN, 'Victory of O')
                            game = False

                        if list_o[0][0][0] % 3 == list_o[1][0][0] % 3== list_o[2][0][0] % 3:
                            BUTTON1.draw(WIN, 'Victory of O')
                            game = False

                        count_up = 0
                        for number in range(len(list_o)):
                            if (0, 0) in list_o[number]:
                                count_up += 1
                            if (1, 1) in list_o[number]:
                                count_up += 1
                            if (2, 2) in list_o[number]:
                                count_up += 1


                        if count_up == 3:
                            BUTTON1.draw(WIN, 'Victory of O')
                            game = False


                        count_down = 0
                        for number in range(len(list_o)):
                            if (0, 2) in list_o[number]:
                                count_down += 1
                            if (1, 1) in list_o[number]:
                                count_down += 1
                            if (2, 0) in list_o[number]:
                                count_down += 1



                        if count_down == 3:
                            BUTTON1.draw(WIN, 'Victory of O')
                            game = False
                    except:
                        pass


            pygame.display.update()

run()

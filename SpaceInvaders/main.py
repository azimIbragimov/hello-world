import pygame
import os, time, random

"""
The following lines set up objects/images
"""
pygame.font.init()
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space shooter")

#TODO
CURRENT_DIRECOTRY = 'C:\\Users\\azimc\\IdeaProjects\\Atomprojects\\spaceshooters'
# CURRENT_DIRECOTRY = os.getcwd()
print(CURRENT_DIRECOTRY)

# load images (ships, lasers, background)
RED_SPACE_SHIP = pygame.image.load(CURRENT_DIRECOTRY + '\\assets\\pixel_ship_red_small.png')
GREEN_SPACE_SHIP = pygame.image.load(CURRENT_DIRECOTRY + '\\assets\\pixel_ship_green_small.png')
BLUE_SPACE_SHIP = pygame.image.load(CURRENT_DIRECOTRY + '\\assets\\pixel_ship_blue_small.png')
YELLOW_SPACE_SHIP = pygame.image.load(CURRENT_DIRECOTRY + '\\assets\\pixel_ship_yellow.png')
RED_LASER = pygame.image.load(CURRENT_DIRECOTRY + '\\assets\\pixel_laser_red.png')
GREEN_LASER = pygame.image.load(CURRENT_DIRECOTRY + '\\assets\\pixel_laser_green.png')
BLUE_LASER = pygame.image.load(CURRENT_DIRECOTRY + '\\assets\\pixel_laser_blue.png')
YELLOW_LASER = pygame.image.load(CURRENT_DIRECOTRY + '\\assets\\pixel_laser_yellow.png')
BG = pygame.transform.scale(pygame.image.load(CURRENT_DIRECOTRY + '\\assets\\background-black.png'), (WIDTH, HEIGHT))

class Laser:
    """
    Creates lasers for ships
    """
    def __init__(self, x, y, img):
        """
        Parameters:
        x --- x coordinate
        y --- y coordinate
        img - png image of laser
        """
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        """ Moves lasers down"""
        self.y += vel

    def off_screen(self, height):
        return not (self.y <=  height and self.y >= 0)

    def collision(self, obj):
        return collide(obj, self)


class Ship:
    """
    Class that desribes behavoir of any ship
    Paramteres:
    x --- x cordinates (int)
    y --- y coordinates (int)
    health --- health of the ship (int)
    """
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.img = None # The image will be uploaded later
        self.laser_img = None # The image will be uploaded later
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        """
        Draws the ship itself
        Paramteres:
        window --- name  of the display window (pygame.display object)
        """
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(objs):
                objs.health -= 10
                self.lasers.remove(laser)


    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        """
        Gets width of the ship
        """
        return self.ship_img.get_width()

    def get_height(self):
        """
        Gets height of the ship
        """
        return self.ship_img.get_height()


class Player(Ship):
    """
    Child class of Ship. This ship is controlled by the player
    """

    def __init__(self,x,y,health=100):
        """Inheritance from the Ship class"""
        super().__init__(x,y,health)
        self.ship_img = YELLOW_SPACE_SHIP   # sets up the ship image
        self.laser_img = YELLOW_LASER   # sets up the laser image
        self.mask = pygame.mask.from_surface(self.ship_img) # creates a cool colision effect
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))

class Enemy(Ship):
    """
    Child class of Ship. The user is supposed to shoot those ships down
    """
    # status of ships with certain colors
    COLOR_MAP = {
    'red': (RED_SPACE_SHIP, RED_LASER),
    'green': (GREEN_SPACE_SHIP, GREEN_LASER),
    'blue': (BLUE_SPACE_SHIP, BLUE_LASER),
    }

    def __init__(self, x, y, color, health = 100):
        """Inheritance"""
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        """
        Makes the enemies go down.
        Paramteres:
        vel - velocity of the ships (int)
        """
        self.y += vel

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None



def main():
    """
    Runs the game
    """
    # Stats of the player
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    level = 0
    lives = 5
    player_vel =5
    laser_vel=4
    main_font = pygame.font.SysFont("comicssans", 50)
    lost_font = pygame.font.SysFont("comicssans", 70)


    # Stats of enemies
    enemies = []
    wave_length = 0
    enemy_vel=1

    player = Player(300, 650)

    lost = False
    lost_count = 0


    def redraw_window():
        """Creates objects on the window"""
        WIN.blit(BG, (0, 0))    # Displays BG on the screen
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 0, 0))  # creates text
        level_label = main_font.render(f"Level: {level}", 1, (255, 0, 0))
        WIN.blit(lives_label, (10, 10)) # places the text
        WIN.blit(level_label, (WIDTH-level_label.get_width()-10, 10))   # places the text

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You lost", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH//2 - lost_label.get_width()//2, 350))


        pygame.display.update() # updates the screen

    while run:
        clock.tick(FPS) # Creates 60 FPS per second
        redraw_window()


        if len(enemies) == 0:
            level += 1
            wave_length += 5
            print(player.health)
            if lives <= 0 or player.health <= 0:
                lost = True
                lost_count += 1
                print(lost)

            if lost:
                if lost_count > FPS * 3:
                    run = False
                else:
                    continue


            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100), random.choice(['red', 'green', 'blue']))
                print(f"New enemy: {i}")
                enemies.append(enemy)

        """Key pressing"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()   # Returns a dictionary of all pressed buttons
        if keys[pygame.K_a] and player.x + player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width()< WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y + player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height()< HEIGHT:  # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)

            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)




            player.move_lasers(-laser_vel, enemies)


main()

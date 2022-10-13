from pygame import *
from enemy import *
from plane_sprites import *
from background import *
from hero import *
from score import *
from pause import *
from bullet import *

class PlaneGame(object):
    pygame.init()
    pygame.mixer.init()
    def __init__(self):
        
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.delay = 100
        self.switch = True
        self.bomb_pic = Bullet2()
        pygame.mixer.music.load("sounds/bgm.ogg")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        
        self.boom_sound = pygame.mixer.Sound("sounds/boom.wav")
        self.boom_sound.set_volume(0.6)

        self.e1_destory_index = 0
        self.e2_destory_index = 0
        self.e3_destory_index = 0
        self.my_destory_index = 0

        self.__create_sprites()
        self.pause_font = pygame.font.SysFont("arial", 50)
        self.bomb_num = pygame.font.SysFont("arial", 24)
        self.game_over = pygame.font.SysFont("arial", 50)
        pygame.time.set_timer(CREATE_SMALL_ENEMY_EVENT, 1000)
        pygame.time.set_timer(CREATE_MID_ENEMY_EVENT, 2000)
        pygame.time.set_timer(CREATE_LARGE_ENEMY_EVENT, 5000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 150)
        pygame.time.set_timer(RELOAD_BOMB_EVENT, 3000)

    def start_game(self):
        # Main game loop
        while True:
            # set refresh rate
            self.clock.tick(FRAME_RATE)
            # handle event
            self.__event_handler()
            # check collision
            self.__check_collide()
            # update sprites
            self.__update_sprites()
            # display everyting
            pygame.display.update()
            # print(self.delay)
            # For animation
            self.delay -= 1
            if self.delay == 0:
                self.delay = 100

    def __create_sprites(self):
        
        bg1 = Background()
        bg2 = Background(is_alt=True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        self.small_enemy_group = pygame.sprite.Group()
        self.mid_enemy_group = pygame.sprite.Group()
        self.large_enemy_group = pygame.sprite.Group()
        self.enemies_group = pygame.sprite.Group()

        self.hero = Hero()

        self.score_Score = Score()

        self.pause = Pause()


    
    # collect all the event
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.pause.rect.collidepoint(event.pos):
                    self.pause.paused = not self.pause.paused

            elif event.type == MOUSEMOTION:
                if self.pause.rect.collidepoint(event.pos):
                    if self.pause.paused:
                        self.pause.image = self.pause.resume_pressed
                    else:
                        self.pause.image = self.pause.pause_pressed
                else:
                    if self.pause.paused:
                        self.pause.image = self.pause.resume
                    else:
                        self.pause.image = self.pause.pause

            if not self.pause.paused and not self.hero.stop:      

                if event.type == CREATE_SMALL_ENEMY_EVENT:
                    enemy = SmallEnemy()
                    self.small_enemy_group.add(enemy)
                    self.enemies_group.add(enemy)
                elif event.type == CREATE_MID_ENEMY_EVENT:
                    enemy = MidEnemy()
                    self.mid_enemy_group.add(enemy)
                    self.enemies_group.add(enemy)
                elif event.type == CREATE_LARGE_ENEMY_EVENT:
                    enemy = LargeEnemy()
                    self.large_enemy_group.add(enemy)
                    self.enemies_group.add(enemy)
                elif event.type == RELOAD_BOMB_EVENT and self.hero.bomb_num < 3:
                    self.hero.bomb_num += 1
                elif event.type == HERO_FIRE_EVENT:
                    self.hero.fire()
                elif event.type == KEYDOWN:
                    if event.key == K_TAB:
                        if self.hero.bomb_num > 0:
                            self.hero.bomb()
                        
        if not self.pause.paused:
            self.hero.move()
        

    def __update_sprites(self):
        
        
        self.back_group.draw(self.screen)
        if not self.pause.paused and not self.hero.stop :
            self.back_group.update()
            # enemy
            for enemy in self.large_enemy_group:
                if not enemy.die:
                    if enemy.life > 6:
                        self.screen.blit(enemy.image, enemy.rect)
                    else:
                        self.screen.blit(enemy.image_hit, enemy.rect)

                    enemy.update()

                    # draw the health power
                    pygame.draw.line(self.screen, BLACK, (enemy.rect.left, enemy.rect.top - 5), (enemy.rect.right, enemy.rect.top - 5), 2)

                    get_hit = (LargeEnemy.life -enemy.life) / LargeEnemy.life

                    pygame.draw.line(self.screen, GREEN, (enemy.rect.left, enemy.rect.top - 5), (enemy.rect.right - (enemy.rect.right - enemy.rect.left) * get_hit, enemy.rect.top - 5), 2)

                else:
                    if not self.delay % 5:
                        self.screen.blit(enemy.destory_images[self.e3_destory_index], enemy.rect)
                        self.e3_destory_index = (self.e3_destory_index + 1) % 6
                        if self.e3_destory_index == 0:
                            enemy.kill()
                            self.score_Score.score += 10000

            for enemy in self.mid_enemy_group:
                if not enemy.die:
                    if enemy.life > 3:
                        self.screen.blit(enemy.image, enemy.rect)
                    else:
                        self.screen.blit(enemy.image_hit, enemy.rect)
                    
                    enemy.update()

                    # draw the health power
                    pygame.draw.line(self.screen, BLACK, (enemy.rect.left, enemy.rect.top - 5), (enemy.rect.right, enemy.rect.top - 5), 2)

                    get_hit = (MidEnemy.life -enemy.life) / MidEnemy.life

                    pygame.draw.line(self.screen, GREEN, (enemy.rect.left, enemy.rect.top - 5), (enemy.rect.right - (enemy.rect.right - enemy.rect.left) * get_hit, enemy.rect.top - 5), 2)

                else:
                    if not self.delay % 5:
                        self.screen.blit(enemy.destory_images[self.e2_destory_index], enemy.rect)
                        self.e2_destory_index = (self.e2_destory_index + 1) % 4
                        if self.e2_destory_index == 0:
                            enemy.kill()
                            self.score_Score.score += 5000
            
            for enemy in self.small_enemy_group:
                if not enemy.die:
                    self.screen.blit(enemy.image, enemy.rect)
                    enemy.update()
                else:
                    if not self.delay % 5:
                        self.screen.blit(enemy.destory_images[self.e1_destory_index], enemy.rect)
                        self.e1_destory_index = (self.e1_destory_index + 1) % 4
                        if self.e1_destory_index == 0:
                            enemy.kill()
                            self.score_Score.score += 1000

            # Bullet
            self.hero.bullet_group.update()
            self.hero.bullet_group.draw(self.screen)

            # Hero
            if not self.hero.die:
                if self.switch:
                    self.screen.blit(self.hero.image, self.hero.rect)
                else:
                    self.screen.blit(self.hero.image2, self.hero.rect)
                # Switch the image 0.25 s once
                if not (self.delay % 5):
                    self.switch = not self.switch

                self.hero.update()
            else:
                if not self.delay % 5:
                    if not self.hero.stop:
                        self.screen.blit(self.hero.destory_images[self.my_destory_index], self.hero.rect)
                        self.my_destory_index = (self.my_destory_index + 1) % 4
                    if self.my_destory_index == 0:
                        self.hero.stop = True
                        pygame.mixer.music.stop()
                        pygame.mixer.stop()
                        pygame.time.set_timer(CREATE_SMALL_ENEMY_EVENT, 0)
                        pygame.time.set_timer(CREATE_MID_ENEMY_EVENT, 0)
                        pygame.time.set_timer(CREATE_LARGE_ENEMY_EVENT, 0)
                        pygame.time.set_timer(HERO_FIRE_EVENT, 0)
                        pygame.time.set_timer(RELOAD_BOMB_EVENT, 0)
                        

        if self.hero.stop:
            self.end = self.game_over.render("Game Over", True, BLACK)
            self.screen.blit(self.end, (SCREEN_RECT.centerx - 100, SCREEN_RECT.centery - 50))

        self.screen.blit(self.bomb_pic.image, (SCREEN_RECT.left + 10, SCREEN_RECT.bottom - 60))
        self.bomb_text = self.bomb_num.render(" x " + str(self.hero.bomb_num), True, BLACK)
        self.screen.blit(self.bomb_text, (SCREEN_RECT.left + 80, SCREEN_RECT.bottom - 40))

        self.score_board = self.score_Score.font.render("Score: " + str(self.score_Score.score), True, BLACK)  
        self.screen.blit(self.score_board, self.score_Score.position)

        self.screen.blit(self.pause.image, self.pause.rect)

        if self.pause.paused:
            pause_text = self.pause_font.render("PAUSE", True, BLACK)
            self.screen.blit(pause_text, (SCREEN_RECT.centerx - 70, SCREEN_RECT.centery - 50))


        

    def __check_collide(self):
        died_enemy = pygame.sprite.groupcollide(self.hero.bullet_group, self.enemies_group, True, False, pygame.sprite.collide_mask)
        if died_enemy:
            for bullet, enemy in died_enemy.items():
                if type(bullet) == type(Bullet1()):
                    enemy[0].life -= bullet.damage
                    if enemy[0].life <= 0:
                        enemy[0].die = True
                else:
                    for enemy in self.enemies_group:
                        self.boom_sound.play()
                        if enemy.rect.top <= bullet.rect.top:
                            enemy.life -= bullet.damage
                            if enemy.life <= 0:
                                enemy.die = True
            

        crash = pygame.sprite.spritecollide(self.hero, self.enemies_group, False, pygame.sprite.collide_mask)
        if crash:
            self.hero.die = True
            for enemy in crash:
                enemy.die = True
    
    @staticmethod
    def __game_over():
        pygame.quit()
        exit()
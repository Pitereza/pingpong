from pygame import *
display.set_caption("Shooter")
window = display.set_mode((700, 500))
background = transform.scale(image.load("3.jpg"), (700, 500))
s1 = 0
s2 = 0
font.init()
font = font.SysFont("Arial", 40)
l1 = font.render("Player 1 lose", True,(255,0,0))
l2 = font.render("Player 2 lose", True,(0,0,255))
class GameSprite(sprite.Sprite):
#конструктор класса
  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      #вызываем конструктор класса (Sprite):
      sprite.Sprite.__init__(self)
      #каждый спрайт должен хранить свойство image - изображение
      self.image = transform.scale(image.load(player_image), (size_x, size_y))
      self.speed = player_speed
      #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
      
#метод, отрисовывающий героя на окне
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
  #метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 0:
           self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < 400:
           self.rect.y+= self.speed
    def ret(self):
        keys = key.get_pressed()
        if keys[K_j] and self.rect.y > 0:
           self.rect.y -= self.speed
        if keys[K_l] and self.rect.y < 400:
           self.rect.y += self.speed
class ball(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_b]:
            self.rect.y = 190
            self.rect.x = 300
speed_x = 1
speed_y = 1        
r1 = Player("6.png", 0, 190, 100, 100, 1 )
r2 = Player("5.png", 580, 190, 150, 150, 1 )
b = ball("7.png",300,190,100, 100, 1  )
run = True
finish = False
while run:
   #событие нажатия на кнопку “Закрыть”
    for e in event.get():
       if e.type == QUIT:
           run = False

    if not finish:
       #обновляем фон
        window.blit(background,(0,0))
        r1.update()
        r1.reset()
        r2.ret()
        r2.reset()
        b.update()
        b.reset()
        
        b.rect.x += speed_x
        b.rect.y += speed_y
        if b.rect.y < 0 or b.rect.y > 450:
            speed_y *= -1
        if b.rect.x < 0:
            s2 = s2 + 1
            b.rect.y = 190
            b.rect.x = 300
        if b.rect.x > 700:
            s1 = s1 + 1 
            b.rect.y = 190
            b.rect.x = 300
        if sprite.collide_rect(r1, b) or sprite.collide_rect(r2, b):
            speed_x *= -1
        
        if s2 > 9:
            finish = True
            window.blit(l1,(200,200))
            
        if s1 > 9:
            finish = True
            window.blit(l2,(200,200))
            b.rect.y = 190
            b.rect.x = 300
        s1s = font.render("Счет: " + str(s1), 1, (255, 0, 0))
        s2s = font.render("Счет: " + str(s2), 1, (0, 0, 255))
        window.blit(s1s,(5,10))
        window.blit(s2s,(550,450))
        display.update()
from pygame import *
display.set_caption("Shooter")
window = display.set_mode((700, 500))
background = transform.scale(image.load("3.jpg"), (700, 500))

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
        if sprite.collide_rect(r1, b) or sprite.collide_rect(r2, b):
            speed_x *= -1
        

        display.update()
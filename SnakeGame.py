import random
import arcade


class Fruit(arcade.Sprite):
    def __init__(self , game):
        super().__init__()
        self.width=30
        self.height=30
        self.center_x=random.randint(10,game.width-10)
        self.center_y=random.randint(10,game.height-10)
class Pear(Fruit):
    def __init__(self):
        super().__init__("my-project\session15\pear.png")


class Apple(Fruit):
    def __init__(self):
        super().__init__("my-project\session15\Apple.png")
        

class Bomb(Fruit):
    def __init__(self):
        super().__init__("💩")



class Snake(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width=30
        self.height=30
        self.center_x= game.width //2
        self.center_y= game.height//2
        self.color=arcade.color.BROWN
        self.change_x=0
        self.change_y=0
        self.speed=2
        self.score=0
        self.body=[]

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color) 
        for part in self.body:
            arcade.draw_rectangle_filled(part['x'] , part['y'] , self.width , self.height, arcade.color.YELLOW)
        

    def move(self):
        self.body.append({'x': self.center_x,'y':self.center_y})
        if len(self.body)>self.score:
            self.body.pop(0)

        self.center_x +=self.change_x * self.speed
        self.center_y +=self.change_y * self.speed

    def eat(self,game):
        if self==game.apple:
             del game.apple
             self.score +=2
             print(self.score)
        elif self==game.pear:
             del game.pear
             self.score +=1 
             print(self.score)
        elif self==game.bomb:
             del game.bomb
             self.score -=1
             print(self.score)
        
    def gameover(self):
        if self.center_x==485 or self.center_y==485 or self.center_x==15 or self.center_y==15:
            print("Game Over")       
        elif self.score==0:
            print("Game Over")
        

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500 , height=500 , title="Snake Game")
        arcade.set_background_color(arcade.color.GREEN)
        self.apple=Apple(self)
        self.pear=Pear(self)
        self.bomb=Bomb(self)
        self.snake=Snake(self)
        


    def on_draw(self):
        arcade.start_render()
        self.apple.draw()
        self.pear.draw()
        self.bomb.draw()
        self.snake.draw()
        arcade.draw_text("score: ",10,470,arcade.color.RED , 17,20)
        arcade.finish_render()


    def on_update(self, delta_time: float):
        self.snake.move()
        self.snake.gameover()
        if arcade.check_for_collision(self.snake , self.apple):
            self.snake.eat(self.apple,self.pear,self.bomb)
            self.pear=Pear(self)

        elif arcade.check_for_collision(self.snake , self.pear):
            self.snake.eat(self.apple,self.pear,self.bomb)
            self.bomb=Bomb(self)

        elif arcade.check_for_collision(self.snake , self.bomb):
            self.snake.eat(self.apple,self.pear,self.bomb)
            self.apple=Apple(self)



    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol==arcade.key.DOWN:
            self.snake.change_x=0
            self.snake.change_y = -1
        elif symbol==arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y=0
        elif symbol==arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake_change_y = 0
   
    

game=Game()
arcade.run()
        



#Marla Windman

import sys
import arcade
import pathlib
import arcade.gui
from typing import List
import random
import math
from main import FRAME_WIDTH, FRAME_HEIGHT
from enum import auto, Enum
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3
SPRITE_SPEED = 0.5
SPRITE_SPEED2 = 1
FIRE_SPEED = 5
mouse_COUNT = 4
max_health = 10
max_health2 = 80
max_health3 = 20
num = 300
HEALTH_NUMBER_OFFSET_X = -10
HEALTH_NUMBER_OFFSET_Y = -75
class MoveEnum(Enum):
    NONE = auto()
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
#gives player heath bar
class player(arcade.AnimatedTimeBasedSprite):
    def __init__(self, ship_path: str, speed: int, game_window, center_x, center_y):
        super().__init__(ship_path)
        self.speed = speed
        self.game = game_window
            # self.center_x = random.randrange(SCREEN_WIDTH)
            # self.center_y = random.randrange(150, SCREEN_HEIGHT)
        self.center_x = 300
        self.center_y = 300
        self.max_health = max_health2
        self.cur_health = max_health2

    def draw_health_number(self):
        health_string = f"{self.cur_health}/{self.max_health}"
        arcade.draw_text(health_string,
                         start_x=self.center_x + HEALTH_NUMBER_OFFSET_X,
                         start_y=self.center_y + HEALTH_NUMBER_OFFSET_Y,
                         font_size=12,
                         color=arcade.color.WHITE)
# Gives enomys heath bar and makes so they follow player
class enomy(arcade.AnimatedTimeBasedSprite):
        def __init__(self, ship_path: str, speed: int, game_window,center_x,center_y):
            super().__init__(ship_path)
            #self.speed = speed
            self.game = game_window
            #self.center_x = random.randrange(SCREEN_WIDTH)
           # self.center_y = random.randrange(150, SCREEN_HEIGHT)
            #self.center_x = 500
            #self.center_y = 700
            self.max_health = max_health
            self.cur_health = max_health
        def move(self,run):
           # flame = pathlib.Path.cwd() / 'Assets' / 'flames'
#@#            arcade.play_sound(self.mouse_sprite_sound)
           if arcade.get_distance_between_sprites(self, run) < 500:
               if self.center_y < run.center_y:
                   self.center_y += min(SPRITE_SPEED, run.center_y - self.center_y)
                   print(min(SPRITE_SPEED, run.center_y - self.center_y))
               elif self.center_y > run.center_y:
                   self.center_y -= min(SPRITE_SPEED, self.center_y - run.center_y)
               if self.center_x < run.center_x:
                   self.center_x += min(SPRITE_SPEED, run.center_x - self.center_x)
               elif self.center_x > run.center_x:
                   self.center_x -= min(SPRITE_SPEED, self.center_x - run.center_x)
        def move2(self,run):
#            arcade.play_sound(self.mouse_sprite_sound)
           # flame = pathlib.Path.cwd() / 'Assets' / 'flames'
            if arcade.get_distance_between_sprites(self,run) < 500:
                if self.center_y < run.center_y:
                    self.center_y += min(SPRITE_SPEED, run.center_y - self.center_y)
                    print(min(SPRITE_SPEED, run.center_y - self.center_y))
                elif self.center_y > run.center_y:
                    self.center_y -= min(SPRITE_SPEED, self.center_y - run.center_y)
                if self.center_x < run.center_x:
                    self.center_x += min(SPRITE_SPEED, run.center_x - self.center_x)
                elif self.center_x > run.center_x:
                    self.center_x -= min(SPRITE_SPEED, self.center_x - run.center_x)
        def move3(self,run):
         #   arcade.play_sound(self.mush_sprite_sound)
           # flame = pathlib.Path.cwd() / 'Assets' / 'flames'
            if arcade.get_distance_between_sprites(self,run) < 500:
                if self.center_y < run.center_y:
                    self.center_y += min(SPRITE_SPEED2, run.center_y - self.center_y)
                    print(min(SPRITE_SPEED, run.center_y - self.center_y))
                elif self.center_y > run.center_y:
                    self.center_y -= min(SPRITE_SPEED2, self.center_y - run.center_y)
                if self.center_x < run.center_x:
                    self.center_x += min(SPRITE_SPEED2, run.center_x - self.center_x)
                elif self.center_x > run.center_x:
                    self.center_x -= min(SPRITE_SPEED2, self.center_x - run.center_x)

        def draw_health_number(self):

            health_string = f"{self.cur_health}/{self.max_health}"
            arcade.draw_text(health_string,
                             start_x=self.center_x + HEALTH_NUMBER_OFFSET_X,
                             start_y=self.center_y + HEALTH_NUMBER_OFFSET_Y,
                             font_size=12,
                             color=arcade.color.WHITE)
# Same as other enomy class just makes heath higher
class enomy2(arcade.AnimatedTimeBasedSprite):
    def __init__(self, ship_path: str, speed: int, game_window, center_x, center_y):
                super().__init__(ship_path)
                # self.speed = speed
                self.game = game_window
                # self.center_x = random.randrange(SCREEN_WIDTH)
                # self.center_y = random.randrange(150, SCREEN_HEIGHT)
                # self.center_x = 500
                # self.center_y = 700
                self.max_health = 20
                self.cur_health = 20

    def move(self, run):
                # flame = pathlib.Path.cwd() / 'Assets' / 'flames'
#                arcade.play_sound(self.frog_sound)
                if arcade.get_distance_between_sprites(self, run) < 300:
                    if self.center_y < run.center_y:
                        self.center_y += min(SPRITE_SPEED, run.center_y - self.center_y)
                        print(min(SPRITE_SPEED, run.center_y - self.center_y))
                    elif self.center_y > run.center_y:
                        self.center_y -= min(SPRITE_SPEED, self.center_y - run.center_y)
                    if self.center_x < run.center_x:
                        self.center_x += min(SPRITE_SPEED, run.center_x - self.center_x)
                    elif self.center_x > run.center_x:
                        self.center_x -= min(SPRITE_SPEED, self.center_x - run.center_x)

    def draw_health_number(self):

                health_string = f"{self.cur_health}/{self.max_health}"
                arcade.draw_text(health_string,
                                 start_x=self.center_x + HEALTH_NUMBER_OFFSET_X,
                                 start_y=self.center_y + HEALTH_NUMBER_OFFSET_Y,
                                 font_size=12,
                                 color=arcade.color.WHITE)

class TownWindow (arcade.Window):
    def __init__(self):
        super().__init__(960,960)
        self.wall_list = None
        self.attacknum = 0
        self.sprites_list = arcade.SpriteList()
        self.map_location = pathlib.Path.cwd() / 'Assets' / 'little witch.json'
        self.mapscene = None
        self.mush_list = arcade.SpriteList()
        self.player_stand = arcade.SpriteList()
        self.all_sprites_list = arcade.SpriteList()
        self.all_sprites_list2 = arcade.SpriteList()
        self.attacklist = arcade.SpriteList()
        self.flame_list = arcade.SpriteList()
        self.mflame_list = arcade.SpriteList()
        self.text_box = arcade.SpriteList()
        arcade.set_background_color(arcade.color.COOL_GREY)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.mousehp = 5
        self.playerhp = 10
        self.max_health = max_health
        self.cur_health = max_health
        self.enomys = 4
        self.fire_sound = arcade.load_sound(":resources:sounds/hurt3.wav")
        self.mfire_sound = arcade.load_sound(":resources:sounds/explosion2.wav")
        self.playerwalk_sound = arcade.load_sound(":resources:sounds/jump5.wav")
        self.mouse_sprite_sound = arcade.load_sound(":resources:sounds/jump3.wav")
        self.mush_sprite_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.frog_sound = arcade.load_sound(":resources:sounds/upgrade2.wav")
        self.fox_sound = arcade.load_sound(":resources:sounds/secret4.wav")
        self.hit_sound = arcade.load_sound(":resources:sounds/lose4.wav")



#gets everything read to be drawen. for exaple gets the texteres for srpits and makes then also makes the map
    def setup(self):
       run = pathlib.Path.cwd() / 'Assets' / 'Run'
       path2 = pathlib.Path.cwd() / 'Assets' / 'mayaStand.png'
       fox = pathlib.Path.cwd() / 'Assets' / 'foxidle'
       frog = pathlib.Path.cwd() / 'Assets' / 'rzabba'
       self.run  = player(None, speed=7, game_window=self,center_x=300, center_y=300)
       self.run.scale = 0.4
       self.fox = arcade.AnimatedTimeBasedSprite(None, 3.5, center_x=350, center_y=620)
       self.thing_list = arcade.SpriteList()
       self.frog = enomy2(None, speed=3, game_window=self, center_x=300, center_y=300)
       self.frog_list = arcade.SpriteList()
       all_files = run.glob('*.png')  # return a generator with all the qualified paths to all png files in dir
       foxstand = fox.glob('*.png')
       frogs = frog.glob('*.png')
       self.frog.scale = 1.6
       texturesw = []
       textures = []
       texturesf = []
       #self.flame
       self.stand = []
       self.temp = []
       self.empty = []
       atacktexture = []
       count = 0
       #player
       self.idel = arcade.AnimationKeyframe(count, 70, arcade.load_texture(path2))
       for file_path in all_files:
           count += 1
           frame = arcade.AnimationKeyframe(count, 70, arcade.load_texture(str(file_path)))# we want the whole image
           textures.append(frame)
           if count ==1:
               self.run.texture = frame.texture
       count = 0
       #attack
       attack = pathlib.Path.cwd() / 'Assets' / 'attack'
       self.attacken = arcade.AnimatedTimeBasedSprite(None, 2, center_x=350, center_y=620)
       all_file = attack.glob('*.png')
       count = 0
       for file_path in all_file:
           count += 1
           attackframe = arcade.AnimationKeyframe(count, 1400, arcade.load_texture(str(file_path)))  # we want the whole image
           atacktexture.append(attackframe)
           if count == 1:
               self.attacken.texture = attackframe.texture
       count = 0
       #fox
       for file_path in foxstand:
           count += 1
           foxframe = arcade.AnimationKeyframe(count, 70, arcade.load_texture(str(file_path)))
           texturesw.append(foxframe)
           if count == 1:
               self.fox.texture = foxframe.texture
       count = 0
       #frog
       for file_path in frogs:
           count += 1
           frogframe = arcade.AnimationKeyframe(count, 70, arcade.load_texture(str(file_path)))
           texturesf.append(frogframe)
           if count == 1:
               self.frog.texture = frogframe.texture
       self.run.frames = textures
       self.fox.frames = texturesw
       self.frog.frames = texturesf
       self.attacken.frames = atacktexture
       self.attacklist.append(self.attacken)
       self.thing_list.append(self.run)
       self.thing_list.append(self.fox)
       self.frog_list.append(self.frog)
       #self.attacken.update_animation()
       self.run.update_animation()
       self.fox.update_animation()
      # print(type(self.run.frames[self.cur_frame_idx]))
       sample_map = arcade.tilemap.load_tilemap(self.map_location)
       self.mapscene1 = arcade.Scene.from_tilemap(sample_map)
       self.wall_list = sample_map.sprite_lists['houses']
       self.simple_physics = arcade.PhysicsEngineSimple(self.run,self.wall_list)
       self.simple_physic = arcade.PhysicsEngineSimple(self.run, self.thing_list)
       self.current_scene = self.mapscene1

       woodsmap = arcade.tilemap.load_tilemap(pathlib.Path.cwd() / 'Assets' / 'woods.json')
       woodsmap2 = arcade.tilemap.load_tilemap(pathlib.Path.cwd() / 'Assets' / 'woods2.json')
       self.woods2 = arcade.Scene.from_tilemap(woodsmap2)
       self.woods = arcade.Scene.from_tilemap(woodsmap)
       self.wall_list3 = woodsmap2.sprite_lists['bush']
       self.wall_list2 = woodsmap.sprite_lists['trees']
       self.player = arcade.AnimatedWalkingSprite()
       num = [0,105,230]
       mouse2 = pathlib.Path.cwd() / 'Assets' / 'mouse.png'
       self.mouse_sprite2 = enomy(str(mouse2), speed=3, game_window=self, center_x=300, center_y=300)
       self.mouse_sprite2.scale = 3
       # self.mouse_sprite.center_x   = 5000
       self.mouse_sprite2.center_y = 5000
       self.mouse_sprite2.speed = 0.5
        #mosue
       mouse_frames2: List[arcade.AnimationKeyframe] = []
       for row in range(2):
           if row == 1:
               for col in range(3):
                   frame = arcade.AnimationKeyframe(col * row, 200, arcade.load_texture(str(mouse2),
                                                                                        num[col],
                                                                                        400,
                                                                                        120,
                                                                                        70))
                   mouse_frames2.append(frame)
       mouse = pathlib.Path.cwd() / 'Assets' / 'mouse.png'
       self.mouse_sprite = enomy(str(mouse), speed=3, game_window=self,center_x=300, center_y=300)

         #self.mouse_sprite.center_x   = 5000
       self.mouse_sprite.center_y = 5000
       self.mouse_sprite.speed = 0.5
        #mosue
       mouse_frames: List[arcade.AnimationKeyframe] = []
       for row in range(2):
            if row == 1:
                    for col in range(3):
                        frame = arcade.AnimationKeyframe(col * row, 200, arcade.load_texture(str(mouse),
                                                                                    num[col],
                                                                                    400,
                                                                                    120,
                                                                                    70))
                        mouse_frames.append(frame)
        #mushroom
       mushroom = pathlib.Path.cwd() / 'Assets' / 'Mushroom.png'
       self.Mushroom = enomy(str(mushroom), speed=3, game_window=self, center_x=300, center_y=300)
       self.Mushroom.scale = 0.8
       self.Mushroom.speed = 100
       mushroom_frame: List[arcade.AnimationKeyframe] = []
       for row in range(1):
           if row == 0:
               for col in range(6):
                   frame = arcade.AnimationKeyframe(col * row, 200, arcade.load_texture(str(mushroom),
                                                                                        col * 145,
                                                                                        10,
                                                                                        144,
                                                                                        134))
                   mushroom_frame.append(frame)



       self.Mushroom.frames = mushroom_frame
       self.mouse_sprite.frames = mouse_frames
       self.mouse_sprite2.frames = mouse_frames2
       self.all_sprites_list = arcade.SpriteList()
       self.mush_list.append(self.Mushroom)
       self.all_sprites_list.append(self.mouse_sprite)
       self.all_sprites_list2.append(self.mouse_sprite2)



    def update(self, delta_time: float):
        if self.enomys == 0:
            sys.exit()
        #updates the srpites and tecters
        self.simple_physics.update()
        self.simple_physic.update()
        self.mush_list.update()
        self.frog_list.update()
        self.thing_list.update()
        self.flame_list.update()
        self.mflame_list.update()
        self.text_box.update()
        self.frog_list.update_animation()
        self.mush_list.update_animation()
        self.flame_list.update_animation()
        self.mflame_list.update_animation()
        for player in self.thing_list:
            if self.run.cur_health == 0:
                player.remove_from_sprite_lists()
                sys.exit()
        # makes text box go away
        for text in self.text_box:
            if arcade.get_distance_between_sprites(self.run, self.fox) > 100:
                text.remove_from_sprite_lists()
        #chack for damage
        for flames in self.flame_list:
            if  arcade.get_distance_between_sprites(flames, self.mouse_sprite) < 40:
                flames.remove_from_sprite_lists()
                self.mouse_sprite.cur_health -= 1
                arcade.play_sound(self.hit_sound)
            if arcade.get_distance_between_sprites(flames, self.mouse_sprite2) < 100:
                arcade.play_sound(self.hit_sound)
                self.mouse_sprite2.cur_health -= 1
                flames.remove_from_sprite_lists()
            if arcade.get_distance_between_sprites(flames, self.Mushroom) < 40:
                arcade.play_sound(self.hit_sound)
                self.Mushroom.cur_health -= 1
                flames.remove_from_sprite_lists()
            if arcade.get_distance_between_sprites(flames, self.frog) < 40:
                arcade.play_sound(self.hit_sound)
                self.frog.cur_health -= 1
                flames.remove_from_sprite_lists()
            if flames.bottom > self.height:
                flames.remove_from_sprite_lists()
        if arcade.check_for_collision_with_list(self.run, self.all_sprites_list2) and arcade.get_distance_between_sprites(self.run, self.mouse_sprite2) < 60:
            arcade.play_sound(self.hit_sound)
            self.run.cur_health -= 2
        if arcade.get_distance_between_sprites(self.run, self.Mushroom) < 40:
            arcade.play_sound(self.hit_sound)
            self.run.cur_health -= 1
        if arcade.get_distance_between_sprites(self.run, self.frog) < 40:
            arcade.play_sound(self.hit_sound)
            self.run.cur_health -= 1
        for flames in self.mflame_list:
            hit_list = arcade.check_for_collision_with_list(flames, self.thing_list)
            if len(hit_list) > 0:
                arcade.play_sound(self.hit_sound)
                flames.remove_from_sprite_lists()
                self.run.cur_health -= 1
            if flames.bottom > self.height:
                flames.remove_from_sprite_lists()
        if self.current_scene == self.woods:
            for mouse in self.all_sprites_list:
                self.all_sprites_list.update()
                self.all_sprites_list.update_animation()
                self.mouse_sprite.move(self.run)
                if self.mouse_sprite.cur_health <= 0:
                    arcade.play_sound(self.mouse_sprite_sound)
                    mouse.remove_from_sprite_lists()
                    if self.run.cur_health == 80:
                        self.run.cur_health += 0
                    elif self.run.cur_health == 79:
                        self.run.cur_health += 1
                    elif self.run.cur_health == 78:
                        self.run.cur_health += 2
                    elif self.run.cur_health == 77:
                        self.run.cur_health += 3
                    elif self.run.cur_health == 76:
                        self.run.cur_health += 4
                    else:
                        self.run.cur_health += 5
                    mouse.center_x = 1000
                    self.enomys -= 1
            for mouse in self.all_sprites_list2:
                #self.mouse_sprite = self.temp
                self.all_sprites_list2.update()
                self.all_sprites_list2.update_animation()
                self.mouse_sprite2.move2(self.run)
                if self.mouse_sprite2.cur_health <= 0:
                    arcade.play_sound(self.mouse_sprite_sound)
                    mouse.remove_from_sprite_lists()
                    if self.run.cur_health == 80:
                        self.run.cur_health += 0
                    elif self.run.cur_health == 79:
                        self.run.cur_health += 1
                    elif self.run.cur_health == 78:
                        self.run.cur_health += 2
                    elif self.run.cur_health == 77:
                        self.run.cur_health += 3
                    elif self.run.cur_health == 76:
                        self.run.cur_health += 4
                    else:
                        self.run.cur_health += 5
                    mouse.center_x = 1000
                    self.enomys -= 1
                    #self.frog.center_y = 5000
        if self.current_scene == self.woods2:
            for mush in self.mush_list:
                #self.mouse_sprite = self.temp
                self.mush_list.update()
                self.mush_list.update_animation()
                self.Mushroom.move3(self.run)
                if self.Mushroom.cur_health <= 0:
                    arcade.play_sound(self.mush_sprite_sound)
                    mush.remove_from_sprite_lists()
                    if self.run.cur_health == 80:
                        self.run.cur_health += 0
                    elif self.run.cur_health == 79:
                        self.run.cur_health += 1
                    elif self.run.cur_health == 78:
                        self.run.cur_health += 2
                    elif self.run.cur_health == 77:
                        self.run.cur_health += 3
                    elif self.run.cur_health == 76:
                        self.run.cur_health += 4
                    else:
                        self.run.cur_health += 5
                    mush.center_x = 1000
                    self.enomys -= 1

            for frog in self.frog_list:
                self.frog_list.update()
                self.frog_list.update_animation()
                self.frog.move(self.run)
                if self.frog.cur_health <= 0:
                    frog.remove_from_sprite_lists()
                    arcade.play_sound(self.frog_sound)
                    if self.run.cur_health == 80:
                        self.run.cur_health += 0
                    elif self.run.cur_health == 79:
                        self.run.cur_health += 1
                    elif self.run.cur_health == 78:
                        self.run.cur_health += 2
                    elif self.run.cur_health == 77:
                        self.run.cur_health += 3
                    elif self.run.cur_health == 76:
                        self.run.cur_health += 4
                    else:
                        self.run.cur_health += 5
                    frog.center_x = 1000
                    self.enomys -= 1

# chages scean
        if self.current_scene == self.mapscene1:
            self.frog.center_y = 5000
            self.fox.center_x = 350
            self.fox.center_y = 620
            self.simple_physic.update()
            self.fox.update_animation()
        else:
            self.fox.center_x = 1000


       # self.fox.update_animation()
        if self.attacknum == 1 :
            #print((self.attacknum))
            self.run.texture = self.attacken.texture
            #self.run.update_animation()
           # self.attacknum -= 1
        if self.attacknum == 10:
            self.attacknum = 0
        if self.attacknum == 0:
            #print((self.attacknum))
           # self.run.texture = self.run.texture
            if self.run.change_x > 0 or  self.run.change_x < 0 or self.run.change_y > 0 or self.run.change_y<0:
                self.run.update_animation()
            else:
                self.run.texture = self.idel.texture
                #self.run.update_animation()

    def on_draw(self):
#draws things on map
        arcade.start_render()
        self.current_scene.draw()
        self.frog_list.draw()
        self.thing_list.draw()
        self.mush_list.draw()
        self.all_sprites_list.draw()
        self.all_sprites_list2.draw()
        self.flame_list.draw()
        self.mflame_list.draw()
        self.manager.draw()
        self.text_box.draw()
        self.mouse_sprite.draw_health_number()
        self.Mushroom.draw_health_number()
        self.mouse_sprite2.draw_health_number()
        self.run.draw_health_number()
        self.frog.draw_health_number()

    def on_key_press(self, key, modifiers):
        count = 0
        #Called whenever a key is pressed. """
        #player move
        if key == arcade.key.UP or key == arcade.key.W:
            self.direction = MoveEnum.UP
            self.run.change_y = 1
            arcade.play_sound(self.playerwalk_sound)
            #self.run.update_animation()
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.direction = MoveEnum.DOWN
            arcade.play_sound(self.playerwalk_sound)
            #self.player.change_y = -MOVEMENT_SPEED
            self.run.change_y = -1
            #self.run.update_animation()
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.direction = MoveEnum.LEFT
            arcade.play_sound(self.playerwalk_sound)
            #self.player.change_x = -MOVEMENT_SPEED
            self.run.change_x = -1
            #self.run.update_animation()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.direction = MoveEnum.RIGHT
            arcade.play_sound(self.playerwalk_sound)
            self.run.change_x = 1
            #self.run.update_animation()
        if self.run.center_y > 970:  # if the player is on map1 and heading off the map
            self.current_scene = self.woods
            self.run.center_y = 100
            #print(self.thing_list)
            #print(self.all_sprites_list)
            for mosue in self.all_sprites_list:
                self.mouse_sprite.center_x = 200
                self.mouse_sprite.center_y = 300
                self.simple_physics = arcade.PhysicsEngineSimple(self.run, self.wall_list2)
            for mosue in self.all_sprites_list2:
                self.mouse_sprite2.center_x = 500
                self.mouse_sprite2.center_y = 800
                self.simple_physics = arcade.PhysicsEngineSimple(self.run, self.wall_list2)
        elif self.run.center_y < self.height - 970:  # if we are on map2 and headed off the scene
            self.current_scene = self.mapscene1
            self.run.center_y = 900
            self.mouse_sprite2.center_y = 5000
            self.Mushroom.center_y = 5000
            self.frog.center_y = 5000
            self.mouse_sprite.center_y = 5000
            self.simple_physics = arcade.PhysicsEngineSimple(self.run, self.wall_list)
        elif self.run.center_x < -10:
            self.current_scene = self.woods2
            self.Mushroom.center_y = 500
            self.Mushroom.center_x = 300
            self.frog.center_y = 700
            self.frog.center_x = 500
            self.mouse_sprite.center_y = 5000
            self.mouse_sprite2.center_y = 5000
            self.simple_physics = arcade.PhysicsEngineSimple(self.run, self.wall_list3)
            self.run.center_x = 900
        elif self.current_scene == self.woods2 and self.run.center_x >  900:
            print(self.run.center_x)
            self.current_scene = self.woods
            self.run.center_y = 500
            self.run.center_x = 50
            self.Mushroom.center_y = 5000
            self.frog.center_y = 5000
            for mosue in self.all_sprites_list:
                self.mouse_sprite.center_x = 200
                self.mouse_sprite.center_y = 300
                self.simple_physics = arcade.PhysicsEngineSimple(self.run, self.wall_list2)
            for mosue in self.all_sprites_list2:
                self.mouse_sprite2.center_x = 500
                self.mouse_sprite2.center_y = 800
                self.simple_physics = arcade.PhysicsEngineSimple(self.run, self.wall_list2)
                #open text box
        if (key == arcade.key.SPACE) and arcade.get_distance_between_sprites(self.run, self.fox) < 100:
            if arcade.get_distance_between_sprites(self.run, self.fox) < 100:
               # print("hello")
               # self.run.texture = self.idel.texture
                text = pathlib.Path.cwd() / 'Assets' / 'textbox.png'
                arcade.play_sound(self.fox_sound)
                self.textbox = arcade.Sprite(text)
                self.textbox.center_x = 400
                self.textbox.center_y = 300
                self.textbox.scale = 0.7

                self.text_box.append(self.textbox)
                self.textbox.update_animation()
        #chage secane

        if arcade.get_distance_between_sprites(self.run, self.mouse_sprite) < 200:
            mflame = pathlib.Path.cwd() / 'Assets' / 'flames'
            self.mflames = arcade.AnimatedTimeBasedSprite(None, 2)
            self.mflames.change_x = FIRE_SPEED
            mflameshot = mflame.glob('*.png')
            texturesw = []
            count = 0
            for file_path in mflameshot:
                count += 1
                # print("fsfew twc")
                mflameframe = arcade.AnimationKeyframe(count, 70, arcade.load_texture(str(file_path)))
                texturesw.append(mflameframe)
                # print("hello")
                if count == 1:
                    self.mflames.texture = mflameframe.texture
            self.mflames.frames = texturesw
            start_x = self.mouse_sprite.center_x + 20
            start_y = self.mouse_sprite.center_y + 20
            self.mflames.center_x = start_x
            self.mflames.center_y = start_y
            dest_x = self.run.center_x
            dest_y = self.run.center_y
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)
            self.mflames.angle = math.degrees(angle)
            self.mflames.change_x = math.cos(angle) * FIRE_SPEED
            self.mflames.change_y = math.sin(angle) * FIRE_SPEED

            self.mflame_list.append(self.mflames)
            self.mflames.update_animation()
            arcade.play_sound(self.fire_sound)



    def on_key_release(self, key: int, modifiers: int):
        #stops player from moving
        if (key == arcade.key.UP or key == arcade.key.W) and \
                self.direction == MoveEnum.UP:
                self.direction = MoveEnum.NONE
                self.run.change_y = 0
        if (key == arcade.key.DOWN or key == arcade.key.S) and\
                self.direction == MoveEnum.DOWN:
                self.direction = MoveEnum.NONE
                self.run.change_y = 0
        if (key == arcade.key.LEFT or key == arcade.key.A) and \
                self.direction == MoveEnum.LEFT:
                self.direction = MoveEnum.NONE
                self.run.change_x = 0
        if (key == arcade.key.RIGHT or key == arcade.key.D) and \
                self.direction == MoveEnum.RIGHT:
                self.run.change_x = 0



    def on_mouse_press(self, x, y, button, modifiers):
        #fires flame
            flame = pathlib.Path.cwd() / 'Assets' / 'flames'
            self.flames = arcade.AnimatedTimeBasedSprite(None, 2)
            self.flames.change_x = FIRE_SPEED
            flameshot = flame.glob('*.png')
            textures = []
            count = 0
            for file_path in flameshot:
                count += 1
                flameframe = arcade.AnimationKeyframe(count, 0.5, arcade.load_texture(str(file_path)))
                textures.append(flameframe)
                if count == 1:
                    self.flames.texture = flameframe.texture
            self.flames.frames = textures
            self.attacknum = 1

            start_x = self.run.center_x + 20
            start_y = self.run.center_y + 20
            self.flames.center_x = start_x
            self.flames.center_y = start_y
            dest_x = x
            dest_y = y
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            self.flames.angle = math.degrees(angle)
            self.flames.change_x = math.cos(angle) * FIRE_SPEED
            self.flames.change_y = math.sin(angle) * FIRE_SPEED

            self.flame_list.append(self.flames)
            self.flames.update_animation()

            arcade.play_sound(self.fire_sound)
    def on_mouse_release(self, x, y, button, modifiers):
        #stops attack animation
        self.attacknum = 0



if __name__ == '__main__':
    window = TownWindow()
    window.setup()
    arcade.run()
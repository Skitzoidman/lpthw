from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("not yet conf.")
        print("Subclass.")
        exit(1)

class Death(Scene):
    quips = ["You died", "Your Mom", "Luser", "I have a", "Worse"]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""CentralCorridor"""))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""you miss lol"""))
            return 'death'

        elif action == "dodge!":
            print(dedent("""you dodge and die"""))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""good"""))
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""enter WeaponArmory, guess code for bomb. 3digits"""))
        code = '555'
#        code = "{}{}{}".format((randint(1, 9)), (randint(1, 9)), (randint(1, 9)), (randint(1, 9)))
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""container open"""))
            return 'the_bridge'
        else:
            print(dedent("""container locked. for ever"""))
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print(dedent("""entering bridge. 5 Gothons there."""))
        char_inv = Inventory()
        action = input("> ")
        
        if action == "shit":
            if char_inv.get_item("life") == True:
               return 'escape_pod'

        if action == "throw the bomb":
            print(dedent("""you throw the bomb and die"""))
            return 'death'

        elif action == 'slowly place the bomb':
            print(dedent("""worked. you escape"""))
            return 'escape_pod'

        else:
            print("DOES NOT COMPUTE")
            return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print(dedent("""chose pod 1 to 5"""))
        good_pod = randint(1, 5)
        guess = input("[pod #]> ")
        print(guess)

        if guess != int(good_pod) and guess != 'lol':
            print(dedent("""wrong pod. you die, lol"""))
            return 'death'
#        elif guess == int(good_pod) or guess == 'lol':
        else:
            print(dedent("""chose pod {}. you won!""".format(guess)))
            return 'finished'

class Finished(Scene):
    def enter(self):
        print("You won")
        return 'finished'

class Inventory(object):
    item_list = {}

    def __init__(self):
        self.add_item("life")
        pass
    
    def add_item(self, in_item):
#        print(in_item)
        self.item_list.__setitem__(in_item, True)
#        print(self.item_list[in_item])
        pass

    def get_item(self, search_item):
        out_item = self.item_list.get(search_item)
        return out_item
        pass

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Map(object):
    scenes = {'central_corridor': CentralCorridor(), 'laser_weapon_armory': LaserWeaponArmory(), 'the_bridge': TheBridge(), 'escape_pod': EscapePod(), 'death': Death(), 'finished': Finished(),}

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

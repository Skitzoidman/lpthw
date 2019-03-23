class Scene(object):
#    def __init__(self, name):
#       self.name = name

    def enter(self):
#        print("You' re entering: {}".format(self.name))
        pass

class Engine(object):
    def __init__(self, scene_map):
        pass
    
    def play(self):
        pass

class Death(Scene):
    def enter(self):
#        print("You die horribly and you are going to burn in the eternal fires of space hell.")
        pass

class CentralCorridor(Scene):
    def enter(self):
#        print("You are in the main corridor. There are 2 doors and a small hatchway.\nWhich one do you wish to enter?")
        pass

class LaserWeaponArmory(Scene):
    def enter(self):
#        print("")
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

class Map(object):
    def __init___(self, start_scene):
#        self.start_scene = start_scene
        pass
#    def print_scene():
#        print(start_scene)

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass
a_scene = Scene("lol")
#a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
#Scene("LOL").enter()

#Map().opening_scene()

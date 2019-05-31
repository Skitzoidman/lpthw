#scenes:
class Scene(object):
#    def __init__(self, name):
#       self.name = name

    def enter(self):
#        print("You' re entering: {}".format(self.name))
        pass


class Death(Scene):
    def enter(self):
        print("You die horribly and you are going to burn in the eternal fires of space hell.")
        pass

class CentralCorridor(Scene):
    def enter(self):
        print("You are in the main corridor. There are 2 doors and a small hatchway.\nWhich one do you wish to enter?")
        nxt = input("> ")
        return nxt
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

#game engine:

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
        print(scene_map)
        pass
    
    def play(self):
        choice = self.scene_map.enter()
        return choice
        pass
class Map(object):
    def __init__(self, start_scene):
        self.start_scene = start_scene
#        if start_scene == 'death':
#            self.scenes[start_scene].enter()
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        curr_scene = self.start_scene
        return curr_scene
        pass

scenes = {'0':CentralCorridor(), '666':Death()}
num = '0'
a_map = Map(scenes[num]).opening_scene()
#a_map = Map('death').opening_scene()
a_game = Engine(a_map)
num = a_game.play()
print(num)

 #print("""You wake up..a little dizzy... in a big corridor. You hear noises like BOOM BOOM PEW PEW and some kind of dust and fog is everywhere around you.\nAfter a few seconds your vison is clearing up and u don't feel that dizzy anymore. U realize u are on a space ship. The noises are people fighting. Obviously they are fighting your ship as well as on your ship.\nas the fog is lifting you see a big unfriendly and ugly Gothon in front of you, seems he got a blaster pointing to your nuts.\n""")

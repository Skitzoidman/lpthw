#scenes:
class Scene(object):
#    def __init__(self, name):
#       self.name = name

    def enter(self):
#        print("You' re entering: {}".format(self.name))
        pass


class Death(Scene):
    def enter(self):
        print("You die horribly and you are going to burn in the eternal fires of space hell.\nYou most certainly would have died from AIDS anyway, you sucker, nigger without command line skills.\n\nQuit playing video games and get a job. Cock loving geek.")
        pass

class CentralCorridor(Scene):
    def enter(self):
        nxt = 0
        while char_inv.get_item('head_of_gothon') != True and nxt != '666':
            print("""You wake up..a little dizzy... in a big corridor. You hear noises like BOOM BOOM PEW PEW and some kind of dust or fog is everywhere around you.\nAfter a few seconds your vison is clearing up and u don't feel that dizzy anymore. U realize u are on a space ship. The noises are people fighting. Obviously they are fighting your ship as well as on your ship.\nas the fog is lifting you see a big unfriendly and ugly Gothon in front of you, seems he got a blaster pointing to your nuts.\nWhat do you do now, you strong man, you most charming of all imposters?\n\n\t1: try to run(as you always do)\n\t2: beat the shit out of that guy, he is not that scary(who needs balls anyway?)\n\t3: tell him a joke(probably a good one?)\n""")
            answer = input("> ")
            if answer == '1' or answer == '2' or answer == '3':
                if answer == '1':
                    print("\nUp to now that worked out very fine for you. But not this time, lol. He is really eager to kill you. And this is the last time you ran away.\n")
                    nxt = '666'
                if answer == '2':
                    print("""\nNot strong enough, kek. Did you forget to take your steroids? Did you even lift?\nHe first shoots of your balls, ouch.
 Then he smashes your spine with his bare hands. At least it doesn't take long until you loose your contiousness again. Almost instantly.\n""")
                    nxt = '666'
                if answer == '3':
                    print("""Oh boi. It worked. He is laughing and laughing and laughing....he can't stop...he is gasping for air, unsuccesfully.\nHe is dying slowly, but happy.\nHope you won't tell this one to a lady you are trying to impress.\n""")
                    char_inv.add_item('head_of_gothon')
#                print(char_inv)
#                print(char_inv.get_item('1'))
                    
#        if answer == '1' or answer == '2':
#            nxt = '666'
            else:
                print("Dude?! That's not an option. You think this is funny? It's a matter of life and death!\nThe Gothon doesn't think it's funny as well. He just repoints the blaster to your head...and shoots...you are dead.\nI really would like to tell you that your head exploded and your brain and blood is spilling on the floor. Just to let you know how dramatic this descision was. But it's not true. Your head just evaporated and your neck cauterised. So there is no blood.\nBut there is also a good thing about it: Maybe he can use your corpse to harvest the organs and sell them to some smugglers. Believe it or not, it's a prospering market even nowadays.\n")
                nxt = '666'
        if nxt != '666':   
            print("""You are in the main corridor. There are:\n
\t1. a door to the left
\t2. a door in front of you
\t3. a small hatchway under your feet
\nWhich one do you wish to enter?""")
            nxt = input("> ")    
        return nxt
        pass

class LaserWeaponArmory(Scene):
    def enter(self):
        nxt = '0'
        print("Seems like this is the armory. Maybe you can find a big huge blaster to compensate...you know what I mean. Try to get your hands on it, you'll love it... I promise.")
        char_inv.add_item('big_ball_blaster')
        return nxt
        pass

class TheBridge(Scene):
    def enter(self):
        nxt = '666'
        if char_inv.get_item('big_ball_blaster') != True:
            print("Oh shit, another Gothon. This one is a very angry one. He charges towards you and crushes your bones.\n")
        if char_inv.get_item('big_ball_blaster') == True:
            nxt = '0'
        return nxt
        pass

class EscapePod(Scene):
    def enter(self):
        print("You made it! At least if you can get pass those high-tech gothon spaceships scanning for you, god knows why. I don't think you are worth that much trouble.\nAnd if you you really can do that you just have to survive in space for... let's say some weeks.. without food, nor water.\nYou may really think about quitting playing video games and doing real crazy shit, like fucking some girls, beeing high on Emma or Alice in the club, smoking some weed in the sunset. Enjoy life you fool.") 
        pass

class Inventory(object):
    item_list = {}

    def __init__(self):
#        self.item = item
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

#game engine:
class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
        pass
    
    def play(self):
        choice = self.scene_map.enter()
        return choice
        pass

class Map(object):
    def __init__(self, start_scene):
        self.start_scene = start_scene
        pass

#    def next_scene(self, scene_name):
#        pass

    def open_scene(self):
        self.start_scene
        return self.start_scene
        pass

scenes = {'0':CentralCorridor(), '1':LaserWeaponArmory(), '2':TheBridge(), '3':EscapePod(),'666':Death()}
scene_ref = '0'
char_inv = Inventory()

while scene_ref == '0' or scene_ref == '1' or scene_ref == '2' or scene_ref == '3' or scene_ref == '666':
    a_map = Map(scenes[scene_ref]).open_scene()
    a_game = Engine(a_map)
    scene_ref = a_game.play()

#if num != '0' or num != '2' or num != '2' or num != '3' or num != '666' or num != 'bla':
#    print("WTF! You broke it! You shithead, moron. Why do you even live on? Get out of my game!")

# Importing Libraries
from tkinter import *
from random import *
from math import *
import os
from tkinter import simpledialog

class Element:
    def __init__(self, properties):
        self.properties = properties

# Create The Create New Mod Function
def createNewMod():
    exit

def create_file_from_template(template_path, new_file_path, replacements):
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

        # Perform replacements in the template content
        for key, value in replacements.items():
            print(f"{key} : {value}")
            replace = eval(value)
            template_content = template_content.replace(key, replace)

    # Create the directory if it doesn't exist
    directory = os.path.dirname(new_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(new_file_path, 'w') as new_file:
        new_file.write(template_content)

def makeItem():
    pass

def stringReturn(name):
    return name

class Mod:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

def createElement():
    toMake = canMake.get(ACTIVE)

    name = simpledialog.askstring('Text Input', 'Name without spaces:')

    tMod = Mod(name)
    
    replaces = {'<MOD>' : f'''"{mod}"''', '<NAME>' : f'''"{name}"'''}

    #for prop in elementTypes[toMake].properties:
    #    exec(prop)

    if toMake == "item":
        global channel, noMelee, noUseGraphic, axe, hammer, pick, tileBoost, useStyle, damageType, useAnimation, sound, rarity, useTime, useAnimation, damage, knockback, crit, goldcost, autoReuse
        useStyles = ["Swing"]
        damageTypes = ["Melee"]
        rarities = ["Blue"]
        sounds = ["Item1"]
        
        useStyle = Listbox(root)
        for item in useStyles:
            useStyle.insert(END, item)
        useStyle.place(x=152, y=2)
            
        useTime = IntVar()
        useAnimation = IntVar()
        damage = IntVar()
        knockback = IntVar()
        crit = IntVar()
        goldcost = IntVar()
        axe = IntVar()
        hammer = IntVar()
        pick = IntVar()
        tileBoost = IntVar()

        Label(root, text="Use time").place(x = 152, y = 180)
        Spinbox(root, from_=-2147483647, to=2147483647, textvariable=useTime).place(x=152, y=200)
        Label(root, text="Use animation").place(x = 302, y = 180)
        Spinbox(root, from_=-2147483647, to=2147483647, textvariable=useAnimation).place(x=302, y=200)
        Label(root, text="Damage").place(x = 152, y = 230)
        Spinbox(root, from_=-2147483647, to=2147483647, textvariable=damage).place(x=152, y=250)
        Label(root, text="Knockback").place(x = 302, y = 230)
        Spinbox(root, from_=-2147483647, to=2147483647, textvariable=knockback).place(x=302, y=250)
        Label(root, text="Crit").place(x = 152, y = 280)
        Spinbox(root, from_=-2147483647, to=2147483647, textvariable=crit).place(x=152, y=300)
        Label(root, text="Gold cost").place(x = 302, y = 280)
        Spinbox(root, from_=-2147483647, to=2147483647, textvariable=goldcost).place(x=302, y=300)
        Label(root, text="Axe").place(x = 152, y = 330)
        Spinbox(root, from_=-2147483647, to=2147483647, textvariable=axe).place(x=152, y=350)
        Label(root, text="Hammer").place(x = 302, y = 330)
        Spinbox(root, from_=-2147483647, to=2147483647, textvariable=hammer).place(x=302, y=350)
        Label(root, text="Pick").place(x = 152, y = 380)
        Spinbox(root, from_=-2147483647, to=2147483647, textvariable=pick).place(x=152, y=400)
        Label(root, text="Tile boost").place(x = 302, y = 380)
        Spinbox(root, from_=-2147483647, to=2147483647, textvariable=tileBoost).place(x=302, y=400)
        
        damageType = Listbox(root)
        for item in damageTypes:
            damageType.insert(END, item)
        damageType.place(x=302, y=2)
        
        rarity = Listbox(root)
        
        for item in rarities:
            rarity.insert(END, item)
        rarity.place(x=452, y=2)
            
        sound = Listbox(root)
        for item in sounds:
            sound.insert(END, item)
        sound.place(x=602, y=2)
          
        autoReuse = BooleanVar()
        channel = BooleanVar()
        noMelee = BooleanVar()
        noUseGraphic = BooleanVar()

        replaces['<USESTYLE>'] = "useStyle.get(ACTIVE)"
        replaces['<USETIME>'] = "str(useTime.get())"
        replaces['<USEANIMATION>'] = "str(useAnimation.get())"
        replaces['<AUTOREUSE>'] = "str(autoReuse.get())"
        replaces['<DAMAGETYPE>'] = "damageType.get(ACTIVE)"
        replaces['<DAMAGE>'] = "str(damage.get())"
        replaces['<KNOCKBACK>'] = "str(knockback.get())"
        replaces['<CRIT>'] = "str(crit.get())"
        replaces['<GOLDCOST>'] = "str(goldcost.get())"
        replaces['<RARITY>'] = "rarity.get(ACTIVE)"
        replaces['<SOUND>'] = "sound.get(ACTIVE)"
        replaces['<AXE>'] = "str(axe.get())"
        replaces['<HAMMER>'] = "str(hammer.get())"
        replaces['<PICK>'] = "str(pick.get())"
        replaces['<TILEBOOST>'] = "str(tileBoost.get())"
        replaces['<CHANNEL>'] = "str(channel.get())"
        replaces['<NOMELEE>'] = "str(noMelee.get())"
        replaces['<NOUSEGRAPHIC>'] = "str(noUseGraphic.get())"
        
        Checkbutton(root, text="Auto reuse", variable=autoReuse).place(x=152, y=500)
        Checkbutton(root, text="Channel", variable=channel).place(x=302, y=500)
        Checkbutton(root, text="No melee", variable=noMelee).place(x=452, y=500)
        Checkbutton(root, text="No use graphic", variable=noUseGraphic).place(x=602, y=500)
    elif toMake == "tile":
        global solid, mergeDirt, blockLight, dust, mapr, mapg, mapb
        dusts = ["Stone"]

        dust = Listbox(root)
        for item in dusts:
            dust.insert(END, item)
        dust.place(x=152, y=2)

        mapr = IntVar()
        mapg = IntVar()
        mapb = IntVar()
        solid = BooleanVar()
        mergeDirt = BooleanVar()
        blockLight = BooleanVar()

        Label(root, text="Map R").place(x = 152, y = 180)
        Spinbox(root, from_=-2147483647, to=2147483647, textvariable=mapr).place(x=152, y=200)
        Label(root, text="Map G").place(x = 302, y = 180)
        Spinbox(root, from_=-2147483647, to=2147483647, textvariable=mapg).place(x=302, y=200)
        Label(root, text="Map B").place(x = 452, y = 180)
        Spinbox(root, from_=-2147483647, to=2147483647, textvariable=mapb).place(x=452, y=200)

        Checkbutton(root, text="Solid", variable=solid).place(x=152, y=500)
        Checkbutton(root, text="Merge dirt", variable=mergeDirt).place(x=302, y=500)
        Checkbutton(root, text="Block light", variable=blockLight).place(x=452, y=500)
    
        replaces['<SOLID>'] = "str(solid.get())"
        replaces['<MERGEDIRT>'] = "str(mergeDirt.get())"
        replaces['<BLOCKLIGHT>'] = "str(blockLight.get())"
        replaces['<DUST>'] = "dust.get(ACTIVE)"
        replaces['<MAPR>'] = "str(mapr.get())"
        replaces['<MAPG>'] = "str(mapg.get())"
        replaces['<MAPB>'] = "str(mapb.get())"

    print("eh")
    Button(root, text="Save", height = 1, width = 16, command = lambda: create_file_from_template(f"Templates/{toMake}.txt", f"{currentpath}\\{toMake.capitalize()}s\\{name}.cs", replaces)).place(x=152, y=450)

def openWorkspace(modpath):
    global currentpath
    global root
    global sideFrame
    global mainFrame
    global canMake
    global make
    
    for widget in root.winfo_children():
        widget.destroy()
        
    root.title(f"TCreator - {modpath}")

    currentpath = modpath

    sideFrame = Frame(root, width=150, height=600, bg="gray")
    mainFrame = Frame(root, width=850, height=600, bg="darkgray")
    sideFrame.grid(row = 0, column = 0)
    mainFrame.grid(row = 0, column = 1)
    
    canMake = Listbox(root)
    canMake.place(x=2, y=2)
    make = Button(root, text="Create", height = 1, width = 16, command=createElement)
    make.place(x=2, y=180)

    items = ['item', 'tile', 'npc', 'projectile', 'buff']
    for item in items:
        canMake.insert(END, item)

def list_folders(path):
    folders = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            folders.append(item)
    return folders
    
# Create The Window
root = Tk()
root.title("TCreator - Start Menu")
root.geometry("1000x600")
root.resizable(0, 0)

# Create The Side Frame
sideFrame = Frame(root, width=300, height=600, bg="gray")

# Create The Main Frame
mainFrame = Frame(root, width=700, height=600, bg="darkgray")

# Place Everything On The Grid
sideFrame.grid(row = 0, column = 0)
mainFrame.grid(row = 0, column = 1)

# Create A List Of Mods
settingsfile = open("settings.txt", "r+")

for line in settingsfile:
    modlocation = line.strip()
 
mods = list_folders(modlocation)

currentpath = ""

btny = 2

for mod in mods:
    Button(root, text=mod, height=1, width=41, command=lambda: openWorkspace(os.path.join(modlocation, mod))).place(x=2, y=btny)
    btny += 27

elementTypes = {"item" : Element(["replaces['<USESTYLE>'] = simpledialog.askstring('Text Input', 'Use style:')",
                                  "replaces['<USETIME>'] = simpledialog.askstring('Text Input', 'Use time:')",
                                  "replaces['<USEANIMATION>'] = simpledialog.askstring('Text Input', 'Use animation:')",
                                  "replaces['<AUTOREUSE>'] = (str(simpledialog.askstring('Text Input', 'Auto reuse:') == 1)).lower()",
                                  "replaces['<DAMAGETYPE>'] = simpledialog.askstring('Text Input', 'Damage type:')",
                                  "replaces['<DAMAGE>'] = simpledialog.askstring('Text Input', 'Damage:')",
                                  "replaces['<KNOCKBACK>'] = simpledialog.askstring('Text Input', 'Knockback:')",
                                  "replaces['<CRIT>'] = simpledialog.askstring('Text Input', 'Crit:')",
                                  "replaces['<GOLDCOST>'] = simpledialog.askstring('Text Input', 'Gold cost:')",
                                  "replaces['<RARITY>'] = simpledialog.askstring('Text Input', 'Rarity:')",
                                  "replaces['<SOUND>'] = simpledialog.askstring('Text Input', 'Sound:')"])}

# Create The Menu Buttons
createBtn = Button(root, text="Create New Mod", command=createNewMod).place(x=50, y=300)

mainloop()


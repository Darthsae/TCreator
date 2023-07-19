# Importing Libraries
from tkinter import *
from random import *
from math import *
import os, re
from tkinter import simpledialog
from PIL import Image

def get_image_dimensions(image_path, width=True, height=True):
    print(width)
    print(height)
    try:
        with Image.open(image_path) as img:
            awidth, aheight = img.size
            if width and height:
                toReturn = "awidth, aheight"
            elif width:
                toReturn = "awidth"
            elif height:
                toReturn = "aheight"
            else:
                awidth, aheight = 16, 16
                toReturn = "awidth, aheight"
            return eval(toReturn)
    except OSError as e:
        print(f"Unable to open image file: {e}")
        awidth, aheight = 16, 16
        if width and height:
            toReturn = "awidth, aheight"
        elif width:
            toReturn = "awidth"
        elif height:
            toReturn = "aheight"
        else:
            toReturn = "awidth, aheight"
        return eval(toReturn)

class ElementData():
    def __init__(self, elementType, values, name):
        self.type = elementType
        self.values = values
        self.name = name

class ElementButton(Button):
    def __init__(self, *args, **kwargs):
        self.type = kwargs.pop("elementType", None)
        self.values = kwargs.pop("values", None)
        super().__init__(*args, **kwargs)

def extract_number_from_string(string):
    pattern = r"\d+"
    matches = re.findall(pattern, string)

    if matches:
        number = int(matches[0])
        return number
    else:
        return None
        
def get_replaced_values(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    patternV = r'(\w+)\s+=\s+(.*?);'
    matchesV = re.findall(patternV, content)

    patternC = r'(?:Item|Tile)\.\w+\s+=\s+(.*?);'
    matchesC = re.findall(patternC, content)

    replaced_values = {}

    for matchC, matchV in zip(matchesC, matchesV):
        replaced_values[f"<{str(matchV[0]).upper()}>"] = matchC

    return replaced_values

class ScrollableWindow(Frame):
    """
    A custom scrollable window widget.

    Parameters:
        parent (Tkinter widget): The parent widget for the ScrollableWindow.
        items (list): A list of items to be displayed as buttons in the window.
        width (int): The width of the ScrollableWindow in pixels (default: 300).
        height (int): The height of the ScrollableWindow in pixels (default: 200).
        bg (str): The background color of the ScrollableWindow (default: "white").

    Methods:
        button_click(item)
            Executes when a button in the ScrollableWindow is clicked.
            Prints a message indicating which button was clicked.

    Example usage:
        # Create a Tkinter window
        root = Tk()

        # Create a list of items
        items = ["Button 1", "Button 2", "Button 3"]

        # Create a ScrollableWindow instance
        scroll_window = ScrollableWindow(root, items)

        # Pack the ScrollableWindow into the root window
        scroll_window.pack()

        # Start the Tkinter event loop
        root.mainloop()
    """

    def __init__(self, parent, items, width=300, height=200, bg="white", fg="white"):
        """
        Initializes the ScrollableWindow object.

        Parameters:
            parent (Tkinter widget): The parent widget for the ScrollableWindow.
            items (list): A list of items to be displayed as buttons in the window.
            width (int): The width of the ScrollableWindow in pixels (default: 300).
            height (int): The height of the ScrollableWindow in pixels (default: 200).
            bg (str): The background color of the ScrollableWindow (default: "white").
        """
        Frame.__init__(self, parent, bg=bg)

        # Create a canvas and scrollbar
        canvas = Canvas(self, bg=bg, relief=FLAT)
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Add a frame inside the canvas
        frame = Frame(canvas, bg=bg)
        frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=frame, anchor="nw")

        # Configure the scrollbar to scroll the canvas
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Add buttons to the frame
        for item in items:
            button = ElementButton(frame, bg=accentColor, activebackground=highlightColor, text=item.name, command=lambda item=item: self.button_click(item), elementType=item.type, values=item.values)
            button.pack(fill="x", expand=True)
        
    def button_click(self, item):
        """
        Event handler for button clicks.

        Parameters:
            item (str): The label of the button that was clicked.
        """
        print(f"Button '{item.name}' clicked!")
        print(f"Length:{len(item.values)}")
        extras = []
        for val in item.values:
            print(val + " = " + item.values[val])
            extras.append(item.values[val])
        if item.type == "item":
            print(f"{item.name}")
            createElement(toMakeValue="'item'", nameValue=f"'{item.name}'", extraData=item.values);

def list_files_with_extension(directory, extension):
    if not os.path.exists(directory):
        return []
    
    files = []
    for file in os.listdir(directory):
        if file.endswith(extension):
            files.append(file[:-len(extension)])
    return files

def create_file_from_template(template_path, new_file_path, replacements):
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

        # Perform replacements in the template content
        for key, value in replacements.items():
            print(f"{key} : {value}")
            if eval(value) and key == "tile":
                toKey = "<PLACEABLETILE>"
                replace = "Item.DefaultToPlaceableTile(ModContent.TileType<Tiles." + tile.get() + ">());"
            elif not eval(value) and key == "tile":
                toKey = "<PLACEABLETILE>"
                replace = " "
            else:
                toKey = key
                replace = eval(value)
            template_content = template_content.replace(toKey, replace)

    # Create the directory if it doesn't exist
    directory = os.path.dirname(new_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(new_file_path, 'w') as new_file:
        new_file.write(template_content)

    openWorkspace(currentpath, currentmod)

class Mod:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

def createElement(toMakeValue="canMake.get(ACTIVE)", nameValue="simpledialog.askstring('Text Input', 'Name without spaces:')", extraData=None):
    global mainFrame, name

    print(nameValue)
    
    toMake = eval(toMakeValue)
    name = eval(nameValue)
    
    for widget in mainFrame.winfo_children():
        widget.destroy()
    mainFrame.destroy()
        
    mainFrame = Frame(root, width=850, height=600, bg=mainThemeColor)
    mainFrame.pack(side="right", fill="both", expand=True)

    tMod = Mod(name)
    
    replaces = {'<MOD>' : f'''"{currentmod}"''', '<NAME>' : f'''"{name}"'''}

    #for prop in elementTypes[toMake].properties:
    #    exec(prop)

    if toMake == "item":
        global accessory, defense, tile, doTile, channel, noMelee, noUseGraphic, axe, hammer, pick, tileBoost, useStyle, damageType, useAnimation, sound, rarity, useTime, useAnimation, damage, knockback, crit, goldcost, autoReuse
        useStyles = ["ItemUseStyleID.Swing"]
        damageTypes = ["DamageClass.Melee"]
        rarities = ["ItemRarityID.Blue"]
        sounds = ["SoundID.Item1"]

        tile = StringVar()
        
        useStyle = Listbox(root, bg=accentColor, selectbackground=highlightColor)
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
        defense = IntVar()
        tileBoost = IntVar()

        Label(root, bg=accentColor, text="Use time").place(x = 152, y = 180)
        Spinbox(root, bg=accentColor, from_=-2147483647, to=2147483647, textvariable=useTime).place(x=152, y=200)
        Label(root, bg=accentColor, text="Use animation").place(x = 302, y = 180)
        Spinbox(root, bg=accentColor, from_=-2147483647, to=2147483647, textvariable=useAnimation).place(x=302, y=200)
        Label(root, bg=accentColor, text="Damage").place(x = 152, y = 230)
        Spinbox(root, bg=accentColor, from_=-2147483647, to=2147483647, textvariable=damage).place(x=152, y=250)
        Label(root, bg=accentColor, text="Knockback").place(x = 302, y = 230)
        Spinbox(root, bg=accentColor, from_=-2147483647, to=2147483647, textvariable=knockback).place(x=302, y=250)
        Label(root, bg=accentColor, text="Crit").place(x = 152, y = 280)
        Spinbox(root, bg=accentColor, from_=-2147483647, to=2147483647, textvariable=crit).place(x=152, y=300)
        Label(root, bg=accentColor, text="Gold cost").place(x = 302, y = 280)
        Spinbox(root, bg=accentColor, from_=-2147483647, to=2147483647, textvariable=goldcost).place(x=302, y=300)
        Label(root, bg=accentColor, text="Axe").place(x = 152, y = 330)
        Spinbox(root, bg=accentColor, from_=-2147483647, to=2147483647, textvariable=axe).place(x=152, y=350)
        Label(root, bg=accentColor, text="Hammer").place(x = 302, y = 330)
        Spinbox(root, bg=accentColor, from_=-2147483647, to=2147483647, textvariable=hammer).place(x=302, y=350)
        Label(root, bg=accentColor, text="Pick").place(x = 152, y = 380)
        Spinbox(root, bg=accentColor, from_=-2147483647, to=2147483647, textvariable=pick).place(x=152, y=400)
        Label(root, bg=accentColor, text="Tile boost").place(x = 302, y = 380)
        Spinbox(root, bg=accentColor, from_=-2147483647, to=2147483647, textvariable=tileBoost).place(x=302, y=400)
        
        damageType = Listbox(root, bg=accentColor, selectbackground=highlightColor)
        for item in damageTypes:
            damageType.insert(END, item)
        damageType.place(x=302, y=2)
        
        rarity = Listbox(root, bg=accentColor, selectbackground=highlightColor)
        
        for item in rarities:
            rarity.insert(END, item)
        rarity.place(x=452, y=2)
            
        sound = Listbox(root, bg=accentColor, selectbackground=highlightColor)
        for item in sounds:
            sound.insert(END, item)
        sound.place(x=602, y=2)
          
        autoReuse = BooleanVar()
        channel = BooleanVar()
        noMelee = BooleanVar()
        noUseGraphic = BooleanVar()
        accessory = BooleanVar()
        doTile = BooleanVar()

        replaces['<HEIGHT>'] = "str(get_image_dimensions(f'{currentpath}\\Items\\{name}.png', width=False))"
        replaces['<WIDTH>'] = "str(get_image_dimensions(f'{currentpath}\\Items\\{name}.png', height=False))"
        replaces['<USESTYLE>'] = "useStyle.get(ACTIVE)"
        replaces['<USETIME>'] = "str(useTime.get())"
        replaces['<USEANIMATION>'] = "str(useAnimation.get())"
        replaces['<AUTOREUSE>'] = "str(autoReuse.get()).lower()"
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
        replaces['<CHANNEL>'] = "str(channel.get()).lower()"
        replaces['<NOMELEE>'] = "str(noMelee.get()).lower()"
        replaces['<NOUSEGRAPHIC>'] = "str(noUseGraphic.get()).lower()"
        replaces['<DEFENSE>'] = "str(defense.get())"
        replaces['<ACCESSORY>'] = "str(accessory.get()).lower()"
        replaces['tile'] = "doTile.get()"
        
        Checkbutton(root, bg=accentColor, activebackground=highlightColor, text="Auto reuse", variable=autoReuse).place(x=152, y=500)
        Checkbutton(root, bg=accentColor, activebackground=highlightColor, text="Channel", variable=channel).place(x=302, y=500)
        Checkbutton(root, bg=accentColor, activebackground=highlightColor, text="No melee", variable=noMelee).place(x=452, y=500)
        Checkbutton(root, bg=accentColor, activebackground=highlightColor, text="No use graphic", variable=noUseGraphic).place(x=602, y=500)
        Checkbutton(root, bg=accentColor, activebackground=highlightColor, text="Tile", variable=doTile).place(x=152, y=550)
        Entry(root, bg=accentColor, textvariable=tile).place(x=302, y=550)
        Checkbutton(root, bg=accentColor, activebackground=highlightColor, text="Accessory", variable=accessory).place(x=452, y=550)

        if not extraData == None:
            try:
                useTime.set(int(extraData["<USETIME>"]))
            except:
                pass
            try:
                useAnimation.set(int(extraData["<USEANIMATION>"]))
            except:
                pass
            try:
                autoReuse.set(bool(extraData["<AUTOREUSE>"] == "true"))
            except:
                pass
            try:
                damage.set(int(extraData["<DAMAGE>"]))
            except:
                pass
            try:
                knockback.set(int(extraData["<KNOCKBACK>"]))
            except:
                pass
            try:
                crit.set(int(extraData["<CRIT>"]))
            except:
                pass
            try:
                goldcost.set(extract_number_from_string(extraData["<VALUE>"]))
            except:
                pass
            try:
                axe.set(int(extraData["<AXE>"]))
            except:
                pass
            try:
                hammer.set(int(extraData["<HAMMER>"]))
            except:
                pass
            try:
                pick.set(int(extraData["<PICK>"]))
            except:
                pass
            try:
                tileBoost.set(int(extraData["<TILEBOOST>"]))
            except:
                pass
            try:
                channel.set(bool(extraData["<CHANNEL>"] == "true"))
            except:
                pass
            try:
                noMelee.set(bool(extraData["<NOMELEE>"] == "true"))
            except:
                pass
            try:
                noUseGraphic.set(bool(extraData["<NOUSEGRAPHIC>"] == "true"))
            except:
                pass
            try:
                accessory.set(bool(extraData["<ACCESSORY>"] == "true"))
            except:
                pass
            try:
                defense.set(int(extraData["<DEFENSE>"]))
            except:
                pass
    elif toMake == "tile":
        global solid, mergeDirt, blockLight, dust, mapr, mapg, mapb
        dusts = ["DustID.Stone"]

        dust = Listbox(root, bg=accentColor, selectbackground=highlightColor)
        for item in dusts:
            dust.insert(END, item)
        dust.place(x=152, y=2)

        mapr = IntVar()
        mapg = IntVar()
        mapb = IntVar()
        solid = BooleanVar()
        mergeDirt = BooleanVar()
        blockLight = BooleanVar()

        Label(root, text="Map R", bg=accentColor).place(x = 152, y = 180)
        Spinbox(root, bg=accentColor, from_=-2147483647, to=2147483647, textvariable=mapr).place(x=152, y=200)
        Label(root, text="Map G", bg=accentColor).place(x = 302, y = 180)
        Spinbox(root, bg=accentColor, from_=-2147483647, to=2147483647, textvariable=mapg).place(x=302, y=200)
        Label(root, text="Map B", bg=accentColor).place(x = 452, y = 180)
        Spinbox(root, bg=accentColor, from_=-2147483647, to=2147483647, textvariable=mapb).place(x=452, y=200)

        Checkbutton(root, bg=accentColor, activebackground=highlightColor, text="Solid", variable=solid).place(x=152, y=500)
        Checkbutton(root, bg=accentColor, activebackground=highlightColor, text="Merge dirt", variable=mergeDirt).place(x=302, y=500)
        Checkbutton(root, bg=accentColor, activebackground=highlightColor, text="Block light", variable=blockLight).place(x=452, y=500)
    
        replaces['<SOLID>'] = "str(solid.get()).lower()"
        replaces['<MERGEDIRT>'] = "str(mergeDirt.get()).lower()"
        replaces['<BLOCKLIGHT>'] = "str(blockLight.get()).lower()"
        replaces['<DUST>'] = "dust.get(ACTIVE)"
        replaces['<MAPR>'] = "str(mapr.get())"
        replaces['<MAPG>'] = "str(mapg.get())"
        replaces['<MAPB>'] = "str(mapb.get())"

    #print("eh")
    Button(root, text="Save", height = 1, width = 16, bg=accentColor, activebackground=highlightColor, command = lambda: create_file_from_template(f"Templates/{toMake}.txt", f"{currentpath}\\{toMake.capitalize()}s\\{name}.cs", replaces)).place(x=152, y=450)

def openWorkspace(modpath, mod):
    global currentpath
    global currentmod
    global root
    global sideFrame
    global mainFrame
    global canMake
    global make
    global items
    global tiles
    
    for widget in root.winfo_children():
        widget.destroy()
        
    root.title(f"TCreator - {modpath}")

    currentpath = modpath
    currentmod = mod

    toadd = []

    items = list_files_with_extension(currentpath+"/Items", ".cs")
    tiles = list_files_with_extension(currentpath+"/Tiles", ".cs")

    for item in items:
        toadd.append(ElementData("item", get_replaced_values(currentpath + "\\Items\\" + item + ".cs"), item))
        #print(item)

    for tile in tiles:
        toadd.append(ElementData("tile", get_replaced_values(currentpath + "\\Tiles\\" + tile + ".cs"), tile))
        #print(tile)

    sideFrame = Frame(root, width=150, height=600, bg=secondaryThemeColor)
    mainFrame = ScrollableWindow(root, width=850, height=600, bg=mainThemeColor, items=toadd)
    sideFrame.pack(side="left", fill="both")
    mainFrame.pack(side="right", fill="both", expand=True)
    
    canMake = Listbox(root, bg=accentColor, selectbackground=highlightColor)
    canMake.place(x=2, y=2)
    make = Button(root, bg=accentColor, activebackground=highlightColor, text="Create", height = 1, width = 16, command=createElement)
    make.place(x=2, y=180)

    Button(root, bg=accentColor, activebackground=highlightColor, text = "Main Menu", command = main_menu_back).place(x=2, y=552)

    itemsa = ['item', 'tile', 'npc', 'projectile', 'buff']
    for item in itemsa:
        canMake.insert(END, item)

def list_folders(path):
    folders = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            folders.append(item)
    return folders

def main_menu_back():
    global root
    for widget in root.winfo_children():
        widget.destroy()

    root.destroy()

    main_menu()

def readColors(file):
    global secondaryThemeColor, mainThemeColor, accentColor, highlightColor
    lines = file.readlines()
    if len(lines) >= 4:
        mainThemeColor = lines[0].strip()
        secondaryThemeColor = lines[1].strip()
        accentColor = lines[2].strip()
        highlightColor = lines[3].strip()
    else:
        print("The file does not contain enough lines.")

def main_menu():
    global root, sideFrame, mainFrame, settingsfile, modlocation, mods, currentpath, currentmod, btny, amod, items, tiles, createBtn
    # Create The Window
    root = Tk()
    root.title("TCreator - Start Menu")
    root.geometry("1000x600")
    root.resizable(0, 0)
    
    readColors(open("colors.TCtheme", "r+"))

    # Create The Side Frame
    sideFrame = Frame(root, width=300, height=600, bg=secondaryThemeColor)

    # Create The Main Frame
    mainFrame = Frame(root, width=700, height=600, bg=mainThemeColor)

    # Place Everything On The Grid
    sideFrame.grid(row = 0, column = 0)
    mainFrame.grid(row = 0, column = 1)

    # Create A List Of Mods
    settingsfile = open("settings.txt", "r+")

    for line in settingsfile:
        modlocation = line.strip()
     
    mods = list_folders(modlocation)

    currentpath = ""
    currentmod = ""

    btny = 2

    for amod in range(len(mods)):
        Button(root, text=mods[amod], height=1, width=41, bg=accentColor, activebackground=highlightColor, command=lambda amod=amod: openWorkspace(os.path.join(modlocation, mods[amod]), mods[amod])).place(x=2, y=btny)
        btny += 27

    items = []
    tiles = []

main_menu()

mainloop()

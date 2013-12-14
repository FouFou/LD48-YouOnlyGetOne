# You can place the script of your game in this file.

image lulu = "img/Lulu.png"

image bg tavern = "img/background-pink.png"
image bg outsideTavern = "img/background-orange.png"



define l = Character(_('Lulu'), color="#7BAB4D")
define a = Character(_('Anita'), color="#6496C1")
# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
  





# The game starts here.
label start:

    scene bg outsideTavern
    with fade
        #will be outside need for mead

    "At last, {i}The Need For Mead{/i}.  The old man back in that cave said this place was only supposed to be a mile down the road! Clearly he doesn't get out of that cave very often."

    "Still, there is no better place that a tavern called {i}A Need For Mead{/i} to help one get started on a heroic quest.  Might as well go inside and see what I can discover."


    scene bg tavern
    with fade

    show lulu
    l "Hello, and welcome to {i}A Need for Mead{/i}!  I am the owner and barkeep, Lulu."  

label luluMenu:
    l "Can I help you with anything?"

    menu:
        "Beverage":
            jump drink
        "Quests":
            jump quests
        "Companions":
            jump companions

label drink:
    a "I would love something to drink, if it isn't too much trouble."
    l "Well, that's what I'm here for. I have some very fine Dwarven Ale that  arrived earlier this week from beyond the Misty Mountains.  Or perhaps you would prefer something else?"
    menu:
        "Beer":
            jump beer
        "Something Else":
            jump wine

label beer:
    a "A beer would be wonderful, thank you." 
    l "An excelent choice! Here you go!"
    jump luluMenu

label wine:
    a "Actually, if you had some red wine, I would love to have a glass of it."
    l "You don't often see a Dwarf asking for wine."
    a "Just because I'm a Dwarf doesn't mean I can't appreciate beverages other than an ale or a stout!"
    l "Excellent point.  One glass of wine coming right up!"
    jump luluMenu

label quests:
    a "You wouldn't happen to know about any Quests in these parts?"
    l "I do, but I fear you must find a traveling companion, if you are to partake in such a Quest. For it is far too dangerous to go alone.  You much choose one companion to accompany you."
    menu:
        "Finding a companion":
            jump companions
        "Nevermind":
            jump luluMenu

label companions:
    a "Do you know where I could find a companion to accompany me on a Quest?"
    l "Well, you've come to the right place!  I do believe two other travelers have come in today also looking for a quest.  A Paladin and a Rogue!"
    menu:
        "Talk to the Paladin":
            jump paladin
        "Talk to the Rogue":
            jump rogue
        "Continue to talk to Lulu":
            jump luluMenu


label paladin:
    
    jump end

label rogue:
    jump end

label end:

    "Well, this bit hasn't been written yet, so The end!"





    return
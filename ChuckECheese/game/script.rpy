init python:
    renpy.music.register_channel("main_channel", loop = True)

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Charles")

define u = Character("[user]", what_color = "#0a02f0")

define audio.bg = "./audio/BackgroundTheme.wav"

define anger = 0
define sadness = 0

image bg example:
    "./images/exampleBG.jpg"
    # zoom 0.8
    # less than 1 makes it smaller
    # greater than 1 makes it bigger

image Charles base:
    "./images/MarcieBase.png"

image Charles angry:
    "./images/MarcieAngry.png"

image Usr sad:
    "./images/KiaraSad.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg example with fade
    play music bg


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Charles base

    # These display lines of dialogue.

    c "Welcome to Chuck E Cheese!"

    $ user = renpy.input("What is your name?")
    $ user = user.strip()

    hide Charles

    show User sad

    u "Nice to meet you!"

    menu:
        "Go left":
            $ anger += 1
            jump left

        "Go right":
            jump right

    # This ends the game.
    return

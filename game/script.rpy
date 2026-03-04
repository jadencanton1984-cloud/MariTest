# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define q = Character("Qieux")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene rainy city

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "After a powerful storm, the city was still trying to recover."
    
    "The streets were wet, debris scattered everywhere, and people moved slowly, exhausted from the disaster."

    "Electricity was out in many areas, but somehow, the internet was still working."

    window hide

    show phone on at truecenter with dissolve

    pause

    "Phones lit up in the darkness as people searched for updates, news, and distractions."

    hide phone on with dissolve

    show q normal at half_size with dissolve

    "While others were cleaning, repairing, and helping each other, Qieux sat quietly, glued to her phone."

    "She scrolled endlessly through social media, bored, restless, and detached from everything happening around her."

    "With nothing else to do and no electricity to power the day, her curiosity slowly turned into an idea."

    q "What if I make a harmless joke?"

    q "What if I go viral??"

    q "What if I become instantly famous?"

    "It felt exciting!"

    "Just for fun, {i}no harm{/i}"

    "At least..."

    "That’s what she thought."

    "Using an AI tool, Qieux quickly created a deepfake video and images showing the sea completely dried up,"

    "Stretching {i}empty{/i} and {i}lifeless.{/i}"

    "The details were perfect."

    "The shadows looked right."

    "The water was gone, it looked real."

    "{i}Too real.{/i}"

    "She stared at the screen, her heart racing"

    q "Oh my God…"
    
    "This is it."

    "With one tap..."
    
    "{b}She posted it.{/b}"

    "Within minutes, notifications exploded."

    "Shares multiplied. Comments flooded in."

    "People started panicking!"

    "What started as a joke turned into fear, confusion, and chaos!"

    #show q sad at half_size

    "Q’ smile slowly faded as she watched the damage unfold on her screen."

    "And in that moment, she realized..."

    "One fake post was enough to change everything."

    "Marites stared at her phone as notifications kept popping up nonstop."

    "Her post was spreading everywhere!"

    ""

    return


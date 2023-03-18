# going left dialogue
label left:
    "You went left"

    menu:
        "Go straight":
            $ anger += 2
            "You went forward"
        "Turn around":
            "You turn around"
        "Stay still":
            "You stay still"

    hide User
    show Charles angry
    c "Nice to see you again!"

    if anger > 2:
        jump angry
    elif anger == 1:
        c "I'm a little angry."
    else:
        c "I'm not angry."
return

label angry:
    c "I hate you!"

    menu:
        "I'm sorry.":
            c "I forgive you."
        "I'm not sorry.":
            $ sadness += 2
            c ":("

    while sadness > 0:
        c "That's not very nice."
        $ sadness -= 1


return

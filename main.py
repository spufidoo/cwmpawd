def on_button_pressed_a():
    global beth
    beth = "C"
    basic.show_string("C")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global beth
    beth = "T"
    basic.show_string("T")
input.on_button_pressed(Button.B, on_button_pressed_b)

beth = ""

def on_forever():
    if beth == "C":
        basic.show_string("" + str(input.compass_heading()))
    elif beth == "T":
        basic.show_string("" + str(input.temperature()))
    else:
        basic.show_string("A neu B")

basic.forever(on_forever)
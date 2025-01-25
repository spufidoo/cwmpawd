heading = 0

def on_forever():
    global heading
    heading = input.compass_heading()
    if heading > 315 and heading <= 360 or heading >= 0 and heading <= 45:
        basic.show_string("N")
    elif heading > 45 and heading <= 135:
        basic.show_string("E")
    elif heading > 135 and heading <= 225:
        basic.show_string("S")
    else:
        basic.show_string("W")
basic.forever(on_forever)

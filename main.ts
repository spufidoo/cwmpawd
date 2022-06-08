let beth = ""
input.onButtonPressed(Button.A, function () {
    beth = "C"
    basic.showString("C")
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Heart)
})
input.onButtonPressed(Button.B, function () {
    beth = "T"
    basic.showString("T")
})
basic.forever(function () {
    if (beth == "C") {
        basic.showString("" + input.compassHeading())
    } else if (beth == "T") {
        basic.showString("" + input.temperature())
    } else {
        basic.showString("A neu B")
    }
})

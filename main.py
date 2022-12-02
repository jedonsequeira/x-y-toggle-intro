def on_button_pressed_a():
    for a in range(5):
        for i in range(5):
            led.toggle(a, i)
            basic.pause(pauseLen)
            led.toggle(a, i)
            basic.pause(pauseLen)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

pauseLen = 0
pauseLen = 100
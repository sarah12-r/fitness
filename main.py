def on_button_pressed_a():
    global Hartbeat
    Hartbeat = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global Hartbeat
    Hartbeat = True
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Hartbeat = False
trace_1 = images.create_image("""
    . . . . #
    # . . . #
    # . . # .
    . # . # .
    . . # . .
    """)
trace_2 = images.create_image("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    # # # # #
    """)
trace_2.show_image(0)

def on_forever():
    global Hartbeat
    if Hartbeat:
        Hartbeat = False
        music.play(music.tone_playable(262, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        trace_1.scroll_image(1, 200)
        trace_2.scroll_image(1, 200)
basic.forever(on_forever)

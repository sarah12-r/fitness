input.onButtonPressed(Button.A, function () {
    Hartbeat = true
})
input.onGesture(Gesture.Shake, function () {
    Hartbeat = true
})
let Hartbeat = false
let trace_1 = images.createImage(`
    . . . . #
    # . . . #
    # . . # .
    . # . # .
    . . # . .
    `)
let trace_2 = images.createImage(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    # # # # #
    `)
trace_2.showImage(0)
basic.forever(function () {
    if (Hartbeat) {
        Hartbeat = false
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
        trace_1.scrollImage(1, 200)
        trace_2.scrollImage(1, 200)
    }
})

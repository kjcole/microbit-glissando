input.onButtonPressed(Button.A, function () {
    pitch = lo
    for (let index = 0; index < 880; index++) {
        pitch += slide
        music.playTone(pitch, music.beat(BeatFraction.Sixteenth))
    }
})
input.onButtonPressed(Button.AB, function () {
    toggle = !(toggle)
    music.setBuiltInSpeakerEnabled(toggle)
})
input.onButtonPressed(Button.B, function () {
    pitch = hi
    for (let index = 0; index < 880; index++) {
        pitch += 0 - slide
        music.playTone(pitch, music.beat(BeatFraction.Sixteenth))
    }
})
let toggle = false
let pitch = 0
let slide = 0
let hi = 0
let lo = 0
lo = 27.5
hi = 4186.009
slide = (hi - lo) / 880

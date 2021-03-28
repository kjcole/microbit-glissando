def on_button_pressed_a():
    global pitch
    pitch = lo
    for index in range(880):
        pitch += slide
        music.play_tone(pitch, music.beat(BeatFraction.SIXTEENTH))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global toggle
    toggle = not (toggle)
    music.set_built_in_speaker_enabled(toggle)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global pitch
    pitch = hi
    for index2 in range(880):
        pitch += 0 - slide
        music.play_tone(pitch, music.beat(BeatFraction.SIXTEENTH))
input.on_button_pressed(Button.B, on_button_pressed_b)

toggle = False
pitch = 0
slide = 0
hi = 0
lo = 0
lo = 27.5
hi = 4186.009
slide = (hi - lo) / 880
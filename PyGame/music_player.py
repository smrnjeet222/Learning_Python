from pygame import mixer

mixer.init()

mixer.music.load("song.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()

while True:
    print("Press 'p' to pause \nPress 'r' to resume")
    print("Press 'e' to exit program")
    query = input(">>>>>  ")

    if query == 'p':
        mixer.music.pause()
    elif query =='r':
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        break

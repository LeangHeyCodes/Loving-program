import time
import sys
import os

def type_writer(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def floating_hearts():
    hearts = ["💖", "💕", "💘", "💝", "❤️"]
    for i in range(15):
        print(" " * (i % 10) + hearts[i % len(hearts)])
        time.sleep(0.1)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def valentine_fancy():
    girlfriend = input("Enter your girlfriend's name: ")

    clear_screen()
    floating_hearts()
    print("\n")

    type_writer("Happy Valentine's Day ❤️\n", 0.06)

    message = f"""
I just wanted to use my coding skills to tell you
how much I love you, my dear {girlfriend}.
You light up my world, and I’m so grateful
to have you in my life.

I wrote a poem just for you 💕

Though miles stretch out between our hearts,
And distance keeps us far apart,
I feel you near in every thought and dream.
When I awake, it all feels real, it seems.

You aren’t here to comfort me,
But soon I hope you will be.
A perfect, loving, sweet girl you are,
Never truly distant, never far.

This Valentine, though I cannot hold your hand
To break the cold or help me stand,
I send a kiss through digital space,
Carried gently to your face.

You are never far from my heart.
I loved you then, I love you now.
The distance is just temporary pain—
Like waiting for a rainbow after rain.

I’m counting down the days
Until you’re here with me again.

I hope this little program puts a smile on your face 💖

With all my love,
Leang Hey ❤️
"""

    for line in message.split("\n"):
        type_writer(line, 0.03)
        time.sleep(0.2)

    print("\n")
    floating_hearts()

valentine_fancy()
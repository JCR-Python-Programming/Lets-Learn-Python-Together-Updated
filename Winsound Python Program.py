# Windows Wave Sounds Python program example

# Make Python make random sounding music that never stops playing
# via, importing Python's winsound module.

# Created by Joseph C. Richardson, GitHub.com

# You must create a sounds folder so you can keep your Windows wave sounds
# within the very same folder you will create your Windows wave sound Python
# program example as shown here.

# Step 1: Go to your C drive, then look for the Windows folder and open it.
# Step 2: Then look for Media folder and open it.
# Step 3: Select any Windows wave sounds, showing the music Icon to the left.
# Step 4: Copy any chosen Windows wave sounds and paste them into your newly
# created sounds folder, where this Windows wave sounds Python program is stored.
# Step 5: Type the name of the sound wave in a list, as shown in my Python program
# example below.

# If you like, you can also leave the sounds where they are, without the copy and paste,
# but you will have to copy down the file's path location, which for new Python programmers
# this could be quite challenging to fully understand. So I wanted to teach this in a much
# easier way so that we all can understand how to create and use wave sounds in Python.

# Step 6: Import the time module, the random module and the winsound module.

import time,random,winsound

sounds = [
    'Speech Disambiguation',
    'Speech On',
    'Windows Balloon',
    'Windows Battery Critical',
    'Windows Battery Low',
    'Windows Critical Stop',
    'Windows Default',
    'Windows Ding',
    'Windows Error',
    'Windows Exclamation',
    'ringout']

# Try these two barebones default Python program examples:

# winsound.PlaySound('Speech Disambiguation',winsound.SND_ASYNC)

# winsound.PlaySound('Speech Disambiguation',winsound.SND_ALIAS)

while True:
    random_sound = random.randint(0,10)
    print('Windows Wave Sounds Only:',sounds[random_sound])
    winsound.PlaySound(sounds[random_sound],winsound.SND_ASYNC)
    time.sleep(.3)

# You can also make wave sounds play after each one completely finishes first.

# winsound.PlaySound(sounds[random_sound],winsound.SND_ALIAS)

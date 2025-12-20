from time import sleep as delay
import os;os.system('title Knowledge Poem')
import atexit

cyan = '\033[38;2;0;255;255m'
pink = '\033[38;2;255;0;255m'

anti_flick = '\033[H'+'\033[?25l'
show_cursor = '\033[?25h\033[0m'

length = 0

def restore_terminal():
    print(show_cursor,flush = True)

atexit.register(restore_terminal)

knowledge_poem = (f'''{anti_flick}{cyan}
'Knowledge'
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream's creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.

THIS BELONGS TO EVERY MAN, WOMAN AND CHILD
Never give up your dream, no matter how far away it may seem to be, because that is when it is
ever so close to becoming true. If you dream of something long enough and strong enough, your
dream will come true, when you least expect it. Always remember, we are never too young or too
old to dream and use our imagination, for we only get one and it is ours forever. May your heart
be filled with courage and compassion, and your mind be as limitless and as wondrous as the
universe itself! If you dream it, you can be it. Believe it!''','cls',len)

while length <= knowledge_poem[2](knowledge_poem[0]):
  print(knowledge_poem[0][:length])

  delay(.05)
  length += 1

print(knowledge_poem[0])

input(f'\n{pink}Press Enter to close this Python program:')

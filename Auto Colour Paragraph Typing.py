import os;from time import sleep as wait

clear_screen='cls'

dash_paragraph_break = '-'*60

text_colours=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = light blue
    '\x1b[37m'  # index 6 = white
    )

paragraphs = f'''{text_colours[5]}{dash_paragraph_break}
  {text_colours[0]}Science is not just for smart people from a university.
  Science can and often does happen for anyone. All you
  really need is a bit of imagination and a whole lot of trial
  and error. Anyone can achieve anything they so wish. All
  you have to do is believe in yourself, while you make all
  kinds of mistakes along the way. Sooner or later, what
  doesn't work now will eventually work out, when you least
  expect it. Science and discovery is all about trial and error.
  So don't become discouraged when something won't work
  out right. Give it some time, before you know it, you will
  start to see the sparks fly...
{text_colours[5]}{dash_paragraph_break}
  {text_colours[1]}And as far as mistakes go, you are going to be in for quite
  the wild ride and a rude awakening if you think that you
  can stave them. Yet, always remember that mistakes are
  simply hidden teachers in discrete disguise. if you don't
  make mistakes, you won't learn. If you find you are making
  too many mistakes, walk away from the forest to see the
  trees. Don't give up! Take a Break instead! You will see
  them trees and when you do, the sparks will start to fly...
{text_colours[5]}{dash_paragraph_break}
  {text_colours[3]}Don't be afraid of making mistakes, they are our greatest
  lessons through life. When we learn from them, they
  become our greatest teachers through life and we
  become their greatest, lifelong student...
{text_colours[5]}{dash_paragraph_break}
  {text_colours[2]}Always remember that mistakes are Hidden Teachers in
  discrete disguise. So don't ever be afraid of making
  mistakes; they always teach us something, while we
  unwittingly achieve closer to our accomplished goal...
{text_colours[5]}{dash_paragraph_break}
  {text_colours[4]}It's because of mistakes that things are possible to
  achieve. It's because of mistakes that keep us at a
  humble stance, not getting careless or dangerous with
  the things we learn and do. Mistakes are very important
  byproducts of everything we venture into. The mistakes
  we make can lead to a far greater understanding and
  knowledge than we had ever anticipated. Imagine that?
{text_colours[5]}{dash_paragraph_break}
  {text_colours[6]}‘Knowledge’ is a free invention of the heart and of the
  mind itself! The only textbooks needed are the heart and
  the mind. The only exam to be written is the key to ponder
  into wonder. For the heart and the mind hold the key to
  the greatest diploma of all, the dream’s creation of our
  imagination. For the heart and the mind are thus, the
  greatest teachers of us… Believe in yourself! For you are
  their greatest student...

  THIS BELONGS TO EVERY MAN, WOMAN AND CHILD
  Never give up your dream, no matter how far away it may
  seem to be, because that is when it is ever so close to
  becoming true. If you dream of something long enough
  and strong enough, your dream will come true, when you
  least expect it. Always remember, we are never too young
  or too old to dream and use our imagination, for we only
  get one and it is ours forever. May your heart be filled
  with courage and compassion, and your mind be as
  limitless and as wondrous as the universe itself! If you
  dream it, you can be it. Believe it!
{text_colours[5]}{dash_paragraph_break}
  {text_colours[0]}What's behind the light beholds the answer to all things
  possible! Everyone has dreams, but it's most important
  to keep them even if they take an entire lifetime to come
  true...

  Just one very important lesson to always remember: learn
  how to play again; that’s the key to ponder into wonder.
  That’s the key which makes all dreams possible! And that’s
  the only exam to be written…
{text_colours[5]}{dash_paragraph_break}
  {text_colours[1]}GitHub username: Robomaster-S1
  https://github.com/ROBOMASTER-S1

  You can visit my GitHub Gist page for quicker access to
  these Python files and Python programs:

  I am almost a complete Walking Human Computer Science
  Research Laboratory Machine on Two Legs... 😁
'''
length=0

while length<=len(paragraphs):
  print(paragraphs[:length]);wait(.08);length+=1;os.system(clear_screen)

input(paragraphs)

# I am almost a complete Walking Human Computer Science Research Laboratory
# Machine on Two Legs... 😁

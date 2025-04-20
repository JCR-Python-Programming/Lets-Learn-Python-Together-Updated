# This is so neat! I just made this up to see if it would work.
# Watch this Python program execution/run example:

# Created by JCR, GitHub.com

# Change one of the values, then re-execute/run the Python program.

logical_list_values = ['Value','Value','Value','Value']

user_message1 = f'''All values are the same.
\n{logical_list_values[0]} {logical_list_values[1]} \
{logical_list_values[2]} {logical_list_values[3]}:
\nYou have {len(logical_list_values)} logical list values.'''

user_message2 = f'''All values are NOT the same.
\n{logical_list_values[0]} {logical_list_values[1]} \
{logical_list_values[2]} {logical_list_values[3]}:
\nYou have {len(logical_list_values)} logical list values.'''

if logical_list_values[0] is logical_list_values[1]\
   is logical_list_values[2] is logical_list_values[3]:
    print(user_message1)

else:
    print(user_message2)

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

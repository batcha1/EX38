# Aly Batch
# 11.6.19
# Doing things to lists
from typing import List

ten_things = "apples oranges crows telephone light sugar"

print("wait there are not 10 things in that list. lets fix that.")

stuff = ten_things.split(' ')
more_stuff =["day", "night", "song", "frisbee",
              "corn", "banana", "girl", "boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding: ", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now.")

    print("there we go: ", stuff)

    print("lets do some things with stuff.")

    print(stuff[1])
    print(stuff[-1])  # whoa fancy
    print(stuff.pop())
    print(''.join(stuff))  # what? xool!
    print('#'.join(stuff[3:5]))  # super stellar

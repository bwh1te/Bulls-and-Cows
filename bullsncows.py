import random
import re

print """
BULLS & COWS
 Guess a four-digit number with unique digits.
 If you guessed right digit and it's position - it's a bull.
 If you guessed right digit but it's standing on a incorrect position - it's a cow.
 Good luck!
"""

number = "".join(map(str, random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],  4) ))
print number #cheatcode

guess = 0
while not guess:
    bulls, cows = (0, 0)
    x = raw_input("Your try: ")
    if re.match('\d{4}', x) and len(x) == 4 and len(set(x)) == 4:
        if number == x:
            print "Yeah! You're right!"
            guess = 1
        else:
            for position, digit in enumerate(x):
                if str(digit) in number:
                    if number[position] == digit:
                        bulls += 1
                    else:
                        cows +=1
            print " Bulls %d Cows %d" % (bulls, cows)
    else:
        print " Incorrect input format! It should be 4 unique digits!"
from BullCow_utils import *

assert IsIsogram("banana") == False 

assert IsIsogram("bear") == True

assert IsIsogram("naughty")== True

assert IsIsogram("triangle") == True

assert IsIsogram("deadly") == False

assert IsIsogram("concluded") == False 

assert IsIsogram("gasoline") == True

assert IsIsogram("appeases") == False

assert IsIsogram("llllllll") == False

assert IsIsogram("*&^%$#") == True

assert IsIsogram("OI GOVNA") == False

assert IsIsogram("     ") == False 


assert GetBullCow("tree", "teen") == (2, 1)

assert GetBullCow ("water", "water") == (5, 0)

assert GetBullCow ("train", "train") == (5, 0)

assert GetBullCow("couple", "schizy") == (0, 1)

assert GetBullCow("bake", "cake") == (3, 0)

assert GetBullCow("carpet", "martin") == (2, 1)

assert GetBullCow ("%^&$(!", "sublime") == (0, 0)

assert GetBullCow ("12345", "darts") == (0, 0)


assert GetVaildWords(['bake', 'Bones', 'Port', 'Dream', 'lips'])== ['bake', 'Bones', 'Port', 'Dream', 'lips']

assert GetVaildWords(['drake', 'party', 'murtle', 'lollipop', 'squidward'])== ['drake', 'party', 'murtle']

assert GetVaildWords(['e', 'd', 'c', 'b', 'a'])== []

assert GetVaildWords(['starter', 'horse', 'ninja', 'pancake', 'liar'])== ['horse', 'liar']

assert GetVaildWords(['123', '321', '908', '098', '12345'])== ["12345"]

assert GetVaildWords(['@', '&', '(', ')', 'true',]) == ['true']

assert GetVaildWords(['turtle squid dogs hogs logs hundred']) == []

assert GetVaildWords([]) == []

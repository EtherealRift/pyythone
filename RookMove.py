#* * * * * * * * * 1
# - - - - - - - - 2
# - - - - - - - - 3
# - - - - - - - - 4
# - - - - - - - - 5
# - - - - - - - - 6
# - - - - - - - - 7
# - - - - - - - - 8
# * * * * * * * * *
print("Where is the rook in the x pos")
rookx = int(input(""))
print("Where is the rook in the y pos")
rooky = int(input(""))
print("Where do you want to put the rook in the x pos")
posx = int(input(""))
print("Where do you want to put the rook in the y pos")
posy = int(input(""))
if (rookx < 0 or posx < 0 or rooky < 0 or posy < 0):
    print("No negetive numbers allowed!!")
    exit()
if (rookx > 8 or posx > 8 or rooky > 8 or posy > 8):
    print("It's off the board friend")
    exit()
if (rookx == posx or rooky == posy):
    print("Correct!")
    exit()
else:
    print("Incorrect!")
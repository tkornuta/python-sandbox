from getkey import getkey, keys
key = ""
while key != 'q':
  key = getkey()
  if key == keys.UP:
    print("UP!")
  elif key == keys.DOWN:
    print("DOWN!")
  elif key == 'a':
    print("a")
  elif key == 'Y':
    print("Y")
  else:
    # Handle other text characters
    print("other")
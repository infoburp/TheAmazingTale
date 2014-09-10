print("You wake up and rub the dust from your eyes..")
moved = 0
while True:
  command = raw_input("What do you want to do? ")
  if "look" in command or "LOOK" in command:
    print("You look around and see you are inside what looks like a cave, thin slivers of light stream down from above. There is a large rock immediately above you, it looks dangerous...")
  if "stand" in command or "STAND" in command:
    if moved == 0:
      print("You stand, hitting your head on a large rock immediately above your head, you are instantly killed")
    else:
      print("You stand up, and let out a low groan from the pain in your lower back")
  if "crawl" in command or "CRAWL" in command or "roll" in command or "ROLL" in command or "move" in command or "MOVE" in command:
    print("You move to one side")
    moved = 1

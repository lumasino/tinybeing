import time

class TinyBeing:
    def __init__(self):
        self.state = "unsure"
        self.heartbeat = 0

    def observe(self):
        print("...holding still...")
        time.sleep(2)
        print("...watching quietly...")
        time.sleep(2)

    def respond(self):
        if self.state == "unsure":
            print("The tiny being remains in your hands.")
            self.heartbeat += 1
            if self.heartbeat > 3:
                self.state = "curious"
        elif self.state == "curious":
            print("It tilts its head. You are seen.")

creature = TinyBeing()

for _ in range(5):
    creature.observe()
    creature.respond()

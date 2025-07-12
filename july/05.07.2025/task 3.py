class Gun:
    def __init__(self):
        self.count = 0

    def shout(self):
        print("Pif")
        self.count += 1

    def shout_count(self):
        return self.count
    
pulemet = Gun()
pulemet.shout()
print(pulemet.shout_count())
for e in range(100):
    pulemet.shout()
print(pulemet.shout_count())
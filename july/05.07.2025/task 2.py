class House:
    def __init__(self):
        self.rooms = 3
        self.color = "grey"

    def count_room(self):
        self.rooms += 1
        return self.rooms
    
    def change_color(self, new_color):
        self.color = new_color
        return self.color
    
new_home = House()
new_home.count_room()
new_home.change_color("purple")
print(new_home.rooms)
print(new_home.color)
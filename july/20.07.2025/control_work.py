class Hero:
    def __init__(self, name, health):
        self.__name = name 
        self.__health = health
    def name(self):
        return self.__name
    
    def health(self):
        return self.__health
    
    def take_damage(self, damage):
        self.__damage = damage
        self.__health = self.__health - self.__damage
        
    def __str__(self):
        return f"Герой: {self.__name}, Здоровье: {self.__health} hp"
    
hero1 = Hero("Philosph", 100)
print(hero1)
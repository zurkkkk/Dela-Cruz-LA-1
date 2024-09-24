class mobileLegends:
    def __init__(self,heroName, heroRole, dmg_type):
        self.heroName = heroName
        self.heroRole = heroRole
        self.dmg_type = dmg_type
        
    def teamDescription(self, heroRole, dmg_type): #method
        print(f"{self.heroName} is a {heroRole} that deals {dmg_type} damage.")
        
    def __str__(self): #string manipulation
        return (f"{self.heroName} is a {self.heroRole} that deals {self.dmg_type} damage.")
    
hero = mobileLegends("Chou", "Fighter", "Physical")
print(f"{hero.heroName} is a {hero.heroRole} that deals {hero.dmg_type} damage")

hero2 = mobileLegends("Harith", "Mage", "Magic")
print(f"{hero2.heroName} is a {hero2.heroRole} that deals {hero2.dmg_type} damage")

hero3 = mobileLegends("Granger", "Marksman", "Physical")
print(hero3) #string representation/manipulation

hero4 = mobileLegends("Baxia", "Tank", "Physical")
hero4.teamDescription("Tank", "Physical")

hero4 = mobileLegends("Lancelot", "Jungler", "Physical")
hero4.teamDescription("Jungler", "Physical")

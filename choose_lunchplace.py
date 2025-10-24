import random 
# Liste des restaurants 
restaurants = [ "Viet-AN", "DICAPO", "Pizza du bout de la rue", "Boulangerie", "Choix de Victor", "Minotaure", "Pitaya", "Boulangerie de la gare"] 
# Choix aléatoire 
choix = random.choice(restaurants)

print(f"🍽️ Aujourd'hui, tu manges chez : {choix}")
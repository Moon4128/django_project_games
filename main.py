import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_collection.settings')
django.setup()

from games.models import Genre, Game

# Створюємо жанри
action = Genre.objects.create(name="Action")
rpg = Genre.objects.create(name="RPG")
strategy = Genre.objects.create(name="Strategy")

# Створюємо ігри
g1 = Game.objects.create(
    title="The Witcher 3", 
    release_year=2015, 
    rating=9.8)
g1.genres.set([rpg, action])

g2 = Game.objects.create(
    title="StarCraft II", 
    release_year=2010, 
    rating=9.0)
g2.genres.set([strategy])

g3 = Game.objects.create(
    title="God of War", 
    release_year=2018, 
    rating=9.6)
g3.genres.set([action])
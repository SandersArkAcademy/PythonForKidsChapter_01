import pickle
favorite_things = {'games' : ['board games', 'card games', 'video games'], 'watching tv' : ['anime', 'cartoons', 'youtube'], 'reading' : ['manga', 'fanfictions', 'fictional stories'], 'archery' : 'shooting arrows to hit the target???'}
favorite_things_file = open('favorites.dat', 'wb')
pickle.dump(favorite_things, favorite_things_file)
favorite_things_file.close()

load_file = open('favorites.dat', 'rb')
loaded_favorite_things = pickle.load(load_file)
load_file.close
print(loaded_favorite_things)
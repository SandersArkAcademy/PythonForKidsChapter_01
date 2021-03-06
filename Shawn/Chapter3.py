#%%

# Example of a string value.

playerName = 'Player 3'
endGameMessage = 'Your game has ended %s .'

print(endGameMessage % playerName)
# %%

#Example of a List

tasksTodo = ['Clean garage','Clean gutters']
print(tasksTodo)
tasksTodo.append('Play among us')
print(tasksTodo)
# When addressing an element in a List start count with Zero.
tasksTodo[2] = 'Really Play among us'
print(tasksTodo[2])
# %%
#Example of Tuple

tasksTodo = ('Clean garage','Clean gutters')
print(tasksTodo)
# %%

#Example of Map in other languages they are called dictionaries.
personName = 'Mr. Cheese'
voiceMailMessages = {   'Unavailable':'Hi %s is not here. Please leave a message',
                        'Available':'Hello, %s will see you shortly.'
                        }

print(voiceMailMessages['Unavailable'] % personName)
print(voiceMailMessages['Available'] % personName)

#%%

#Why is the next line going to error?
print(voiceMailMessages[0] % personName)

# %%


games = ['''Among Us''','''Legend of Zelda''','''Metroid''']
foods = ['Strawberries','Meatloaf','Spaghetti']
favorites = games + foods
#favorites.sort()
print(favorites)
# %%
buildings = 3
ninjas = 25
tunnels = 2
samurai = 40

totalCombatants = buildings*ninjas + tunnels*samurai
print(totalCombatants)
# %%
firstName = 'Shawn'
lastName = 'Sanders'
message = 'Hi there, {1} {0}.'
#print(string.format(message,firstName,lastName)); C#
print(message.format( firstName,  lastName))

# %%

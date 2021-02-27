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

#%%

# Example of a string value.

playerName = 'Player 1'
endGameMessage = 'Your game has ended %s .'

print(endGameMessage % playerName)
# %%

#Example of a List

tasksTodo = ['Clean garage','Clean gutters']
print(tasksTodo)


# When addressing an element in a List start count with Zero.

print(tasksTodo[1])
# %%
#Example of Tuple

tasksTodo = ('Clean garage','Clean gutters')
print(tasksTodo)
# %%

#Example of Map in other languages they are called dictionaries.
personName = 'Angelica'
voiceMailMessages = {'Unavailable':'Hi %s is not here. Please leave a message',
'Available':'Hello, %s will see you shortly.'}

print(voiceMailMessages['Unavailable'] % personName)
print(voiceMailMessages['Available'] % personName)

#%%

#Why is the next line going to error?
print(voiceMailMessages[0] % personName)

# %%

#import random
# randomValue = random.randint(1,20)
# print('You picked the value: %s' %(randomValue))


#from datetime import datetime as dt
#currentTime = dt.now()

#print('Your current Time is: %s.' %(currentTime))

import base64 as b64

Inara_sMessage = b'Here is my secret message.'
outputMessage = b64.b64encode(Inara_sMessage)
print(outputMessage)
decodedMessage = b64.b64decode(outputMessage)
print(decodedMessage)
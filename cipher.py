alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = 5
newMessage = ''

message = input("Please enter a message: ")

for character in message: # Checks against alphabet
    if character in alphabet: # If a character is in the alphabet then add it with encryption according to the K value
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    else: # Or else add the character without encryption
        newMessage += character

print('Your new message is', newMessage)


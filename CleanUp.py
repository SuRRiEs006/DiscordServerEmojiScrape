import time
import win32clipboard
import requests

EmojiName = [line.rstrip('\n') for line in open("EmojiName.txt")]
EmojiURL = [line.rstrip('\n') for line in open("EmojiImageURL.txt")]
print(EmojiURL)

for i in range(0,(len(EmojiName))):
    response = requests.get(EmojiURL[i])
    file = open((EmojiName[i]+".png"), "wb")
    file.write(response.content)
    file.close()
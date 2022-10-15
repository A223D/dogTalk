#A @ 66.96.162.148 n/a
from gpiozero import Button
import pygame
import pyrebase
import os
from gtts import gTTS

pygame.mixer.init()

flag=0

soundsDict1={
17: "./sounds/yes.mp3",
27: "./sounds/no.mp3",
22: "./sounds/bathroom.mp3",
10: "./sounds/treat.mp3",
9: "./sounds/walk.mp3",
11: "./sounds/food.mp3"
}

soundsDict2={
17: "./sounds/come.mp3",
27: "./sounds/good.mp3",
22: "./sounds/leave.mp3",
10: "./sounds/okay.mp3",
9: "./sounds/wait.mp3",
11: "./sounds/help.mp3"
}


config = {
"apiKey": "KEY",
"authDomain": "domain",
"databaseURL": "URL",
"storageBucket": "storage"
}

button17 = Button(17)
button27 = Button(27)
button22 = Button(22)
button10 = Button(10)
button9 = Button(9)
button11 = Button(11)
selector1 = Button(19)
selector2 = Button(26)

def playSound(soundIndex):
	if selector1.is_pressed:
		print("Selector1")
		print("Loading audio file")
		pygame.mixer.music.load(soundsDict1[soundIndex])
		print("Loaded")
	else:
		print("Selector2")
		print("Loading audio file")
		pygame.mixer.music.load(soundsDict2[soundIndex])
		print("Loaded")

	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		pygame.time.Clock().tick(10)



def stream_handler(message):
	global flag
	if flag==0:
		flag=1
		print("Ignored first iteration")
		return 6
	toSay = str(message['data'])
	print("Command", toSay)
	tts = gTTS(toSay)
	tts.save("./sounds/something.mp3")
	print("Loading audio file")
	pygame.mixer.music.load("./sounds/something.mp3")
	print("Loaded")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		pygame.time.Clock().tick(10)

firebase = pyrebase.initialize_app(config)

db = firebase.database()
my_stream=db.child("Data").stream(stream_handler)


while True:
	if button17.is_pressed:
		playSound(17)
	if button27.is_pressed:
		playSound(27)
	if button22.is_pressed:
		playSound(22)
	if button10.is_pressed:
		playSound(10)
	if button9.is_pressed:
		playSound(9)
	if button11.is_pressed:
		playSound(11)

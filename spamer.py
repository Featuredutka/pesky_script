import pyautogui
import webbrowser
import time
import random

DESIRED_URL_VK = "https://vk.com/im?sel=197528377"

TIME_FOR_WEBPAGE_OPEN = 5

phrases = ("CS idem, ili net?", "Zaletai v cs, ya uze tut", "Go katku v cs", "Ne ponyal, cs idesh chi sho?")
phrase_index = random.randrange(0, len(phrases))

webbrowser.open(DESIRED_URL_VK, new=2, autoraise=True)

time.sleep(TIME_FOR_WEBPAGE_OPEN)
pyautogui.typewrite(phrases[phrase_index])
pyautogui.press('enter')



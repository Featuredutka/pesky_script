import pyautogui
import webbrowser
import time
import random
#Hardcoded, upgrade is planned
DESIRED_URL_VK = "https://vk.com/im?sel=197528377"

# Set manually, so you might want to give this thing a test flight
TIME_FOR_WEBPAGE_OPEN = 5

#Dictionary, which can be filled. Migration to txt is planned
phrases = ("CS idem, ili net?", "Zaletai v cs, ya uze tut", "Go katku v cs", "Ne ponyal, cs idesh chi sho?")
phrase_index = random.randrange(0, len(phrases))

webbrowser.open(DESIRED_URL_VK, new=2, autoraise=True)
#TODO - Keyboard layout check (maybe use int element to define pharase's language)
time.sleep(TIME_FOR_WEBPAGE_OPEN)
pyautogui.typewrite(phrases[phrase_index])
pyautogui.press('enter')



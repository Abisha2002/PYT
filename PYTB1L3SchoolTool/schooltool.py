import time

maandag = "Je moet naar school!"
dinsdag = "Je moet naar school!"
woensdag = "Je moet naar school!"
donderdag = "Je moet naar school!"
vrijdag = "Je moet naar school!"
vrijdag = "je hebt geen school!"
zondag = "Je hebt geen school je kan uitslapen!"
x = maandag
print(type(x))

print("vul hier onder in welke dag het is ")
time.sleep(2)

maandag = True

if maandag == True:
    print("Je moet naar school vandaag!")
elif dinsdag == True:
    print("Je moet naar school vandaag!")
elif woensdag == True:
    print("Je moet naar school vandaag!")
elif donderdag == True: 
    print("Je moet naar school vandaag!")
elif vrijdag == True:
    print("Je moet naar school toe vandaag!")
else:
  print("Je hebt geen school vandaag, je kan lekker uitslapen!")

s = "Одним дождливым вечером чупакабра прогуливалась по городу. \
Увидела чебуречную и решила зайти в неё. купила чебурек, съела и отравилась. \
Чупакабры были недовольны, и потому восстали. \
Вдруг вижу яркий свет в конце тоннеля?! \
Просыпаюсь уже в мокрой постели. \
"

start_sentense = True
new_story = ''

for ch in s:
    if start_sentense == True and ch.isalpha():
       new_story += ch.upper()
       start_sentense = False
    else:
        new_story += ch

    if ch in(".!?"):
        start_sentense = True

print(new_story)
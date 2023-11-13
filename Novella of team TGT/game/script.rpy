define e = Character('Эйлин', color="#c8ffc8")
define Igor = Character('Игорь', color="")
define Kat = Character('Катя', color = "")
image logo text = Text("Спустя час", size=50)


label start:

    scene bg 1ceiling
    with Dissolve(.5)

    pause(1)

    scene bg 2telefon
    with Dissolve(.5)

    "Очередное утро"

    scene bg 3dirtybedroom
    with Dissolve(.5)

    "Обычное, практически ничем не отличающееся от любого другого,{w} но… Сегодня мне обещали прислать письмо и сообщить, возьмут ли меня на большой проект…{w} Нужно прийти в себя и проснуться окончательно."

    scene bg hallway1
    with Dissolve(.5)

    pause(1)

    scene bg kitchen
    with Dissolve(.5)

    "Надеюсь в холодильнике осталась еда…"

    scene 5holodos
    with Dissolve(.5)

    "Повезло… {w}Так, нужен план. Сейчас поем, после нужно прибраться и привести дом в порядок.{w} Раз намечается новый этап жизни, нужно войти в него красиво. Главное чтобы мне не отказали…"

    scene bg 468kitchen
    with Dissolve(.5)

    scene 7kitchen
    with Dissolve(.5)

    pause(1.5)

    scene bg 468kitchen
    with Dissolve(.5)

    scene 9food
    with Dissolve(.5)

    "Так страшно…{w} Вдруг назначат не меня? И так весь год только маленькие проекты, сколько это может продолжаться?"

    scene bg black
    with Dissolve(.5)
    show logo text:
        xalign 0.5
        yalign 0.5

    pause(2)

    scene bg bedroom
    with Dissolve(.5)

    "Ну, вроде всё…{w} Нужно проверить почту, быть может мне мне уже написали письмо?"

    scene 11mail
    with Dissolve(.5)

    "Новое письмо! Пожалуйста, хоть бы мне дали этот проект…"

    scene 12openmail
    with Dissolve(.5)

    "Неужели?! Этот проект мой!"
    "Так, спокойно, нужно обдумать всё.{w} Так, чем раньше начну, тем будет лучше. Сегодня нужно позвонить заказчику, причём желательно в ближайшее время. Но сейчас нужно успокоиться и взять себя в руки."
    "Так, сейчас зайду в кофейню, а после поеду в офис, там будет проще сориентироваться и сделать всё идеально."
    return

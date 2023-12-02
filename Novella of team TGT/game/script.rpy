﻿define igor = Character('Игорь', color="f0f0f0")
define kat = Character('Катя', color = "f0f0f0")
define zakaz = Character('Фёдор Вячеславович', color = "f0f0f0")
define random = Character('Случайный работник', color = 'f0f0f0')
define sasha = Character('Александра', color = "f0f0f0")
define michel = Character('Михаил', color = 'f0f0f0')
define valya = Character('Валентин', color = 'f0f0f0')
image logo text = Text("Спустя час", size = 50)
image logo text2 = Text("Спустя 2 часа", size = 50)
image logo text3 = Text("Спустя несколько минут", size = 50)
image logo text4 = Text("Спустя неделю", size = 50)


label start:

    scene bg 1ceiling
    with Dissolve(.5)

    pause(1)

    scene bg 2telefon
    with Dissolve(.5)

    "Очередное утро"

    scene bg 3dirtybedroom
    with Dissolve(.5)

    "Обычное, практически ничем не отличающееся от любого другого,но… {w}  Сегодня мне обещали прислать письмо и сообщить, возьмут ли меня на большой проект…"
    "Нужно прийти в себя и проснуться окончательно."

    scene bg hallway1
    with Dissolve(.5)

    pause(1)

    scene bg kitchen
    with Dissolve(.5)

    "Надеюсь в холодильнике осталась еда…"

    scene 5holodos
    with Dissolve(.5)

    "Повезло… {w}Так, нужен план. Сейчас поем, после нужно прибраться и привести дом в порядок."
    "Раз намечается новый этап жизни, нужно войти в него красиво. Главное чтобы мне не отказали…"

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
    "Так, спокойно, нужно обдумать всё.{w} Так, чем раньше начну, тем будет лучше. Сегодня нужно позвонить заказчику, причём желательно в ближайшее время."
    "Но сейчас нужно успокоиться и взять себя в руки."
    "Так, сейчас зайду в кофейню, а после поеду в офис, там будет проще сориентироваться и сделать всё идеально."

    scene bg black
    with Dissolve(.5)
    show logo text2:
        xalign 0.5
        yalign 0.5

    pause(2)

    scene 21pict
    with Dissolve(.5)

    pause(2.0)

    scene 22pict
    with Dissolve(.5)

    pause(2.0)

    scene 23pict
    with Dissolve(.5)

    pause(2.0)

    scene 24pict
    with Dissolve(.5)

    igor"Здравствуйте, Фёдор Вячеславович?"
    zakaz"Здравствуйте, да, кто беспокоит?"
    igor"Извините, не представился. Меня зовут Игорь Евгеньевич, я представляю компанию BDR. Вы заказывали у нас проект, все верно?"
    zakaz"Да, Игорь Евгеньевич, совершенно верно. Давайте я приеду в ваш офис через час, обсудим детали. Я надеюсь вы сможете в это время меня встретить?"
    igor"Да, конечно, жду, как приедете - поднимайтесь на 17 этаж, там вас встретит секретарша и проводит до переговорной."
    zakaz"Хорошо, до свидания."

    "Хм, даже интересно что там за проект… Целый час ждать, надо себя хотя бы чем-то занять, чтобы не думать об этом и не переволноваться."
    "Как минимум проверить переговорную: вдруг там грязно, или она через час будет занята?"

    scene 25pict
    with Dissolve(.5)

    "Сначала посмотрю что в переговорной с овальным столом. Если она окажется кем-то занята на это время, пойду в другую."

    scene 26pict
    with Dissolve(.5)

    "О, 14:00 никем не занято, как удачно! Нужно вписать сюда себя, чтобы комнату никто неожиданно не занял."

    scene 27pict
    with Dissolve(.5)

    "Надеюсь за час успеем решить часть вопросов, необходимых для начала работы."

    scene 28pict
    with Dissolve(.5)

    "Чёрт, почему это никто не убирает?"

    scene 29pict
    with Dissolve(.5)

    igor"ЭЙ! Кто-то знает где наш уборщик? Почему в переговорной мусор?"

    show random:
        xalign 0.75
        yalign 1.0

    random"Официально заболел, но по слухам перебрал на выходных с алкоголем, поэтому не вышел. Уволить бы за такое по-хорошему…"

    hide random

    scene 28pict
    with Dissolve(.5)

    "Даже дослушивать эту душераздирающую историю не хочу. Вот вам и PM: позвони, приберись, обсуди, команду набери, всё организуй и получи по голове за какие-то недочёты."
    "Ладно, убирать тут в целом не так уж и много, слава богу не квартира какой-нибудь бабушки с 50 собаками и тараканами, а всего лишь несколько бутылок воды и упаковок от снеков."

    scene bg black
    with Dissolve(.5)
    show logo text:
        xalign 0.5
        yalign 0.5

    pause(1.0)

    scene 211pict
    with Dissolve(.5)

    "Ну, вроде все готово. Вода, бумага с ручкой, чистая переговорная, секретарша предупреждена о необходимости проводить сюда заказчика, так что остаётся ждать."
    "С минуты на минуту уже должен прийти."

    scene bg black
    with Dissolve(.5)
    show logo text3:
        xalign 0.5
        yalign 0.5

    pause(1.0)

    scene 211pict
    with Dissolve(.5)

    show fedor simple:
        xalign 0.75
        yalign 1.0
    with Dissolve(.5)

    zakaz"Здравствуйте, Игорь Евгеньевич?"
    igor"Здравствуйте, да, проходите! Сразу к делу, верно? Расскажите, какой конкретно проект вам нужен."

    hide fedor simple

    show fedor rass:
        xalign 0.75
        yalign 1.0

    zakaz"Знаете систему социального рейтинга в Китае? Так вот, я получил разрешение от губернатора региона на реализацию подобного проекта. Мне от вас эта система как раз таки нужна."

    hide fedor rass

    show fedor happy:
        xalign 0.75
        yalign 1.0

    zakaz"Опробуем сначала на небольшом городе, и если властям это понравится, будем внедрять в большие города и распространять по всей стране."

    hide fedor happy

    show fedor sad:
        xalign 0.75
        yalign 1.0

    zakaz"Да, займет это, конечно, уйму времени, да и средств потребует немало, но такая система поможет сделать общество лучше. По крайней мере я в это верю."

    hide fedor sad

    show fedor rass:
        xalign 0.75
        yalign 1.0

    zakaz"Суть вот в чём: в небольшом экспериментальном городе мы установим огромное количество камер,будем собирать данные о населении:"
    zakaz"справки из налоговой, полиции, документы с места работы, чеки из магазинов и так далее."
    zakaz"Ваше приложение должно будет анализировать записи с камер и в зависимости от действий людей менять их рейтинг."
    zakaz"Плюнул, допустим, на дорогу, водки бутылку купил - система снизит его рейтинг."
    zakaz"Высадил дерево возле леса, котёнка бездомного покормил - система добавит ему баллов."
    zakaz"То же самое и с документами. А этот социальный рейтинг конвертируется в бонусы или штрафы."
    zakaz"Ну, к примеру, за идеальный рейтинг налоги уменьшаются на 10 процентов, скидка в магазине на какие-то товары."
    zakaz"А за низкий рейтинг не будут принимать на высокооплачиваемую работу, разрешать брать кредиты, машину в каршеринге."
    igor"Хм, звучит интересно, но реализовать будет трудно."
    zakaz"Не переживайте, деньги выделю, время тоже, работайте, главное результат дайте. Буду раз в неделю-две контролировать ваш прогресс лично, может иногда помощников отправлять буду."
    zakaz"Как считаете, по времени за сколько уложитесь? Сколько рублей вложить в проект придется?"
    igor"Честно говоря, сложно ответить так сразу. Я отчитаюсь вам на почту, как определюсь с этим."

    hide fedor rass

    show fedor simple:
        xalign 0.75
        yalign 1.0

    zakaz"Нет, не нужно, расскажите лично, когда приеду в следующий раз. Так, про работу с данными я рассказал, теперь про само приложение на телефоны граждан."

    hide fedor simple

    show fedor happy:
        xalign 0.75
        yalign 1.0

    zakaz"Сделайте по дизайну его патриотичным, цвета флага добавьте обязательно, красиво оформите город проживания - герб этого города добавить рядом с названием."

    hide fedor happy

    show fedor rass:
        xalign 0.75
        yalign 1.0

    zakaz"Должно быть меню, где будет указано место работы, жительства и прочие данные о человеке, чтобы проще было следить за его активностями и поощрять."
    zakaz"При переезде в другой город человек должен будет уведомить, документы подать, для этого тоже функции должны быть."
    zakaz"Обязательно вкладку с историей изменения рейтинга, чтобы человек знал, за что его штрафуют, а за что хвалят, и менял поведение в лучшую сторону."
    zakaz"Нужна в главном меню и сама шкала социального рейтинга - от 0 до 1000, соответствующие преимущества для данного рейтинга."
    zakaz"Отдельное меню с ближайшими мероприятиями, за посещение которых можно баллы получить."
    zakaz"Например, доклад какого- нибудь учёного, спектакль или что-то подобное."
    zakaz"Эти данные в будущем будут вносить мэры городов, вам не нужно лично всё туда писать, просто сделайте возможность властям редактировать эти мероприятия."

    hide fedor rass

    show fedor simple:
        xalign 0.75
        yalign 1.0

    zakaz"Этого пока что будет достаточно. В процессе работы в случае необходимости внесём дополнительные корректировки, чтобы сделать эту систему ещё лучше. Вам всё понятно?"
    igor"Да, кажется да. Тогда сегодня же и начну свою работу."

    hide fedor simple

    show fedor happy:
        xalign 0.75
        yalign 1.0

    zakaz"Замечательно. Значит через неделю можно будет приехать и посмотреть на первые результаты?"
    igor"Ммм, думаю что нет. Сначала нужно собрать команду, объяснить им всё, пообсуждать вопросы и так далее."
    igor"Я вам напишу или позвоню, когда можно или нужно будет приехать, ориентировочно, я полагаю, это будет через две недели."

    hide fedor happy

    show fedor simple:
        xalign 0.75
        yalign 1.0

    zakaz"Хорошо, тогда я жду вашего звонка. Удачной и продуктивной работы, до свидания!"

    hide fedor simple
    with Dissolve(.5)

    "Да, реализовать этот проект будет адски трудно. Сегодня нужно начать искать сотрудников, без них никуда."
    "Итак, в первую очередь нужны маркетологи, дизайнеры и разработчики, а после них обязательно тестировщики, чтобы все баги решить до выхода приложения."

    scene bg black
    with Dissolve(.5)
    show logo text4:
        xalign 0.5
        yalign 0.5

    pause(1.0)

    scene bg 1ceiling
    with Dissolve(.5)

    pause(1.0)

    scene bg bedroom
    with Dissolve(.5)

    "Наконец-то этот день настал! Команда собрана, и сегодня работа над проектом уже начнется."
    "Нужно позавтракать и ехать в офис, чтобы прибыть первым и подготовить полный рассказ о предстоящей работе."

    scene bg black
    with Dissolve(.5)
    show logo text2:
        xalign 0.5
        yalign 0.5

    pause(1.0)

    scene 215pict
    with Dissolve(.5)

    "Итак, цель на сегодня - рассказать главам отделов о том, что я от них жду. Речь навыступление перед ними уже готова, так что остаётся лишь дождаться, пока все прибудут."

    show kat happy:
        xalign 0.75
        yalign 1.0
    with Dissolve(.5)

    igor"Ого, как быстро! До назначенного времени ещё 15 минут!"
    kat"Я надеюсь это не повод меня выгнать отсюда, верно?"
    igor"Нет, конечно нет! Проходи, располагайся как тебе удобно, все остальные тоже скоро должны прийти."

    hide kat happy
    with Dissolve(.5)

    scene bg black
    with Dissolve(.5)
    show logo text3:
        xalign 0.5
        yalign 0.5

    pause(1.0)

    scene 215pict
    with Dissolve(.5)

    show sasha simple:
        xalign 0.55
        yalign 1.0
    with Dissolve(.5)

    show michel simple:
        xalign 0.85
        yalign 1.0
    with Dissolve(.5)

    michel"Всем привет!"
    igor"Привет, ребята! Опоздали на минуту, но в целом ничего страшного. Не видели там в коридоре Валентина?"
    igor"Я конечно понимаю, что до этапа тестировки функций ещё далеко, но всё равно он тут нужен."
    sasha"Нет, не встречали. Может в пробках задерживается?"
    michel"Думаю, хотя бы минут пять подождать мы точно можем."
    igor"Ладно, подождём. А я пока за кофе схожу. Если он не придёт, когда я вернусь, начнём без него."

    hide sasha simple
    with Dissolve(.5)

    hide michel simple
    with Dissolve(.5)

    scene bg black
    with Dissolve(.5)
    show logo text3:
        xalign 0.5
        yalign 0.5

    scene 215pict
    with Dissolve(.5)

    show valya happy:
        xalign 0.75
        yalign 0.5
    with Dissolve(.5)

    igor"О, а вот и ты!"
    valya"Да, опоздал на пять минут. Было интересно проверить, начнёте ли вы без меня, если я опоздаю. Не зря же я тестировщик!"
    igor"Ты везде используешь возможности что-то протестировать?"
    valya"Именно так! Я поэтому эту профессию и выбрал, что с детства создавал множество проблем своими проверками различных возможностей всего, что попадалось мне на глаза."

    hide valya happy

    show valya louf:
        xalign 0.75
        yalign 0.5

    valya"Однажды даже тестировал вилкой розетку, к счастью родители вовремя заметили это и предотвратили."

    hide valya louf

    show valya happy:
        xalign 0.75
        yalign 0.5

    valya"Надеюсь в рамках этого проекта такие тесты проводить мне не придётся, хотя я готов на всё ради успеха проекта!"
    igor"В моих планах не было проведения таких тестов. Всё, что тебе угрожает, это штрафы или выговоры, если будешь ещё проводить эксперименты с опозданиями."

    hide valya happy

    show valya louf:
        xalign 0.75
        yalign 0.5

    valya"Ой-ой, не надо! Буду приходить вовремя!"
    igor"Вот и хорошо. А теперь пойдём в переговорную. Хотел кофе взять, пока тебя нет, но видимо не судьба."


    return

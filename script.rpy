# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define Me = Character('Я', color="84c3be")
define pupil1 = Character('Одноклассник', color="#c8ffc8")
define mom = Character('Мать', color="ff9baa")
define taisia = Character('Ученица №1', color="fc89ac")
define polina = Character('Полина', color="f78fa7")
define vadim = Character('Вадим', color="42aaff")
define sonia = Character('Соня', color="de5d83")
define mishab = Character('Миша', color="5d76cb")
define ok = Character('Леша ОК', color="fefe22")
define teacher = Character('Учитель', color="acb78e")
define vasiliy = Character('Ученик')
define ikir = Character('Ученик')
define mitya = Character("Митя", color="ffffff")
define van = Character('Иван Даркохльмов-Спайд', color = "f0f0f0")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

init:
    $ strength = 5
    $ intellect = 5
    $ beaty = 5
    $ alco = False
    $ smoke = False
    $ lagguage = []
    $ badCompRep = 0 #"плохие" парни
    $ goodCompRep = 0 #обычные челики
    $ musCompRep = 0 #меланхоличная компания
    $ teachersRep = 0 #преп. состав
    $ name = "Артем" 
    $ reputation = {} #репутация отделньых людей
    $ flags = []
    $ qLocs = {} #номер будущего квеста в локации

    python:
        
            import math

            class Shaker(object):
            
                anchors = {
                    'top' : 0.0,
                    'center' : 0.5,
                    'bottom' : 1.0,
                    'left' : 0.0,
                    'right' : 1.0,
                    }
            
                def __init__(self, start, child, dist):
                    if start is None:
                        start = child.get_placement()
                    #
                    self.start = [ self.anchors.get(i, i) for i in start ]  # центральная позиция
                    self.dist = dist    # максимальное расстояние, в пикселях, от начальной точки
                    self.child = child
                    
                def __call__(self, t, sizes):
                    # Число с плавающей точкой в целое число... превращает числа с плавающей точкой
                    # в целые.      
                    def fti(x, r):
                        if x is None:
                            x = 0
                        if isinstance(x, float):
                            return int(x * r)
                        else:
                            return x

                    xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                    xpos = xpos - xanchor
                    ypos = ypos - yanchor
                    
                    nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                    ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                    return (int(nx), int(ny), 0, 0)
            
            def _Shake(start, time, child=None, dist=100.0, **properties):

                move = Shaker(start, child, dist=dist)
            
                return renpy.display.layout.Motion(move,
                              time,
                              child,
                              add_sizes=True,
                              **properties)

            Shake = renpy.curry(_Shake)


# Игра начинается здесь:
label start:

    $ strength = 5
    $ intellect = 5
    $ beaty = 5
    $ alco = False
    $ smoke = False
    $ lagguage = []
    $ badCompRep = 0 
    $ goodCompRep = 0 
    $ musCompRep = 0 
    $ reputation = {'Сердюк': 0}
    $ teachersRep = 0
    $ flags = []
    $ day = 1
    $ qLocs = {
    "Сарай": 1, "Сарай мал": 1, "Дом": 1,
    "Гараж": 1, "Свалка": 1, "Дрова": 1, 
    "Дом мал": 1, "Реактивы": 1, "Лес": 1,
    "Баня": 1
    }

    scene bg old school
    "Восемь лет я учился в обычной школе"

    "Мои одноклассники были кретинами, которые абсолютно не хотели учиться"
    show pupil1 asks
    pupil1 "Есть мегахорошее предложение прогулять завтра матешу и пойти бухнуть"
    menu:
        "Бухнуть или учиться?"

        "Согласиться":
            pupil1 "Маладца"  
            $ badCompRep += 1
            $ alco = True

        "Прости, у меня завтра дела после урока":
            pupil1 "Ну ладно"

        "Не хочу прогуливать урок":
            pupil1 "Ботан"
            $ teachersRep += 1
            $ intellect += 1

    hide pupil1 asks

    "Учителя мне тоже не нравились, ведь объясняли очень мало."
    "У меня все хорошо получалось, поэтому я часто хотел забить на домашние задания"

    show pupil1 asks
    pupil1 "Предлагаю после уроков в скейт парк, мы пару сигарет возьмем"
    menu:
        "Пойти с одноклассниками или остаться дома?"

        "Согласиться":
            pupil1 "Смотри, не упади"
            $ badCompRep += 1
            $ strength += 1
            $ smoke = True

        "Согласиться, но отказаться курить":
            pupil1 "Маменькин сынок"
            $ strength += 2

        "Сорян, не смогу":
            pupil1 "Ну тогда в другой раз"

        "Я еще домашки не сделал":
            pupil1 "Душнила"
            $ teachersRep += 1
            $ intellect += 1


    hide pupil1 asks
    "Но однажды произошло событие, которое навсегда изменило мою жизнь"
    hide bg old school

    show bg home

    show mom
    mom "Сынок, я нашла тебе хорошую школу. № 179, если я не ошибаюсь. Очень советую тебе посмотреть."
    mom "Сын моей подруги учится там в изобреательском классе. Говорят, у них появилось вакантное место."
    hide mom
    "Я посмотрел про школу и она мне очень понравилась. Я решил поступать."
    hide bg home

    show bg sch179
    "Я пришел на поступление и сдал все письменные и устные экзамены."
    "Меня высоко оценили и я прошел на последнее испытание"
    hide bg sch179

    show bg home
    show mom
    mom "Сын, ты молодец. Мне написали, что ты прошел на последнее испытание."
    mom "Мне на почту написали, что ты поедещь в какую-то Хрипань. Там на тебя неделю посмотрят и если ты понравишься, то возьмут."
    mom "Выезд послезавтра, тебе надо собраться."
    hide mom

    jump preparation

    return

label preparation:

    "Места немного, поэтому надо взять только самое необходимое"

    menu:
        "Что взять с собой?"

        "Умные книги" if intellect > 5:
            $ intellect += 1
            $ strength += 1
            $ lagguage.append('Книга')

        "Биту" if strength > 5:
            $ strength += 2
            $ intellect -= 1
            $ lagguage.append('Бита')  

        "Бутылку вина" if alco:
            $ lagguage.append('Вино') 

        "Пачку сиг" if smoke:
            $ lagguage.append('Сиги')

        "Сиги и бутылку вина" if smoke and alco:
            $ lagguage.append('Вино')
            $ lagguage.append('Сиги')

        "Поезать налегке":
            $ intellect -= 1
            $ strength -= 1
            $ lagguage.append('Лишнее место') 
            hide home

            jump station

    "В рюкзаке осталось еще немного места"

    menu:
        "Что еще взять?"

        "Петарду":
            $ lagguage.append('Петарда')

        "Консервы":
            $ lagguage.append('Консервы')  

        "Виниловую пластинку":
            $ lagguage.append('Пластинка')  
            $ musCompRep += 1

        "Ничего":
            $ lagguage.append('Лишнее место')    

    "Я взял [lagguage[0]], [lagguage[1]]"

    hide home

    jump station


    return


label station:

    show bg station

    "И вот я уже стою на вокзале."
    "На станции стояла группа людей, среди которых я узнал и преподавателей, которые принимали у меня экзамены."
    "Я подошел к ним и поздоровался"
    Me "Здравствуйте"

    show teacher

    teacher "Ну здравствуй."
    teacher "Вижу, что ты новый поступающий. Ух и сложно же тебе придется!"
    hide teacher

    jump stationDialog

    return

label stationDialog:

    show teacher at right
    show vasiliy at left
    show ikir at left:
        xalign 0.25
        yalign 1.00
    teacher "Пока познакомься с ребятами, вон они там стоят"
    hide teacher

    $ reputation['Пушкин'] = 0
    $ reputation['Кирюха'] = 0

    menu:
        "К кому подойти?"

        "К пацану слева":
            $ goodCompRep += 1
            $ reputation['Пушкин'] += 1
            jump vasiliyDialog

        "К панку справа":
            $ badCompRep += 1
            $ reputation['Кирюха'] += 1
            jump ikirDialog

    return



label vasiliyDialog:
    hide ikir
    hide vasiliy
    show vasiliy:
        zoom 1.50
        xalign 0.50
    Me "Привет я [name], а как тебя зовут?"
    vasiliy "Я Вася"
    $ vasiliy = "Вася"
    vasiliy "А ты в будешь в нашем калссе учиться?"
    Me "Ну я пока полностью не поступил, Хрипань - послдений этап. Как там все происходит, кстати?"
    vasiliy "Я там еще ни разу не был, но мне одноклассники рассказывали."
    vasiliy "Говорят, там много работать надо, но я точно не знаю."
    hide vasiliy
    jump train

    return

label ikirDialog:
    hide vasiliy
    hide ikir
    show ikir:
        zoom 1.50
        xalign 0.50
    Me "Здарова"
    ikir "Привет"
    Me "Я вот новый поступающий в 9 класс, мне сказали, что Хрипань - полседний этап поступления"
    Me "Что вообще делают в Хрипани?"
    ikir "Для начала, надо туда добраться."
    ikir "Это тяжело, ведь нас может забрать ведьма из Шатурских болот. Или на крайний случай Шаурмян."
    menu:
        "Что за фигню ты говоришь":
            $ badCompRep -= 1
            Me "Что ты за бред несешь?"
            $ reputation['Кирюха'] -= 2
            ikir "Неумение слушать элитных педобиров до добра тебя не доведет, учти"
        "Спокойно слушать":
            pass
    ikir "Как только мы туда доедем, всех новичков отправляют откачивать канализацию, а вот что дальше сам узнаешь."
    hide ikir
    jump train

    return


label train:
    

    show teacher
    teacher "Ну все, пора ехать"
    hide teacher
    hide bg station
    show bg train

    "Я сел в электричку"
    

    jump trainDialog

    return

label trainDialog:

    with Shake((0, 0, 0, 0), 1.5, dist=15)
    
    show sonia:
        xalign 0.25
        yalign -0.20
        zoom 1.25
    show mishab:
        xalign 0.70
        zoom 1.25
    show polina at right
    show polina at right:
        zoom 0.90
    show taisia
    show taisia:
        zoom 0.90
    show vadim at left:
        xalign 0.00
    show vadim at left:
        zoom 1.50
        yalign -0.05

    "В электричку завалилась странная кампания моих ровесников"
    "У всех были походные рюкзаки и спальники, а у некоторых гитары"

    taisia "Привет всем"

    hide sonia
    hide polina 
    hide vadim
    hide mishab

    show taisia at left:
        zoom 0.85
    show teacher
    teacher "Привет, Тася, Вадим, Полина, Соня"
    $ taisia = "Тася"
    hide teacher
    hide taisia
    hide bg train

    show bg train full
    

    $ reputation['Тася'] = 0
    $ reputation['Полина'] = 0
    $ reputation['Соня'] = 0
    $ reputation['Вадим'] = 0
    $ reputation['Миша Б'] = 0

    "Ребята расселись по поезду"
    "Я могу присоединиться к ним или сесть одному"

    menu:
        "К кому подойти?"

        "К группе слева":
            hide bg train full
            jump taisiaDialog

        "К группе справа":
            hide bg train full
            jump soniaDialog
            
        "К алкашам в соседнем вагоне":
            pass

        "Ни к кому":
            hide bg train full
            jump loneTrain
    

    return

label taisiaDialog:
    show bg train window
    show taisia sits:
        xalign 1.00
        yalign 0.90
    show vadim sits:
        xalign 0.15
        yalign 0.90
        zoom 1.25
    $ reputation['Тася'] += 1
    $ reputation['Вадим'] += 1
    $ goodCompRep += 1
    $ badCompRep += 1
    Me "Привет, я [name]"
    taisia "Здарова"
    Me "Расскажите мне про Хрипань"
    taisia "Хрипань - такое прекрасное место, где мы люди много работают."
    Me "А что мы там делать будем?"
    taisia "Люди клаудт плитку и красят стены, а также ликвидируют потопы в канализации"
    vadim "Тебя закидают работой, и ты не будешь спать"
    taisia "Вобщем прекрасное место"
    vadim "там есть много выборов что сделать: разносить стены, разбирать кровати, класть плитку, готовить, штукатурить, в общем много всего."
    Me "А отдыхать там дают?"
    taisia "Совсеем немного и только после полуночи"
    "В приятных беседах мы провели всю поездку"
    hide taisia
    hide vadim
    hide bg train
    jump arrival
    return

label soniaDialog:
    show bg train window
    show mishab half:
        xalign 0.60
        yalign 0.50
    show polina sits:
        xalign 1.15
        yalign 0.90
        zoom 1.25
    show sonia sits:
        xalign 0.15
        yalign 0.90
    $ reputation['Соня'] += 1
    $ reputation['Полина'] += 1
    $ reputation['Миша Б'] += 1
    $ goodCompRep += 2

    Me "Расскажите мне про Хрипань"
    polina "Это место, где тебя закидают работой, и ты не будешь спат"
    Me "А что мы там делать будем?"
    mishab "Стены утеплять, шкафы и кровати таскать, ну ты увидишь"
    sonia "Кстати, мы с Тасей и Полиной собираемся плитку в подвале класть, не хочешь нам помочь?"
    menu:
        "Согласиться":
            sonia "Круто, будет весело"
            $ reputation['Соня'] += 2
            $ flags.append('Плитка')

        "Отказаться":
            sonia "Жаль"
            $ reputation['Соня'] -= 1

        "Если будет возможность":
            sonia "Главное не забудь"
            $ reputation['Соня'] += 2
            $ flags.append('Плитка В')

    "В приятных беседах мы провели всю поездку"

    hide sonia
    hide polina
    hide mishab

    jump arrival
    return


label loneTrain:
    show bg train window
    "Я стесняюсь и не знаю, к кому подсесть"
    "Придется ехать в гордом одиночесвте"
    "От скуки я засыпаю."

    hide bg train
    with fade
    jump arrival
    
    return

label arrival:
    show bg arrival
    "Вот мы и приехали"
    show teacher
    teacher "Идем"
    hide teacher

    hide bg arrival
    show bg shawa
    pause
    hide bg shawa  
    show bg road
    pause
    hide bg road
    show bg road 2
    pause
    hide bg road 2

    jump chripanArrival

    return

label chripanArrival:
    show bg chripan
    show teacher

    teacher "Вот мы и пришли"

    hide teacher

    show taisia:
        zoom 0.95
        xalign 0.50
        yalign -0.10

    taisia "Это база"

    hide taisia

    hide bg chripan

    show bg chripan home

    show ok

    ok "Привет"
    ok "Для новоприбывших меня зовут Леша или Леша ОК"
    ok "Нужно работать, задач очень много. Поэтому мы распределим задачи. Но сначала вас нужно заселить."

    hide ok
    show hata
    show ok

    ok "Вот ваша комната"

    hide ok
    
    "Передо мной предстала довольно просторная комната с большим оличеством двухярусных кроватей"

    hide hata
    show hata full

    "Мы спокойно разместились в комнате"
    "Пришло время поработать"

    hide hata full 

    "Мы пошли искать препов, они оказались на заднем дворе Хрипани"

    hide chripan
    show bg hripan back
    show ok
    ok "Есть следующий фронт работ"
    ok "Нужно положит плитку в подвале, перенести шкафы в малый дом из сарая и помочь Мите, он сейчас в гараже"
    hide ok
    hide bg hripan back
    jump map

    return

label map:

    window hide

    $ result = renpy.imagemap("map.png", "map 2.png", [
    (644, 46, 890, 220, "Сарай"),
    (910, 101, 966, 216, "Сарай_мал"),
    (1135, 180, 1419, 504, "Дом"),
    (1423, 286, 1500, 490, "Гараж"),
    (0, 900, 1920, 1080, "Лес"),
    (881, 431, 968, 619, "Дрова"),
    (1295, 795, 1406, 913, "Дом_мал"),
    (1407, 828, 1440, 905, "Реактивы"),
    (490, 270, 794, 655, "Свалка"),
    (320, 572, 511, 760, "Баня")
    ])

    window show
    call questChooser(result) from _call_questChooser
    return

label questChooser(lName = ''):
    $ qLocs[lName] += 1
    $ lName = lName + str(qLocs[lName] - 1)
    if renpy.has_label(lName):
        jump expression lName
    else:
        "На месте никого не оказалось"
        jump map
    return


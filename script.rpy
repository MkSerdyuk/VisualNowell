# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define Me = Character('Я', color="84c3be")

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


    define pupil1 = Character('Одноклассник', color="#c8ffc8")

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
    define mom = Character('Мать', color="ff9baa")

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

        "Презервативы":
            $ lagguage.append('Презервативы')

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
    define teacher = Character('Учитель', color="acb78e")
    define vasiliy = Character('Ученик')
    define ikir = Character('Ученик')
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
    
    define taisia = Character('Ученица №1', color="fc89ac")
    define polina = Character('Полина', color="f78fa7")
    define vadim = Character('Вадим', color="42aaff")
    define sonia = Character('Соня', color="de5d83")
    define mishab = Character('Миша', color="5d76cb")
    
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

    define ok = Character('Леша ОК', color="fefe22")

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
    ok "Нужно положит плитку в подвале, перенести шкафы в малый дом из сарая и помочь Мите, он сейчас в доме"
    hide ok
    hide bg hripan back
    jump map

    return

label map:

    window hide

    $ result = renpy.imagemap("map.png", "map 2.png", [
    (644, 46, 890, 220, "Сарай"),
    (910, 101, 966, 216, "Сарай мал"),
    (1135, 180, 1419, 504, "Дом"),
    (1423, 286, 1500, 490, "Гараж"),
    (0, 900, 1920, 1080, "Лес"),
    (881, 431, 968, 619, "Дрова"),
    (1295, 795, 1406, 913, "Дом мал"),
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

label Дом1:
    $ flags.append('Самогон')
    show mitya sits
    define mitya = Character("Митя", color="ffffff")
    $ reputation['Митя'] = 0
    mitya "Сегодня мы будем гнать самогон"
    mitya "Чтобы получить качетсвенный продукт нужно приложить много труда"
    mitya "Сегодня мы будем искать все необходимые реактивы"
    mitya "В первую очередь нам нужен сахар и фрукты"
    mitya "Фрукты я поищу сам, а сахар скорее всего в бане"
    hide mitya sits
    jump gym1
    return

label gym1:
    show bg bania
    "Я подошел к бане"
    "Она оказалась просто шикарной"
    "Ни разу не видел такого шикарного строения"
    hide bg bania
    show bg bania hall
    "Я зашел внутрь"
    show taisia warrior
    taisia "Хочешь заиметь право на пососать член?"
    menu:
        "Хочешь заиметь право на пососать член?"
        "Нет, спасибо":
            "Жаль, раньше у тебя хорошо получалось"
            jump gymInside
        "Да, конечно":
            jump suction
            $ reputation['Тася'] += 3
        "Отсоси потом проси" if 'Бита' in lagguage or strength > 7:
            jump fight
            $ reputation['Седюк'] += 3


    return

label fight:
    show taisia warrior at right
    show van
    define van = Character('Иван Даркохльмов-Спайд', color = "f0f0f0")
    van "Кто дерется в моем gym?"
    hide taisia warrior
    jump suction
    return

label suction:
    "Пришлось немного пососать"
    $ badCompRep -= 2
    hide van
    hide taisia warrior
    jump gymInside
    return

label gymInside:
    "Чтобы со мной не происходило, надо найти сахар"
    hide bg bania hall
    show bg bania room
    "Надо найти сахар"
    menu:
        "Где может быть сахар"
        "Поискать под шконарем":
            $ lagguage.append('Сахар')
            hide bg bania room
            jump getShugar
        "Поискать под лавкой":
            "Под лавкой я нашел только "
        "Позвать кого-нибудь помочь в поисках":
            show van
            van "My Boy Next Door, для тебя все есть"
            $ lagguage.append('Сахар')
            "Пришлось немного пососать"
            $ badCompRep -= 2
            $ reputation['Тася'] += 3
            $ reputation['Сердюк'] += 3
            "Ну хоть сахар будет"
            hide van
            hide bg bania room
            jump getShugar
           


    return

label getShugar:
    show bg sugar
    "А вот и долгожданный ингридиент для самогона"
    "Надо отнести его Мите"
    hide bg sugar
    jump ДомMitya
    return

label ДомMitya:
    show bg laba
    show mitya
    mitya "Здарова"
    if 'Сахар' in lagguage:
        mitya "О, ты принес сахар"
        jump startTravel
    else:
        $ reputation['Митя'] -= 1
        mitya "Иди поищи еще раз"
        hide mitya
        hide bg laba
        jump gymInside

    return

label startTravel:
    mitya "Теперь нам надо съездить в село за остальными ингридиентами"
    hide mitya
    hide bg laba
    show bg bus
    window hide
    pause
    show bg bus inside
    "Мы залезли в Буханку"
    show mitya
    mitya "Поехали"
    mitya "Расскажу пока рецепт самогона"
    hide mitya
    show bg cook 1
    mitya "Подготовьте все необходимые ингредиенты. Главное составляющее - яблоки. Не играет большой роли, какие это будут яблоки" 
    mitya "Сладкие или кислые, зеленые или красные. Главное, чтобы они были спелые и без гнили. Дрожжи свежие прессованные, можно заменить на винные дрожжи или сухие дрожжи (10 г)."
    hide bg cook 1
    show bg cook 2
    mitya "Яблоки лучше не мыть, в случае сильного загрязнения просто протрите их тряпкой."
    mitya "На кожице яблок содержится много микроорганизмов, которые способствуют брожению, - помыв, вы смоете их. Яблоки измельчите любым удобным способом."
    mitya "Я натерла их на терке, удалив семенную коробочку, но можно измельчить их с помощью блендера или воспользоваться мясорубкой."
    hide bg cook 2
    show bg cook 3
    mitya "В емкость для браги выложите натертые яблоки."
    hide bg cook 3
    show bg cook 4
    mitya "Дрожжи поломайте на кусочки, добавьте ложку сахара."
    hide bg cook 4
    show bg cook 5
    mitya "Залейте теплой водой и дождитесь образования пенной шапочки. Вода должна быть живая, нефильтровання"
    mitya "Температура воды не более 40 градусов - температура выше уьъет дрожжи и брожения не будет."
    hide bg cook 5
    show bg cook 6
    mitya "Влейте дрожжи к натертым яблокам."
    hide bg cook 6
    show bg cook 7
    mitya "Всыпьте сахар и долейте оставшуюся воду. Все аккуратно перемешайте."
    hide bg cook 7
    show bg cook 8
    mitya "Сверху поставьте гидрозатвор или наденьте одноразовую перчатку. Уберите емкость с брагой в теплое место."
    mitya "Температура должна быть не ниже 20 градусов, поэтому подойдут и обычные комнатные условия."
    hide bg cook 8
    show bg cook 9
    mitya "Как только перчатка надуется - брожение началось. Оно может продолжаться от 10 до 20 дней."
    mitya "Закончится брожение тогда, когда вы увидите, что перчатка сдулась."
    hide bg cook 9
    show bg cook 10
    mitya "Брагу аккуратно процедите через сито."
    hide bg cook 10
    show bg cook 11
    mitya "Она готова для перегонки."
    hide bg cook 11
    show bg cook 12
    mitya "Соберите самогонный аппарат. Если вашей моделью предусмотрено, подсоедините все необходимые шланги с холодной водой."
    hide bg cook 12
    show bg cook 13
    mitya "Аккуратно влейте брагу в самогонный аппарат."
    hide bg cook 13
    show bg cook 14
    mitya "Поставьте на огонь. Следите за температурой."
    mitya "Как только она достигнет 70 градусов, включайте холодную воду для охлаждения. Самогон будет стекать буквально по капельке."
    mitya "Собирайте его в отдельную посуду. Такой самогон готов для употребления, но я предлагаю провести вторую перегонку для более чистого продукта."
    mitya "Для этого полученный самогон разбавьте водой до 20 градусов. На 1 л самогона берите 500 мл воды. Залейте в самогонный аппарат и повторите перегонку."
    hide bg cook 14
    show bg cook 15
    mitya "Но первые 100 мл нового самогона и последние 100 мл соберите в отдельную посуду и вылейте."
    mitya "Это \"головы\" и \"хвосты\" не пригодные для употребления. Самогон после второй перегонки получается без характерного самогонного запаха."
    mitya "Разлейте его по бутылкам и дайте настояться 2-3 дня. Можно подкрасить его капелькой чайной заварки."
    hide bg cook 15
    show bg cook 16
    mitya "Соблюдайте меру при употреблении алкоголя!"
    hide bg cook 16
    show bg bus inside
    show mitya
    mitya "Вроде все"
    mitya "Приехали"
    hide bg bus inside
    show bg shop
    "В магазине не оказалось яблок, поэтому мы купили табуретки"
    "Митя утверждает, что из них может получится отличный самогон"
    hide bg shop
    hide mitya
    show bg bus ingr
    show mitya
    mitya "Поехали делать самогон"
    hide mitya
    pause
    hide bg bus ingr
    show bg chripan
    pause
    hide bg chripan
    jump samogonPrep
    return

label samogonPrep:
    show bg laba ingr
    "Мы отнесли все ингридиенты"
    show mitya
    mitya "Приступим"
    mitya "Главное соблюдать рецепт"

    hide bg laba ingr




label Гараж1:
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
    mitya ""

    hide bg laba ingr

    return




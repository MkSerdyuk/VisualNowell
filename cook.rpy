init python:
    def rate:
        pass

    def ingr_dragged(drags, drop):

        if not drop:
            return

        store.detective = drags[0].drag_name
        store.city = drop.drag_name

        if not all_dropped:
            return
        else:
            rate

        return True

    def plate_dragged(drags, drop):
        pass

    def plate_dropped(drops, drag):
        pass

    def bottle_dropped(drops, drag):
        pass




screen cookAlco:
    add "table.jpg"
    $ all_dropped = False
    $ quality = 0

    draggroup:

        drag:
            drag_name "Табуретка"
            child "ingr1.png"
            droppable False
            dragged ingr_dragged
            xpos 100 ypos 100
        drag:
            drag_name "Дрожжи"
            child "ingr2.png"
            droppable False
            dragged ingr_dragged
            xpos 150 ypos 100
        drag:
            drag_name "Сахар"
            child "ingr3.png"
            droppable False
            dragged ingr_dragged
            xpos 200 ypos 100
        drag:
            drag_name "Кипяток"
            child "ingr3.png"
            droppable False
            dragged ingr_dragged
            xpos 250 ypos 100


        drag:
            drag_name "Терка"
            child "grater.png"
            draggable False
            xpos 450 ypos 140
        drag:
            drag_name "Миска"
            child "plate.png"
            dragged plate_dragged
            dropped plate_dropped
            xpos 500 ypos 280
        drag:
            drag_name "Банка"
            draggable False
            dropped bottle_dropped
            child "bottle.png"
            xpos 550 ypos 420


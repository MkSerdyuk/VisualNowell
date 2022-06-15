init python:

    amount = 0
    quality = 5
    #идеальный порядок ингридиентов
    order = ['Табуретка','Сахар','Кипяток','Дрожжи']

    def ingr_dragged(drags, drop):
        global amount, quality, order
        if not drop:
            return
        amount += 1
        drags[0].draggable = False
        drop.draggable = False
        if drags[0].drag_name != order[amount - 1]:
            quality -= 1 
        #renpy.hide(drags[0])     
        if amount < 4:
            return
        return True

screen cookAlco:
    add "table.jpg"

    draggroup:

        drag:
            drag_name "Табуретка"
            child "ingr1.png"
            droppable False
            dragged ingr_dragged
            xpos 0 ypos 0
        drag:
            drag_name "Дрожжи"
            child "ingr2.png"
            droppable False
            dragged ingr_dragged
            xpos 600 ypos 0
        drag:
            drag_name "Сахар"
            child "ingr3.png"
            droppable False
            dragged ingr_dragged
            xpos 0 ypos 600
        drag:
            drag_name "Кипяток"
            child "ingr4.png"
            droppable False
            dragged ingr_dragged
            xpos 400 ypos 600

        drag:
            drag_name "Миска"
            child "plate.png"
            #draggable False
            xpos 1200 ypos 0



import wrap,time
wrap.world.create_world(400,400,200,200)
ppackmen=wrap.sprite.add("pacman",100,200,"player2")
strawberry=wrap.sprite.add("pacman",0,0,"item_strawberry",visible=False)

@wrap.on_key_always(wrap.K_RIGHT)
def right():
    anglea=wrap.sprite.get_angle(ppackmen)
    wrap.sprite.set_angle(ppackmen,anglea+45)

@wrap.on_key_always(wrap.K_LEFT)
def left():
    anglea=wrap.sprite.get_angle(ppackmen)
    wrap.sprite.set_angle(ppackmen,anglea-45)

@wrap.on_key_always(wrap.K_UP)
def up():
    wrap.sprite.move_at_angle_dir(ppackmen,10)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def leftmouse(pos_x,pos_y):
    wrap.sprite.show(strawberry)

@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def lefthidemouse():
    wrap.sprite.hide(strawberry)

@wrap.on_mouse_move()
def movemouse(pos_x,pos_y):
    wrap.sprite.move_to(strawberry,pos_x,pos_y)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def run(pos_x,pos_y):
    wrap.sprite.set_angle_to_point(ppackmen,pos_x,pos_y)












































































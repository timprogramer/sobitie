import wrap,time
wrap.world.create_world(400,400,200,200)
ppackmen=wrap.sprite.add("pacman",100,200,"player2")

@wrap.on_key_down(wrap.K_RIGHT)
def right():
    anglea=wrap.sprite.get_angle(ppackmen)
    wrap.sprite.set_angle(ppackmen,anglea+45)

@wrap.on_key_down(wrap.K_LEFT)
def left():
    anglea=wrap.sprite.get_angle(ppackmen)
    wrap.sprite.set_angle(ppackmen,anglea-45)














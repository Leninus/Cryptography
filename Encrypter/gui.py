import pyglet
import encrypt as ec
window = pyglet.window.Window()
buttons = pyglet.graphics.Batch()
button_encrypt = pyglet.resource.image("button_encrypt.png")
bg = pyglet.image.SolidColorImagePattern(color= (255,255,255,0)).create_image(window.width, window.height)
button = pyglet.gui.PushButton(x=0, y=window.height - 50, pressed = button_encrypt, depressed = button_encrypt, batch=buttons)

@window.event
def on_press():
    print("Press")

@window.event
def on_mouse_press(x, y, button, modifiera):
    print(x, y)

@window.event
def on_draw():
    window.clear()
    bg.blit(0,0)
    buttons.draw()
    window.push_handlers(button)
    button.set_handler("on_press",on_press)

pyglet.app.run()
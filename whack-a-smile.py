from uib_inf100_graphics.event_app import run_app
from smiley import draw_smiley_in_box
import random

def app_started(app):
    app.cx=400
    app.cy=300
    app.radius=100
    app.score=0

def key_pressed(app,event):
    if event.key == 'Space':
        move_smiley_to_random_location(app)

def mouse_pressed(app,event):
    mouse_x=event.x
    mouse_y=event.y
    if distance(mouse_x,mouse_y, app.cx, app.cy)< app.radius:
        move_smiley_to_random_location(app)
        app.score +=1

def distance(x1,y1,x2,y2):
    return((((x1-x2)**2)+((y1-y2)**2))**0.5)

def timer_fired(app):
    app.radius = app.radius * 0.98

def move_smiley_to_random_location(app):
    app.cx = random.randrange(app.width)
    app.cy = random.randrange(app.height)

def redraw_all(app, canvas):
    x_left=app.cx-app.radius
    x_right=app.cx+app.radius
    y_top=app.cy -app.radius
    y_bottom=app.cy+app.radius
    draw_smiley_in_box(canvas, x_left,y_top,x_right,y_bottom)
    canvas.create_text(app.width/2, 20, text=app.score, font="arial 20")

run_app(width=800, height=600, title="whack-a-smile")

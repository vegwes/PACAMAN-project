from uib_inf100_graphics.event_app import run_app

def app_started(app):
    app.color="red"

def key_pressed(app, event):
    app.color="black"
    if event.key == "r":
        app.color = "red"
def redraw_all(app, canvas):
    # tegn firkanten
    canvas.create_rectangle(
        25, 25, app.width - 25, app.height - 25,
        fill=app.color,
    )

run_app(width=400, height=150)

from uib_inf100_graphics.event_app import run_app

def app_started(app):
    # app_started: kjøres én gang når programmet starter.
    # Her oppretter vi variabler i `app`` og gir dem initiell verdi.
    app.counter = 0

def key_pressed(app, event):
    # key_pressed: kjøres hver gang en tast trykkes.
    # Vi kan endre variabler i `app` her.
    app.counter += 1

def redraw_all(app, canvas):
    # redraw_all: kode for å tegne noe på skjermen. Kjøres vanligvis
    # flere ganger i sekundet.
    # Vi kan benytte (se på) variablene i `app` her, men ikke endre dem.
    canvas.create_text(
        app.width/2, app.height/2,
        text=f'{app.counter} tastetrykk',
        font='Arial 30 bold'
    )

run_app(width=300, height=100)
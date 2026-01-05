import random

def app_started(app):
    app.direction = "east"
    app.infomode = False
    app.score = 0
    app.pacman_r = 11
    app.pacman_c = 1
    app.ghost_r = 0
    app.ghost_c = 3
    app.ghost_r2 = 7
    app.ghost_c2 = 12
    app.game_over = False
    app.timer_delay = 160
    app.timer_count = 0
    app.board = [
    [1, -1, 1, 0, -1, 1, 1, 0, -1, 0, 0, -1,1,-1,1],
    [0, 0, 0, 0, -1, 1, -1, 0, -1, 1, 1, 1,1,-1,-1],
    [1, -1, 1, 0, -1, 1, 1, 0, -1, 1, 1, -1,0,-1,0],
    [0, -1, -1, 1, 0, 1, -1, 1, 0, 0, -1, 0,-1,0,-1],
    [1, 0, 1, 0, -1, -1, 0, -1, -1, 1, 1, -1,1,1,1],
    [1, -1, 1, 1, 0, 1, 1, 1, 0, -1, 0, -1,0,1,-1],
    [-1, 0, -1, 0, -1, 0, -1, 0, -1, 1, 1, -1,1,1,-1],
    [-1, 0, 1, 1, -1, 0, 1, 1, -1, 0, -1, -1,0,-1,0],
    [1, -1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1,0,1,-1],
    [1, 0, 0, -1, 0, -1, 0, -1, 0, -1, 0, 1,-1,1,1],
    [0, -1, 1, 0, 1, 1, 1, 0, 1, 1, -1, -1,0,-1,1],
    [1, 0, 1, -1, 0, -1, 0, -1, 1, -1, 0, 1,-1,0,-1],
]
def draw_pacman(canvas,app):
    x_left, y_top, x_right, y_bottom = 25, 80, 375, 320
    rows, cols = len(app.board), len(app.board[0])
    cell_width = (app.width-50) / cols
    cell_height = (app.height-100) / rows

    x1 = x_left + app.pacman_c * cell_width
    y1 = y_top + app.pacman_r * cell_height
    x2 = x1 + cell_width
    y2 = y1 + cell_height

    margin = 5
    canvas.create_oval(x1 + margin, y1 + margin, x2 - margin, y2 - margin, fill="yellow", outline="black")

def move_pacman(app):
    new_row = app.pacman_r
    new_col = app.pacman_c
    if app.direction == "north":
        new_row -= 1
    elif app.direction == "south":
        new_row += 1
    elif app.direction == "east":
        new_col += 1
    elif app.direction == "west":
        new_col -= 1

    if (0 <= new_row <= 11) and (0 <= new_col <=14):
        if app.board[new_row][new_col] != 1:
            app.pacman_r = new_row
            app.pacman_c = new_col

            if app.board[app.pacman_r][app.pacman_c] == -1:
                app.score += 1
                app.board[app.pacman_r][app.pacman_c] = 0

def draw_ghost(canvas,app):
    x_left, y_top, x_right, y_bottom = 25, 80, 375, 320
    rows, cols = len(app.board), len(app.board[0])
    cell_width = (app.width-50) / cols
    cell_height = (app.height-100) / rows

    x1 = x_left + app.ghost_c * cell_width
    y1 = y_top + app.ghost_r * cell_height
    x2 = x1 + cell_width
    y2 = y1 + cell_height

    margin = 5
    canvas.create_oval(x1 + margin, y1 + margin, x2 - margin, y2 - margin, fill="white", outline="black")

def move_ghost(app):
    if app.game_over: return
    possible_moves = []
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for dr, dc in directions:
        r,c = app.ghost_r + dr, app.ghost_c + dc
        if (0 <= r < len(app.board) and 0 <= c < len(app.board[0])):
            if app.board[r][c] != 1:
                possible_moves.append((r,c))
    
    if possible_moves:
        app.ghost_r, app.ghost_c = random.choice(possible_moves)

def draw_ghost2(canvas,app):
    x_left, y_top, x_right, y_bottom = 25, 80, 375, 320
    rows, cols = len(app.board), len(app.board[0])
    cell_width = (app.width-50) / cols
    cell_height = (app.height-100) / rows

    x1 = x_left + app.ghost_c2 * cell_width
    y1 = y_top + app.ghost_r2 * cell_height
    x2 = x1 + cell_width
    y2 = y1 + cell_height

    margin = 5
    canvas.create_oval(x1 + margin, y1 + margin, x2 - margin, y2 - margin, fill="white", outline="black")

def move_ghost2(app):
    if app.game_over: return
    possible_moves = []
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for dr, dc in directions:
        r,c = app.ghost_r2 + dr, app.ghost_c2 + dc
        if (0 <= r < len(app.board) and 0 <= c < len(app.board[0])):
            if app.board[r][c] != 1:
                possible_moves.append((r,c))
    
    if possible_moves:
        app.ghost_r2, app.ghost_c2 = random.choice(possible_moves)

        


def timer_fired(app):
    if not app.game_over:
        app.timer_count +=1
        move_pacman(app)

        if app.timer_count % 2 == 0:
            move_ghost(app)
            move_ghost2(app)
        check_collision(app)

def check_collision(app):
    if app.pacman_r == app.ghost_r and app.pacman_c == app.ghost_c:
        app.game_over = True

    if app.pacman_r == app.ghost_r2 and app.pacman_c == app.ghost_c2:
        app.game_over = True
    

def key_pressed(app, event):
    if event.key == "Space":
        move_pacman(app)

    if event.key == "i":
        if app.infomode == True:
            app.infomode = False
        else:
            app.infomode = True

    if event.key == "Up":
        app.direction = "north"
    elif event.key == "Down":
        app.direction ="south"
    elif event.key == "Right":
        app.direction = "east"
    elif event.key == "Left":
        app.direction = "west"

def draw_board(canvas, x_left, y_top, x_right, y_bottom, board, info_mode,app):

    rows=len(board)
    cols= len(board[0])
    cell_width=(app.width-50)/cols
    cell_height=(app.height-100)/rows

    for r in range(rows):
        for c in range(cols):
            cell_x1=x_left+c*cell_width
            cell_x2=cell_x1+cell_width
            cell_y1=y_top+r*cell_height
            cell_y2=cell_y1+cell_height
            if board[r][c]>0:
                color="blue"
                utline = "blue"
            else:
                color="black"
                utline = "black"
            canvas.create_rectangle(cell_x1,cell_y1,cell_x2,cell_y2,fill=color, outline = utline)

            if board[r][c] < 0:
                margin = 13.5
                canvas.create_oval(cell_x1 + margin, cell_y1 + margin, cell_x2 - margin, cell_y2 - margin, fill="white")

            if info_mode == True:
                canvas.create_text((cell_x1+cell_x2)/2, (cell_y1+cell_y2)/2+10, text=board[r][c])
                canvas.create_text((cell_x1+cell_x2)/2, (cell_y1+cell_y2)/2-10, text=f"{r},{c}")

def redraw_all(app, canvas):
    if app.infomode == True:
        canvas.create_text(app.width/2,20, text = (f"{app.direction=}"))
    canvas.create_text(app.width/2,40, text = (f"SCORE {app.score}"), fill="yellow", font= "Arial 30")
    draw_board(canvas,25,80,375, 320, app.board, app.infomode, app)
    draw_pacman(canvas, app)
    draw_ghost(canvas,app)
    draw_ghost2(canvas,app)

    if app.game_over:
        canvas.create_rectangle(0, 0, app.width, app.height, fill="black")
        canvas.create_text(app.width/2, app.height/2, 
                           text="GAME OVER", fill="red", font="Arial 30 bold")
    else:
        draw_board(canvas, 25, 80, 375, 320, app.board, app.infomode, app)
        draw_pacman(canvas, app)
        draw_ghost(canvas, app)
        draw_ghost2(canvas,app)

if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    run_app(width=500, height=450, title='PACMAN')
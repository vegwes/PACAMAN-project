import random
def get_initial_board():
    return[
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0,-1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
def restart_game(app,delay):
    app.direction = "east"
    app.info_mode = False
    app.state = "active"
    app.timer_delay=delay
    app.score=0
    app.snake_size=3
    app.head_pos=(3,4)
    app.board =get_initial_board()

def app_started(app):
    app.info_mode= False
    app.difficulty_options = {
        "EASY": 220,
        "MEDIUM": 150,
        "HARD": 50
    }
    app.difficulty_keys = list(app.difficulty_options.keys())
    app.selected_difficulty_index = 1
    app.state = "start_screen"
    app.timer_delay = 0 

def get_next_head_position(head_pos, direction):

    row, col = head_pos
    if direction == "north":
        row -= 1
    elif direction == "south":
        row +=1
    elif direction == "east":
        col += 1
    elif direction == "west":
        col -=1
    head_pos = (row,col)
    return head_pos
        
def add_apple_at_random_location(grid):

    len_row=len(grid)
    len_col=len(grid[0])

    row=random.randint(0,len_row-1)
    col=random.randint(0, len_col-1)

    while grid[row][col] !=0:
        row=random.randint(0,len_row-1)
        col=random.randint(0, len_col-1)
    grid[row][col] = -1

def timer_fired(app):
    if app.info_mode== False and app.state=="active":
        move_snake(app)

def move_snake(app):

    next_head=get_next_head_position(app.head_pos, app.direction)
    row,col=next_head
    if not is_move_legal(next_head,app.board):
        app.state="gameover"
        return
    app.head_pos=next_head
    if app.board[row][col]==-1:
        app.score+=1
        app.snake_size+=1
        add_apple_at_random_location(app.board)
        
    for i in range(len(app.board)):
        for u in range(len(app.board[i])):
            if app.board[i][u]>0:
                app.board[i][u]-=1
    app.board[row][col]=app.snake_size

def is_move_legal(pos,board):

    row, col = pos
    rows = len(board)
    cols = len(board[0])
    if row<0 or row>= rows or col<0 or col>=cols:
        return False
    if board[row][col] > 1:
        return False
    else:
        return True
        


def key_pressed(app, event):
    if app.state == "start_screen":
        if event.key == "Up":
            app.selected_difficulty_index = (app.selected_difficulty_index - 1) % len(app.difficulty_keys)
        elif event.key == "Down":
            app.selected_difficulty_index = (app.selected_difficulty_index + 1) % len(app.difficulty_keys)
        elif event.key == "Space":
            selected_key = app.difficulty_keys[app.selected_difficulty_index]
            selected_delay = app.difficulty_options[selected_key]
            restart_game(app, selected_delay)
        return
    if app.state == "gameover":
        if event.key == "Space":
            app.state="start_screen"
            app.selected_difficulty_index = 1
            return
    
    if event.key == "i":
        if app.info_mode == True:
            app.info_mode = False
        else:
            app.info_mode=True
    if app.state=="active":
        if event.key == "Up":
            if app.direction != "south":
                app.direction = "north"      
        elif event.key == "Down":
            if app.direction != "north":
                app.direction = "south"
        elif event.key == "Right":
            if app.direction != "west":
                app.direction = "east"
        elif event.key == "Left":
            if app.direction != "east":
                app.direction = "west"

        if event.key == "Space":
            if app.info_mode:
                move_snake(app)
    

def redraw_all(app, canvas):
    if app.state == "start_screen":
        canvas.create_rectangle(0,0,app.width, app.height, fill="green")
        canvas.create_text(app.width/2, 50, text="SNAKE", font="Arial 60", fill="purple")
        canvas.create_text(app.width/2, 120, text="DIFFICULITY", font="Arial 40", fill="white")

        y_pos = 180
        for i, difficulty in enumerate(app.difficulty_keys):
            font_size = "30"
            color = "purple" if i == app.selected_difficulty_index else "white"
            
            canvas.create_text(app.width/2, y_pos, text=difficulty, font=f"Arial {font_size}", fill=color)
            y_pos += 40
            
        canvas.create_text(app.width/2, app.height - 80, text="Press up or down to choose difficulity", font="Arial 20", fill="white")
        canvas.create_text(app.width/2, app.height - 60, text="Press 'Space' to restart", font="Arial 20", fill="white")

    elif app.state=="gameover":
        canvas.create_rectangle(0,0,app.width, app.height, fill="black")
        canvas.create_text(app.width/2, 90, text="GAME OVER", font= "Arial 60", fill="red")
        canvas.create_text(app.width/2, 135, text=f"SCORE {app.score}", font="Arial 30", fill="green")
        canvas.create_text(app.width/2, 185, text="Press 'Space' to restart", font="Arial 20", fill="white")
    else:
        canvas.create_text(app.width/2, 55, text=f"SCORE {app.score}", font="Arial 30", fill="green")
        if app.info_mode:
            canvas.create_text(app.width/2, 20, text=f'{app.direction=} {app.snake_size=} {app.head_pos=} {app.state=}')
        draw_board(canvas,25,80,375, 320, app.board, app.info_mode, app)


def draw_board(canvas, x_left, y_top, x_right, y_bottom, board, info_mode,app):

    rows=len(board)
    cols= len(board[0])
    cell_width=(app.width-50)/cols
    cell_height=(app.height-100)/rows

    for r in range(rows):
        for c in range(cols):
            if board[r][c]>0:
                color="purple"
            elif board [r][c]==0:
                color="green"
            elif board [r][c]<0:
                color="red"

            cell_x1=x_left+c*cell_width
            cell_x2=cell_x1+cell_width

            cell_y1=y_top+r*cell_height
            cell_y2=cell_y1+cell_height

            canvas.create_rectangle(
                cell_x1,cell_y1,cell_x2,cell_y2,
                fill=color
            )
            if info_mode == True:
                canvas.create_text((cell_x1+cell_x2)/2, (cell_y1+cell_y2)/2+10, text=board[r][c])
                canvas.create_text((cell_x1+cell_x2)/2, (cell_y1+cell_y2)/2-10, text=f"{r},{c}")


if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    run_app(width=500, height=400, title='Snake')
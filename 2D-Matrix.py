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
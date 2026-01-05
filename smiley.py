def draw_smiley_static(canvas):
    canvas.create_oval(0,0,150,150, fill="yellow")
    canvas.create_oval(40,40,50,58, fill="white")
    canvas.create_oval(100,40,110,58, fill="white")
    canvas.create_line(50,105, 75, 120, 100, 105, smooth=True)

def draw_smiley_scaled(canvas,scale):
        canvas.create_oval(0*scale,0*scale,150*scale,150*scale, fill="yellow")
        canvas.create_oval(40*scale,40*scale,50*scale,58*scale, fill="white")
        canvas.create_oval(100*scale,40*scale,110*scale,58*scale, fill="white")
        canvas.create_line(50*scale,105*scale, 75*scale, 120*scale, 100*scale, 105*scale, smooth=True)


def draw_smiley_stretched(canvas,stretch_width,stretch_height):
    canvas.create_oval(0*stretch_width,0*stretch_height,150*stretch_width,150*stretch_height, fill="yellow")
    canvas.create_oval(40*stretch_width,40*stretch_height,50*stretch_width,58*stretch_height, fill="white")
    canvas.create_oval(100*stretch_width,40*stretch_height,110*stretch_width,58*stretch_height, fill="white")
    canvas.create_line(50*stretch_width,105*stretch_height, 75*stretch_width, 120*stretch_height, 100*stretch_width, 105*stretch_height, smooth=True)

def draw_smiley_by_size(canvas,width,height):
     stretch_width= width/150
     stretch_height=height/150
     draw_smiley_stretched(canvas,stretch_width,stretch_height)

def draw_smiley_shifted(canvas, width, height, dx, dy):
    stretch_width= width/150
    stretch_height=height/150
    canvas.create_oval(0*stretch_width +dx,0*stretch_height+dy,150*stretch_width+dx,150*stretch_height+dy, fill="yellow")
    canvas.create_oval(40*stretch_width+dx,40*stretch_height+dy,50*stretch_width+dx,58*stretch_height+dy, fill="white")
    canvas.create_oval(100*stretch_width+dx,40*stretch_height+dy,110*stretch_width+dx,58*stretch_height+dy, fill="white")
    canvas.create_line(50*stretch_width+dx,105*stretch_height+dy, 75*stretch_width+dx, 120*stretch_height+dy, 100*stretch_width+dx, 105*stretch_height+dy, smooth=True)

def draw_smiley_in_box(canvas, x_left, y_top, x_right, y_bottom):
    width=x_right - x_left
    height=y_bottom - y_top
    dx=x_left
    dy=y_top
    stretch_width= width/150
    stretch_height=height/150
    canvas.create_oval(0*stretch_width +dx,0*stretch_height+dy,150*stretch_width+dx,150*stretch_height+dy, fill="yellow")
    canvas.create_oval(40*stretch_width+dx,40*stretch_height+dy,50*stretch_width+dx,58*stretch_height+dy, fill="white")
    canvas.create_oval(100*stretch_width+dx,40*stretch_height+dy,110*stretch_width+dx,58*stretch_height+dy, fill="white")
    canvas.create_line(50*stretch_width+dx,105*stretch_height+dy, 75*stretch_width+dx, 120*stretch_height+dy, 100*stretch_width+dx, 105*stretch_height+dy, smooth=True)

if __name__=='__main__':
    from uib_inf100_graphics.simple import canvas, display

    draw_smiley_in_box(canvas,100,100, 300, 300)

    display(canvas)

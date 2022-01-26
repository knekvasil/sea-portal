# app.py

import numpy as np
from PIL import Image, ImageDraw


def init_graph():
    canvas_edge_px = 128
    canvas_bg_color = (255, 255, 255)
    edge_color = (0, 0, 0)

    canvas = Image.new("RGB", size=(
        canvas_edge_px, canvas_edge_px), color=canvas_bg_color)
    draw = ImageDraw.Draw(canvas)

    axis_point_pos_x = (canvas_edge_px/2, 10)
    axis_point_neg_x = (canvas_edge_px/2, canvas_edge_px-10)

    axis_point_pos_y = (canvas_edge_px-10, canvas_edge_px/2)
    axis_point_neg_y = (10, canvas_edge_px/2)

    axis_edge_x = (axis_point_pos_x, axis_point_neg_x)
    axis_edge_y = (axis_point_pos_y, axis_point_neg_y)

    draw.line(axis_edge_x, fill=edge_color)
    draw.line(axis_edge_y, edge_color)

    print((axis_point_pos_x[1]+3, axis_point_pos_x[0]-3))

    axis_point_pos_y_arrow_edge_l = (axis_point_pos_x,
                                     (axis_point_pos_x[0]-3, axis_point_pos_x[1]+5))
    axis_point_pos_y_arrow_edge_r = (axis_point_pos_x,
                                     (axis_point_pos_x[0]+3, axis_point_pos_x[1]+5))

    axis_point_neg_y_arrow_edge_r = (axis_point_neg_x,
                                     (axis_point_neg_x[0]-3, axis_point_neg_x[1]-5))
    axis_point_neg_y_arrow_edge_l = (axis_point_neg_x,
                                     (axis_point_neg_x[0]+3, axis_point_neg_x[1]-5))

    axis_point_pos_x_arrow_edge_r = (axis_point_pos_y,
                                     (axis_point_pos_y[0]-5, axis_point_pos_y[1]+3))
    axis_point_pos_x_arrow_edge_l = (axis_point_pos_y,
                                     (axis_point_pos_y[0]-5, axis_point_pos_y[1]-3))

    axis_point_neg_x_arrow_edge_r = (axis_point_neg_y,
                                     (axis_point_neg_y[0]+5, axis_point_neg_y[1]+3))
    axis_point_neg_x_arrow_edge_l = (axis_point_neg_y,
                                     (axis_point_neg_y[0]+5, axis_point_neg_y[1]-3))

    draw.line(axis_point_pos_y_arrow_edge_l, fill=edge_color)
    draw.line(axis_point_pos_y_arrow_edge_r, fill=edge_color)

    draw.line(axis_point_neg_y_arrow_edge_l, fill=edge_color)
    draw.line(axis_point_neg_y_arrow_edge_r, fill=edge_color)

    draw.line(axis_point_pos_x_arrow_edge_l, fill=edge_color)
    draw.line(axis_point_pos_x_arrow_edge_r, fill=edge_color)

    draw.line(axis_point_neg_x_arrow_edge_l, fill=edge_color)
    draw.line(axis_point_neg_x_arrow_edge_r, fill=edge_color)

    generate_function(draw)

    canvas.save("preview_image.png")


def generate_function(draw):
    plot_color = (255, 0, 0)
    x = np.linspace(0, 100, 101)
    """
    Graph built in nupy functions ( y = np.sin(x), cos(x), etc.)
    """

    for i in range(len(x)):
        draw.point((i+15, (y[i]*5+64)), fill=plot_color)


def main():
    init_graph()


if __name__ == "__main__":
    main()

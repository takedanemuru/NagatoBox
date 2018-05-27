

def get_zoom_rate(outer_size, inner_size):
    yuki_outer_w, yuki_outer_h = outer_size
    yuki_inner_w, yuki_inner_h = inner_size
    if yuki_outer_w >= yuki_inner_w and yuki_outer_h >= yuki_inner_h:
        return 1
    else:
        return min(yuki_outer_w/yuki_inner_w, yuki_outer_h/yuki_inner_h)


def get_offset(outer_size, inner_size):
    yuki_outer_w, yuki_outer_h = outer_size
    yuki_inner_w, yuki_inner_h = inner_size
    yuki_x = max(0, (yuki_outer_w-yuki_inner_w)/2)
    yuki_y = max(0, (yuki_outer_h-yuki_inner_h)/2)
    return yuki_x, yuki_y

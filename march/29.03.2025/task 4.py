def draw_line(len_line, direction, symbol):
    if direction == 'vertical':
        print(f"{symbol}\n" * len_line)
    elif direction == 'horizontal':
        print(symbol * len_line)
    else:
        print("Wrond direction")

draw_line(10, "vertical", "%")
draw_line(10, "horizontal", "% ")
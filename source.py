from PIL import Image

try:
    im = Image.open('im.png')
except FileNotFoundError:
    im = Image.open('im.jpg')

chars = [
    '#',
    '@',
    'B',
    'K',
    'H',
    'U',
    'P',
    '8',
    '%',
    '&',
    'Q',
    'D',
    'O',
    'L',
    '$',
    '=',
    'o',
    '+',
    '*',
    '"',
    '-',
    ';',
    ',',
    '\'',
    '.',
    ' '
]

# chars = list('@B%8&WM#ZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<i!lI;:,"^`\'. ')

width, height = im.size


def map_vals(v, fl, fh, sl, sh):
    o = round(sl + (float(v - fl) / float(fh - fl) * ((sh - 1) - sl)))
    return o  # if o < sh else sh - 1


def rgb_to_hsl(r, g, b):
    R, G, B = [x / 255 for x in [r, g, b]]
    mx = max([r, g, b]) / 255
    mn = min([r, g, b]) / 255
    l = (mx + mn) / 2
    if l == 0:
        return 0, 0, 0
    if mn == mx:
        return 0, 0, l
    if l < 0.5:
        s = (mx - mn) / (mx + mn)
    else:
        s = (mx - mn) / (2 - mx - mn)

    dr = (((mx - R) / 6) + (mx - mn) / 2) / (mx - mn)
    dg = (((mx - G) / 6) + (mx - mn) / 2) / (mx - mn)
    db = (((mx - B) / 6) + (mx - mn) / 2) / (mx - mn)

    if mx == R:
        h = db - dg
    elif mx == G:
        h = 1 / 3 + dr - db
    else:
        h = 2 / 3 + dg - dr
    if h < 0:
        h += 1
    if h > 1:
        h -= 1
    h *= 360
    return round(h), round(s * 100), round(l * 100)


out_list = [['' for j in range(width)] for i in range(height)]
for y in range(height):
    for x in range(width):
        out_list[y][x] = chars[map_vals(rgb_to_hsl(*im.getpixel((x, y))[:3])[2], 0, 100, 0, len(chars))]
with open('out.txt', 'w') as file:
    file.write('\n'.join([''.join(j) for j in out_list]))

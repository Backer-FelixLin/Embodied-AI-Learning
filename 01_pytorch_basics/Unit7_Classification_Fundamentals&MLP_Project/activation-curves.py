from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont


OUTPUT = Path(__file__).with_suffix('.png')
SCALE = 2
image = Image.new('RGB', (1200 * SCALE, 1080 * SCALE), 'white')
draw = ImageDraw.Draw(image)
font_path = 'C:/Windows/Fonts/arial.ttf'
ink = '#20262B'
grid = '#E4E8E9'
colors = ['#007F73', '#B34039']


def font(size):
    return ImageFont.truetype(font_path, size * SCALE)


def text(x, y, value, size=22, anchor='la', color=ink):
    draw.text((x * SCALE, y * SCALE), value, fill=color,
              font=font(size), anchor=anchor)


def line(points, color=grid, width=1):
    draw.line([(x * SCALE, y * SCALE) for x, y in points],
              fill=color, width=width * SCALE)


def circle(x, y, radius=5, fill='white', outline=ink):
    draw.ellipse(tuple(v * SCALE for v in
                       (x-radius, y-radius, x+radius, y+radius)),
                 fill=fill, outline=outline, width=2 * SCALE)


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def panel(row, col, name, function, limits, ticks, segments=None):
    left, right = 96 + col * 584, 556 + col * 584
    top, bottom = 150 + row * 290, 344 + row * 290
    ymin, ymax = limits

    def xy(x, y):
        return (left + (x + 6) / 12 * (right-left),
                bottom - (y-ymin) / (ymax-ymin) * (bottom-top))

    text((left+right)/2, top-39, name, size=25, anchor='ma')
    for y in ticks:
        _, py = xy(0, y)
        line([(left, py), (right, py)])
        text(left-14, py, f'{y:g}', size=21, anchor='rm')
    for x in [-6, -3, 0, 3, 6]:
        px, _ = xy(x, 0)
        line([(px, top), (px, bottom)])
        text(px, bottom+10, str(x), size=21, anchor='ma')
    line([(left, top), (left, bottom), (right, bottom),
          (right, top), (left, top)], color='#A5ADAE')
    text(right, bottom+38, 'input x', size=21, anchor='ra')
    for lo, hi in segments or [(-6, 6)]:
        values = [lo + (hi-lo)*i/700 for i in range(701)]
        line([xy(x, function(x)) for x in values], colors[col], 3)
    return xy


text(54, 28, 'Activation functions and local derivatives', size=33)
text(54, 73, 'OUTPUT f(x)', size=23, color=colors[0])
text(638, 73, 'LOCAL DERIVATIVE df/dx', size=23, color=colors[1])

panel(0, 0, 'ReLU', lambda x: max(0, x), (-.4, 6.4), [0, 3, 6])
relu_axes = panel(0, 1, 'ReLU derivative', lambda x: float(x > 0),
                  (-.1, 1.1), [0, .5, 1],
                  segments=[(-6, -.02), (.02, 6)])
circle(*relu_axes(0, 1), outline=colors[1])
circle(*relu_axes(0, 0), fill=colors[1], outline=colors[1])

panel(1, 0, 'Sigmoid', sigmoid, (-.1, 1.1), [0, .5, 1])
panel(1, 1, 'Sigmoid derivative', lambda x: sigmoid(x)*(1-sigmoid(x)),
      (-.025, .275), [0, .125, .25])
panel(2, 0, 'Tanh', math.tanh, (-1.2, 1.2), [-1, 0, 1])
panel(2, 1, 'Tanh derivative', lambda x: 1-math.tanh(x)**2,
      (-.1, 1.1), [0, .5, 1])

text(54, 1017, 'ReLU at x = 0: no mathematical derivative; PyTorch uses 0.', size=23)
assert sigmoid(0) == .5
assert math.tanh(0) == 0
assert 1-math.tanh(0)**2 == 1
image.resize((1200, 1080), Image.Resampling.LANCZOS).save(OUTPUT)
print(OUTPUT)

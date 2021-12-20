import sys
from pathlib import Path

inputs = Path(sys.argv[1]).read_text().strip()

inputs = inputs.split('\n\n')
image_enhancement_algorithm = inputs[0].replace('\n', '').strip()
input_image = [line for line in inputs[1].split('\n') if line]
infinite_color = '.'


def get_pixel(x, y):
    line = ''
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i < len(input_image) and 0 <= j < len(input_image):
                line += input_image[i][j]
            else:
                line += infinite_color
    pixel_index = int(line.replace('.', '0').replace('#', '1'), 2)
    return image_enhancement_algorithm[pixel_index]


for _ in range(50):
    image = []
    for i in range(-1, len(input_image) + 1):
        line = ''
        for j in range(-1, len(input_image) + 1):
            line += get_pixel(i, j)
        image.append(line)
    input_image = image
    infinite_color = get_pixel(-1000000, -1000000)

print(f'Lit pixels count: {len([ch for ch in "".join(input_image) if ch == "#"])}')

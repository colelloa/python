from duplicate_image import ImageDuplicator

ORIGINAL_PATH = "training_images/rough_orig.png"
BALL_DIAMETER = 30

dup = ImageDuplicator(ORIGINAL_PATH, BALL_DIAMETER)
max_width = dup.width - BALL_DIAMETER
max_length = dup.length - BALL_DIAMETER

for x in range(0, max_width, BALL_DIAMETER):
    for y in range(0, max_length, BALL_DIAMETER):
        print x,y
        c = list()
        c.append(x)
        c.append(y)
        if x <=30 and y <= 30: #DEV-REMOVE
            new_path = dup.draw_circle(c)
            for percent in range(10, 100, 10):
                if percent == 50 or percent == 80: #DEV-REMOVE
                    new_path = dup.draw_circle(c)
                    dup.blend_images(ORIGINAL_PATH, new_path, c, percent)


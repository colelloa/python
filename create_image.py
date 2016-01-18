from duplicate_image import ImageDuplicator

IMG_ROOT = "training_images"
ORIGINAL_PATH = "training_images/rough_orig.png"
BALL_DIAMETER = 30

dup = ImageDuplicator(ORIGINAL_PATH, BALL_DIAMETER, IMG_ROOT)
max_width = dup.width - BALL_DIAMETER
max_length = dup.length - BALL_DIAMETER

for x in range(0, max_width, BALL_DIAMETER):
    for y in range(0, max_length, BALL_DIAMETER):
        print x,y
        c = list()
        c.append(x)
        c.append(y)
        
        if x <=30 and y <= 30: #DEV-REMOVE - only use (0,0), (0,30), (30, 0), (30, 30)

            new_path = dup.draw_circle(c) #create circle with 100% opacity
            for percent in range(10, 100, 10): #loop from 10-90% in intervals of 10

                if percent == 50 or percent == 80: #DEV-REMOVE - only 50 and 80 percent
                
                    dup.blend_images(ORIGINAL_PATH, new_path, c, percent)


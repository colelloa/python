from duplicate_image import ImageDuplicator

ORIGINAL_PATH = "training_images/rough_orig.png"


dup = ImageDuplicator(ORIGINAL_PATH)
c = (0,0)
new_path = dup.draw_circle(c)
dup.blend_images(ORIGINAL_PATH, new_path, c, 40)

c2 = (50,50)
new_path2 = dup.draw_circle(c)
dup.blend_images(ORIGINAL_PATH, new_path2, c2, 90)



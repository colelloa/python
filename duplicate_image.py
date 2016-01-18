from PIL import Image, ImageFilter, ImageDraw

#image naming convention xcoord_ycoord_alpha.png 
#where coords are those of left corner of box to fill

class ImageDuplicator:

    def __init__(self, orig_path):
        # open grass image
        self.grass_path = orig_path

        img = Image.open(orig_path) #too big to make a permanent instance variable
        dim = img.size
        self.width = dim[0]
        self.length = dim[1]

        del img #special garbage collection 


    def draw_circle(self, left_corner):
        #create draw object from original path
        img = Image.open(self.grass_path)
        draw_obj = ImageDraw.Draw(img)

        #draw circle with diameter=30 at center input
        x0 = left_corner[0]
        y0 = left_corner[1]
        x1 = x0 + 30 #30x30 box to make circle
        y1 = y0 + 30
        draw_obj.ellipse((x0, y0, x1, y1), fill = 'white', outline ='white')
        
        #alpha is 1.00 for newly drawn circle, represented as 100
        new_path = "training_images/{0}_{1}_100.png".format(x0, y0)
        img.save(new_path)
        del draw_obj #garbage collection
        del img 
        return new_path

    def blend_images(self, background_path, ball_path, center, percentage):
        #according to docs at http://effbot.org/imagingbook/image.htm:
        #out = image1 * (1.0 - alpha) + image2 * alpha
        alpha = percentage/100.0
        background = Image.open(background_path)
        ball = Image.open(ball_path)

        final_path = "training_images/{0}_{1}_{2}.png".format(center[0], center[1], percentage)

        out = Image.blend(background, ball, alpha)
        out.save(final_path) #example of convention here
        out.show()

        del background
        del ball






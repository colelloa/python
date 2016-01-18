from PIL import Image, ImageDraw

#image naming convention xcoord_ycoord_alpha.png 
#where coords are those of left corner of box to fill

class ImageDuplicator:

    def __init__(self, orig_path, diameter, root_dir):
        self.BALL_DIAMETER = diameter
        self.IMAGE_ROOT_DIRECTORY = root_dir
        # open grass image
        self.grass_path = orig_path

        img = Image.open(orig_path) #too big to make a permanent instance variable
        dim = img.size
        self.width = dim[0]
        self.length = dim[1] #need the width and length when creating loop in higher abstraction level

        del img # garbage collection 

    def draw_circle(self, left_corner):
        #create draw object from original path
        img = Image.open(self.grass_path)
        draw_obj = ImageDraw.Draw(img)

        #prepare to draw 
        x0 = left_corner[0]
        y0 = left_corner[1]
        x1 = x0 + self.BALL_DIAMETER #create box to draw in
        y1 = y0 + self.BALL_DIAMETER
        draw_obj.ellipse((x0, y0, x1, y1), fill = 'white', outline ='white')
        
        #alpha is 1.00 for newly drawn circle, represented as 100
        new_path = "{0}/{1}_{2}_100.png".format(self.IMAGE_ROOT_DIRECTORY, x0, y0)
        img.save(new_path)

        del draw_obj #garbage collection
        del img 
        return new_path #to make it easier to blend

    def blend_images(self, background_path, ball_path, left_corner, percentage):
        #according to docs at http://effbot.org/imagingbook/image.htm: out = image1 * (1.0 - alpha) + image2 * alpha
        alpha = percentage/100.0
        background = Image.open(background_path)
        ball = Image.open(ball_path)

        final_path = "{0}/{1}_{2}_{3}.png".format(self.IMAGE_ROOT_DIRECTORY, left_corner[0], left_corner[1], percentage)

        out = Image.blend(background, ball, alpha)
        out.save(final_path)

        del background
        del ball 
        del out #collect garbage

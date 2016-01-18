from PIL import Image, ImageFilter, ImageDraw

#picture naming convention:x-coord y-coord alpha

class ImageDuplicator:

    def __init__(self, orig_path):
        # open grass image
        self.grass_path = orig_path

        img = Image.open(orig_path) #too big to make a permanent instance variable
        dim = img.size
        self.width = dim[0]
        self.length = dim[1]

        del img #special garbage collection 


    def draw_circle(self, center):
        #create draw object from original path
        img = Image.open(self.grass_path)
        draw_obj = ImageDraw.Draw(img)

        #draw circle with diameter=30 at center input
        draw_obj.ellipse((center[0], center[1], 30, 30), fill = 'white', outline ='white')
        

        #save image according to convention x-coord y-coord alpha
        #alpha is 1.0 for newly drawn circle, represented as 10
        new_path = "training_images/{0}{1}100.png".format(center[0], center[1])
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

        final_path = "training_images/{0}{1}{2}.png".format(center[0], center[1], percentage)

        out = Image.blend(background, ball, alpha)
        out.save(final_path) #example of convention here
        out.show()

        del background
        del ball






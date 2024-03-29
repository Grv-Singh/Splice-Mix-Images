#coding: utf-8

from __future__ import division
import PIL
from PIL import Image, ImageFont, ImageDraw
import numpy, os, random, time
import numexpr
STAG = time.time()

root=""
W_num =3
H_num = 3
W_size = 640
H_size = 360

alpha = 0.5
aval = []


def getAllPhotos():
    STA = time.time()
    root = os.getcwd() + "/"
    src = root+"/photos/"
    for i in os.listdir(src):
	    if os.path.splitext(src+i)[-1] == ".jpg" or os.path.splitext(src+i)[-1] == ".png":
		    aval.append(src+i)


def scale(img_path, dst_width,dst_height):

    STA = time.time()
    im = Image.open(img_path)
    if im.mode != "RGBA":
        im = im.convert("RGBA")
    s_w,s_h = im.size
    if s_w < s_h:
        im = im.rotate(90)
	
    #if dst_width*0.1/s_w > dst_height*0.1/s_h:
    #    ratio = dst_width*0.1/s_w
    #else:
    #    ratio = dst_height*0.1/s_h
    resized_img = im.resize((dst_width, dst_height), Image.ANTIALIAS)  
    resized_img = resized_img.crop((0,0,dst_width,dst_height))
    print("scale Func Time %s"%(time.time()-STA))

    return resized_img


def jointAndBlend():
    iW_size = W_num * W_size
    iH_size = H_num * H_size
    I = numpy.array(scale(root+"photo.jpg", iW_size, iH_size))
    I = numexpr.evaluate("""I*(1-alpha)""")

    for i in range(W_num):
        for j in range(H_num):
            SH = I[(j*H_size):((j+1)*H_size), (i*W_size):((i+1)*W_size)]
            STA = time.time()
            DA = scale(random.choice(aval), W_size, H_size)
            print("Cal Func Time %s"%(time.time()-STA))
            res  = numexpr.evaluate("""SH+DA*alpha""")
            I[(j*H_size):((j+1)*H_size), (i*W_size):((i+1)*W_size)] = res

    Image.fromarray(I.astype(numpy.uint8)).save("blend.png")


def rotate():
    imName = "blend.png"
    print("Rotating...")
    STA = time.time()
    im = Image.open(imName)
    im2 = Image.new("RGBA", (W_size * int(W_num + 1), H_size * (H_num + 4)))
    im2.paste(im, (int(0.5 * W_size), int(0.8 * H_size)))
    im2 = im2.rotate(359)
    im2.save("rotate.png")
    print("rotate Func Time %s"%(time.time()-STA))


def addText():
    print("Adding Text...")
    img = Image.open("blend.png")
    fontWeight=W_num*W_size//12
    font = ImageFont.truetype('product.ttf', fontWeight)
    draw = ImageDraw.Draw(img)
    draw.ink = 21 + 118*256 + 65*256*256

#    draw.text((0,H_size * 6),unicode("happy every day",'utf-8'),(0,0,0),font=font)

    draw.text((W_size * 0.5, fontWeight), "happy life written by python", font = font)
    img.save("addText.png")

if __name__ == "__main__":

    getAllPhotos()
    jointAndBlend()
    rotate()
    addText()
    print("Total Time %s"%(time.time()-STAG))

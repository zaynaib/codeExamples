from PIL import Image

def copyImage(source):

    dest = Image.new("RGB", source.size)

    for x in range(source.size[0]):

        for y in range(source.size[1]):

            pix = source.getpixel( (x,y) )

            dest.putpixel( (x,y), pix)

    return dest

def drawBox(source, start, size, color):

    endpoints = source.size

    dest = copyImage(source)

    for x in range(size[0]): #range through each pixel in our block

        for y in range(size[1]):

            dest.putpixel( (x+start[0],y+start[1]), color) 

    return dest



def GetBlock(source_img, loc,copy_size):
    newImg = Image.new("RGB",copy_size)
    width,height = copy_size
    for x in range(loc[0], loc[0]+width):
        for y in range(loc[1], loc[1] +height):
            color = source_img.getpixel((x,y))
            newImg.putpixel((x-loc[0], y-loc[1]),color)
    return newImg


def PutBlock(small_img,destination,loc):
    smallwid, smallhei = small_img.size
    deswid,deshei = destination.size
    for x in range(loc[0],loc[0] + smallwid):
        for y in range(loc[1], loc[1]+smallhei):
            color = small_img.getpixel((x-loc[0], y- loc[1]))
            destination.putpixel((x,y),color)


def scale(origImage, widthFactor, heightFactor):
    wid, ht = origImage.size
    newIm = Image.new("RGB", (int(wid *widthFactor),int(ht*heightFactor)))
    for i in range(int(wid*widthFactor)):
        for j in range(int(ht*heightFactor)):
            
            pixCol = origImage.getpixel((int(i / widthFactor),int(j /heightFactor)))

            newIm.putpixel((i,j),pixCol)

    return newIm

def CheckerBoard(img1, img2, block_size):
    wid1, hg1 = img1.size
    wid2, hg2 = img2.size
    if(wid1 *hg1 < wid2*hg2):
        newwid = (wid1/block_size) *block_size
        newhg = (hg1/block_size) * block_size
    else:
        newwid = (wid2/block_size) *block_size
        newhg = (hg2/block_size) * block_size
    
    scale_newimg1 = scale(img1, float(newwid)/wid1,float(newhg)/hg1)
    scale_newimg2 = scale(img2, float(newwid)/wid2, float(newhg/hg2))
    newImage = Image.new("RGB",(newwid,newhg))
    counterx = 0

    for x in range(0,newwid,block_size):
        countery = 0
        for y in range(0,newhg,block_size):
            if((counterx + countery) %2 ==0):
                imgBlock = GetBlock(img1,(x,y),(block_size,block_size))
            else:
                imgBlock = GetBlock(img2,(x,y),(block_size,block_size))
            PutBlock(imgBlock,newImage,(x,y))
            countery += 1
        counterx += 1

    return newImage

img1 = Image.open("light.jpg")
img2 = Image.open("yellow.jpg")

img3 =CheckerBoard(img1,img2,100)
img3.show()




    
    
            




            
            
    
    

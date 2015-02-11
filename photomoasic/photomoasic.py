
from PIL import Image
import os

# the distance function takes 2 pixels as input
# and returns the squared distance between them.
def distance(pix1, pix2):
    dist = 0
    for i in range(3):
        dist = dist + (pix1[i] - pix2[i])*(pix1[i] - pix2[i])
    return dist

# place your code for the "scale" function here
def scale(origImage, widthFactor, heightFactor):
    wid, ht = origImage.size
    newIm = Image.new("RGB", (int(wid *widthFactor),int(ht*heightFactor)))
    for i in range(int(wid*widthFactor)):
        for j in range(int(ht*heightFactor)):
            
            pixCol = origImage.getpixel((int(i / widthFactor),int(j /heightFactor)))

            newIm.putpixel((i,j),pixCol)

    return newIm

# place your code for the "putBlock" function here
def PutBlock(small_img,destination,loc):
    smallwid, smallhei = small_img.size
    deswid,deshei = destination.size
    for x in range(loc[0],loc[0] + smallwid):
        for y in range(loc[1], loc[1]+smallhei):
            color = small_img.getpixel((x-loc[0], y- loc[1]))
            destination.putpixel((x,y),color)


def average(img):
    wid,heg = img.size
    totalpix = wid *heg
    sumred,sumgreen,sumblue = 0,0,0
    for x in range(wid):
        for y in range(heg):
            r,g,b = img.getpixel((x,y))
            sumred = r+sumred
            sumgreen = g+ sumgreen
            sumblue = b +sumblue
    avgred = sumred/totalpix
    avggreen = sumgreen/totalpix
    avgblue = sumblue/totalpix
    avgpixel =(avgred,avggreen,avgblue)
    return avgpixel

'''testImg = Image.new("RGB",(2,2),(100,100,100))
testImg.putpixel((1,0),(0,100,100))
myAvg = average(testImg)
print(myAvg)'''

def scaleTarget(img, res):
    widResolution,hegResolution = res
    scaleimg = scale(img,(float(widResolution)/img.size[0]),(float(hegResolution)/img.size[1]))
    return scaleimg

'''testImg = Image.new("RGB",(2,2),(100,100,100))
resultImg = scaleTarget(testImg,(100,100))
resultImg.show()'''


def buildTile(img, tileSize):
    scaled_thumbnail = scaleTarget(img, tileSize)
    avgcolor_thumbnail = average(img)
    the_tile =(scaled_thumbnail,avgcolor_thumbnail)
    return the_tile

'''testImg = Image.new("RGB",(2,2),(100,100,100))
resultTile = buildTile(testImg, (30,30))
print(resultTile)
print("average color is ", resultTile[1])
resultTile[0].show()'''

def makeTileList(imageFileList, tileSize):
    wid,heg = tileSize
    tileList = []
    for k in imageFileList:
        newimg = Image.open(k)
        tile = buildTile(newimg,tileSize)
        tileList.append(tile)
    return tileList

'''testFileList = ["./tiles/04.jpg","./tiles/73.jpg"]
resultTileList = makeTileList(testFileList, (30,30))
print("average colors ", resultTileList[0][1], resultTileList[1][1])
resultTileList[0][0].show()
resultTileList[1][0].show()'''


def findBestThumb(pix, tileList):
    bestdis = 100,000
    for i in  tileList:
        thedis = distance(pix,i[1])
        if(thedis<bestdis):
            bestdis=thedis
            bestthumbnail =i[0]
    return bestthumbnail
            
'''testFileList = ["./tiles/04.jpg","./tiles/73.jpg"]
resultTileList = makeTileList(testFileList, (30,30))
print("average colors ", resultTileList[0][1], resultTileList[1][1])
bestThumb =findBestThumb((255,255,255), resultTileList)
bestThumb.show()'''


    

def stitchMosaic(img, tileList):
    image_thumb, avgcolor = tileList[0]
    wid,heg = image_thumb.size
    width,height = img.size
    newcanvas = Image.new("RGB", (wid*width,heg*height))
    for x in range(width):
        for y in range(height):
            color = img.getpixel((x,y))
            bestthumb = findBestThumb(color,tileList)
            PutBlock(bestthumb,newcanvas,(x*wid,y*heg))
    return newcanvas

            
    


# the buildMosaic function orchestrates the creation of the mosaic.
# It requires a target image file, and directory of images to use
# as a tile library, a tile size, and a mosaic resolution, as input.
# Though it returns nothing, its effect is to save a photoMosaic in
# a .jpg file.
def buildMosaic(imageFile, imageDirectory, tileSize, res):

    # Task 1:  create a list of image file names from a directory
    imgFileList = os.listdir(imageDirectory)
    for i in range(len(imgFileList)):
        imgFileList[i] = imageDirectory + imgFileList[i]

    # Task 2:  create a list of tiles by calling makeTileList.
    listofTile = makeTileList(imgFileList,(30,30))
    

    # Task 3:  scale target image by calling scaleTarget.
    theTargetScale = scaleTarget(imageFile,res)
    
    # Task 4:  create the mosaic image by calling stitchMosaic.
    theStich = stitchMosaic(theTargetScale,listofTile)
    
    # Task 5:  save the mosaic image to a file.
    theStich.show()

    

img1 =Image.open("green.jpg")
print(img1.size)
#final resolution 350,454

buildMosaic(img1, "./tiles/", (30,30), (30,30))

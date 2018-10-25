 # INFT1004 Introduction to Programming - Assignment 1
# Task: Fix the QR codes that the question provided.
# Author: Nguyen Quang Trung & Cheng Zixin
# Start Date: 24 Feb 2014
# End Date: 18 March 2014

def fixCodes(size):
  # Run each of the required functions in turn, displaying the resulting QR codes at the given size
  # image1 is just reduced; this will expand to the given size and display it
  image = makePicture(getMediaPath("image1.png"))
  repaint(expand(image, size))
  
  # image2 is reduced and inverted; this will invert it back, expand it, and display it
  image = makePicture(getMediaPath("image2.png"))
  repaint(expand(invert(image), size))
  
  # image3 is reduced and has had its positioning squares replaced with random modules
  image = makePicture(getMediaPath("image3.png"))
  repaint(expand(addSquares(image), size))
  
  # image4 has had all of its rows shifted by 12 positions, so it needs them shifted by another 13 to restore them
  image = makePicture(getMediaPath("image4.png"))
  repaint(expand(rowShift(image, 13), size))

  # image5 has had each row shifted by a different amount - the row index. Row 0 shifted by 0, row 1 by 1, and so on.
  # This will take a little work to undo!
  image = makePicture(getMediaPath("image5.png"))
  repaint(expand(progressiveRowShift(image), size))
  
  # All the images from here on are normal size, so they need to be reduced before being worked on
  # image6 simply needs to be reduced, then expanded for diaplay
  image = makePicture(getMediaPath("image6.png"))
  smallPic = reduce(image)
  repaint(expand(smallPic, size))

  # image7 has had all of its rows reflected about their centres; reflect them again to restore it
  image = makePicture(getMediaPath("image7.png"))
  smallPic = reduce(image)
  repaint(expand(rowReflect(smallPic), size))
  
  # image8 has had only alternate columns reflected about their centres, starting with column 0
  image = makePicture(getMediaPath("image8.png"))
  smallPic = reduce(image)
  repaint(expand(alternateColumnReflect(smallPic), size))

  # image9 has had only its active cells inverted
  image = makePicture(getMediaPath("image9.png"))
  smallPic = reduce(image)
  repaint(expand(invertActive(smallPic), size))

  #image10 has had a progressive row shift, like image5, but only shifting the active cells of each row
  image = makePicture(getMediaPath("image10.png"))
  smallPic = reduce(image)
  repaint(expand(progressiveRowShiftActive(smallPic), size))
  
  # image11 has been split into three parts, which need to be merged according to explicit instructions
  image = makePicture(getMediaPath("image11a.png"))
  smallPicA = reduce(image)
  image = makePicture(getMediaPath("image11b.png"))
  smallPicB = reduce(image)
  image = makePicture(getMediaPath("image11c.png"))
  smallPicC = reduce(image)
  repaint(expand(merge(smallPicA, smallPicB, smallPicC), size))
  
  
#Task 1 Author: Cheng Zixin
#Date: 24 February 2015 to 25 February 2015
def expand(smallPic,modileSize):
  #get piture size and pixels
  width=getWidth(smallPic)
  height=getHeight(smallPic)
  newPic=makeEmptyPicture((width+4)*modileSize,(height+4)*modileSize)
  for x in range(0,width):
    for y in range(0,height):
      sourcePixel=getPixelAt(smallPic,x,y)
      color=getColor(sourcePixel)
      # Define pixels coordinate
      startX=x*modileSize
      endX=startX+modileSize
      startY=y*modileSize
      endY=startY+modileSize
      # Set color to new picture
      # for loop range reserved a quiet zone around QR code
      for x1 in range(startX+2*modileSize,endX+2*modileSize):
        for y1 in range(startY+2*modileSize,endY+2*modileSize):
          endPixel=getPixelAt(newPic,x1,y1)
          setColor(endPixel,color) 
  repaint(newPic)
  return newPic


#Task 2 Author: Cheng Zixin
#Date: 25 February 2015 
def invert(smallPic):
  # Get picture pixels
  for pixel in getPixels(smallPic):
    # Get pixel RGB color value
    red=getRed(pixel)
    green=getGreen(pixel)
    blue=getBlue(pixel)
    # convert color RGB value
    invertedColor=makeColor(255-red,255-green,255-blue)
    setColor(pixel,invertedColor)
  return smallPic
  
  
#Task 3 Author: Cheng Zixin
#Date: 26 February 2015 to 27 February 2015
def addSquares(smallPic):
  # Draw the position square
  square=makeEmptyPicture(7,7)
  for square_x1 in range(0,7):
    for square_y1 in range(0,7):
      squarePixel_1=getPixelAt(square,square_x1,0)
      setColor(squarePixel_1,black)
      squarePixel_2=getPixelAt(square,0,square_y1)
      setColor(squarePixel_2,black)
      squarePixel_3=getPixelAt(square,6,square_y1)
      setColor(squarePixel_3,black)
      squarePixel_4=getPixelAt(square,square_x1,6)
      setColor(squarePixel_4,black)
  for square_x2 in range(2,5):
    for square_y2 in range(2,5):
      squarePixel_5=getPixelAt(square,square_x2,square_y2)
      setColor(squarePixel_5,black)
  #Get the target pixels and set color
  srcWidth=7
  srcHeight=7
  tgtWidth=getWidth(smallPic)
  tgtHeight=getHeight(smallPic)
  for x in range(0,srcWidth):
    for y in range(0,srcHeight):
      srcPixel=getPixelAt(square,x,y)
      tgtPixel_1=getPixelAt(smallPic,x,y)
      tgtPixel_2=getPixelAt(smallPic,x+tgtWidth-srcWidth,y)
      tgtPixel_3=getPixelAt(smallPic,x,y+tgtHeight-srcHeight)
      color=getColor(srcPixel)
      setColor(tgtPixel_1,color)
      setColor(tgtPixel_2,color)
      setColor(tgtPixel_3,color)
  #set white cells
  for x in range(0,8):
    for y in range(0,8):
      whiteCell_x1=getPixelAt(smallPic,x,srcHeight)
      whiteCell_x2=getPixelAt(smallPic,x+tgtWidth-srcWidth-1,srcHeight)
      whiteCell_x3=getPixelAt(smallPic,x,tgtHeight-srcHeight-1)
      whiteCell_y1=getPixelAt(smallPic,srcWidth,y)
      whiteCell_y2=getPixelAt(smallPic,tgtWidth-srcWidth-1,y)
      whiteCell_y3=getPixelAt(smallPic,srcWidth,y+tgtWidth-srcWidth-1)
      setColor(whiteCell_x1,white)
      setColor(whiteCell_x2,white)
      setColor(whiteCell_x3,white)
      setColor(whiteCell_y1,white)
      setColor(whiteCell_y2,white)
      setColor(whiteCell_y3,white)
  return smallPic
  
  
#Task 4 Author: Cheng Zixin
#Date: 27 February 2015
def rowShift(smallPic,shiftSize):
  width=getWidth(smallPic)
  height=getHeight(smallPic)
  newPic=makeEmptyPicture(25,25)
  for src_x in range(0,width):
    for src_y in range(0,height):
      srcPixel=getPixelAt(smallPic,src_x,src_y)
      color=getColor(srcPixel)
      if src_x<shiftSize-1: # source left part
        tgtPixel=getPixelAt(newPic,shiftSize+src_x,src_y)
      else: # source right part
        tgtPixel=getPixelAt(newPic,src_x-shiftSize+1,src_y)
      setColor(tgtPixel,color)
  return newPic
  
  
#Task 5 Author: Cheng Zixin
#Date: 2 March 2015
def progressiveRowShift(smallPic):
  #get the source pixel, width and height
  width=getWidth(smallPic)
  height=getHeight(smallPic)
  newPic=makeEmptyPicture(25,25)
  for x in range(0,width):
    for y in range(0,height):
      srcPixel=getPixelAt(smallPic,x,y)
      #set the target pixel
      #x+y<=24 shift to the right directly
      if x+y<=24:
        tgtPixel_1=getPixelAt(newPic,x+y,y)
        color=getColor(srcPixel)
        setColor(tgtPixel_1,color)
      #x+y>24 warp
      else: 
        tgtPixel_2=getPixelAt(newPic,x+y-25,y)
        color=getColor(srcPixel)
        setColor(tgtPixel_2,color)
  return newPic


#Task 6 Author: Cheng Zixin
#Date: 3 March 2015
def reduce(qrPic):
  #get souece piture size 
  width=getWidth(qrPic)
  height=getHeight(qrPic)
  # get the quiet zone size
  quiet_size=0
  isBlack=false
  for x_quiet in range(0,width):
    for y_quiet in range(0,height):
      quietPixel=getPixelAt(qrPic,x_quiet,y_quiet)
      quietColor=getColor(quietPixel)
      if distance(quietColor, black) < 100 and x_quiet==y_quiet:
        quiet_size=y_quiet
        isBlack=true
        break
    if isBlack :
       break
  #get the positioning square size
  temp=0
  isWhite=false
  for x_module in range(quiet_size,width):
    for y_module in range(quiet_size,width):
      modulePixel=getPixelAt(qrPic,x_module,y_module)
      moduleColor=getColor(modulePixel)
      if distance(moduleColor,white) < 100:
        temp=y_module
        isWhite=true
        break
    if isWhite :
       break
  moduleSize=temp-quiet_size
  #calculate the multiple
  #When the QR Code size is equals to 25, the positioning square size is equals to 7.
  multiple=moduleSize/7
  #remove the quiet zone.
  noQuietZonePicWidth=width-quiet_size*2
  noQuietZonePicHeight=height-quiet_size*2
  noQuietZonePic=makeEmptyPicture(noQuietZonePicWidth,noQuietZonePicHeight)
  for x_noQuiet in range(0,noQuietZonePicWidth):
    for y_noQuiet in range(0,noQuietZonePicHeight):
      noQuietPixel=getPixelAt(noQuietZonePic,x_noQuiet,y_noQuiet)
      noQuietSrcPixel=getPixelAt(qrPic,x_noQuiet+quiet_size,y_noQuiet+quiet_size)
      noQuietSrcColor=getColor(noQuietSrcPixel)
      setColor(noQuietPixel,noQuietSrcColor)
  #reduce the noQuietZonePic 7 times
  newPic=makeEmptyPicture(25,25)
  for x in range(0,noQuietZonePicWidth):
    for y in range(0,noQuietZonePicHeight):
      srcPixel=getPixelAt(noQuietZonePic,x,y)
      color=getColor(srcPixel)
      if (x+1)%multiple==0 and (y+1)%multiple==0:
        tgtPixel_1=getPixelAt(newPic,(x+1)/multiple-1,(y+1)/multiple-1)
        setColor(tgtPixel_1,color)
      elif x==0 and y==0:
        tgtPixel_2=getPixelAt(newPic,(x+1)/multiple,(y+1)/multiple)
        setColor(tgtPixel_2,color)
  return newPic
  
  
#Task 7 Author: Nguyen Quang Trung
#Date: 04 March 2015
def rowReflect(smallPic):
  width = getWidth(smallPic)
  height = getHeight(smallPic)
  newPic = makeEmptyPicture(width,height)
  for x in range(0,width):
    for y in range(0,height):
      ScrPixel = getPixelAt(smallPic,x,y)
      #Get Pixel for newPic, modifying the x values
      EndPixel = getPixelAt(newPic,width-1-x,y)
      newColor = getColor(ScrPixel)
      setColor(EndPixel,newColor)
  return newPic
  
  
#Task 8 Author: Nguyen Quang Trung
#Date: 04 March 2015
def alternateColumnReflect(smallPic):
  width = getWidth(smallPic)
  height = getHeight(smallPic)
  newPic = makeEmptyPicture(width,height)
  for x in range(0,width):
    for y in range(0,height):
      ScrPixel = getPixelAt(smallPic,x,y)
      #Select only columnns of even number based on x-cooridnate of pixels
      if x%2 == 0:
        EndPixel = getPixelAt(newPic,x,height-y-1)
        newColor = getColor(ScrPixel)
        setColor(EndPixel,newColor)
      #Columns of odd number remain the same
      else:
        EndPixel = getPixelAt(newPic,x,y)
        newColor = getColor(ScrPixel)
        setColor(EndPixel,newColor)
  return newPic
  
  
#Task 9 Author: Nguyen Quang Trung
#Date: 04 March 2015 
def invertActive(smallPic):
  #Get Pixels of the first section
  for x in range (0,8):
    for y in range (8,17):
      pixel = getPixelAt(smallPic,x,y)
      # Get pixel RGB color value
      red=getRed(pixel)
      green=getGreen(pixel)
      blue=getBlue(pixel)
      # convert color RGB value
      invertedColor=makeColor(255-red,255-green,255-blue)
      setColor(pixel,invertedColor)
  #Get Pixels of the second section
  for x in range (8,17):
    for y in range (0,25):
      pixel = getPixelAt(smallPic,x,y)
      # Get pixel RGB color value
      red=getRed(pixel)
      green=getGreen(pixel)
      blue=getBlue(pixel)
      # convert color RGB value
      invertedColor=makeColor(255-red,255-green,255-blue)   
      setColor(pixel,invertedColor)
   #Get Pixels of the third section
  for x in range (17,25):
    for y in range (8,25):
      pixel = getPixelAt(smallPic,x,y)
      # Get pixel RGB color value
      red=getRed(pixel)
      green=getGreen(pixel)
      blue=getBlue(pixel)
      # convert color RGB value
      invertedColor=makeColor(255-red,255-green,255-blue)   
      setColor(pixel,invertedColor)
  return smallPic
  
  
#Task 10 Author: Nguyen Quang Trung
#Date: 10 March 2015 to 12 March 2015
def progressiveRowShiftActive(smallPic): 
  width=getWidth(smallPic)
  height=getHeight(smallPic)
  newPic=makeEmptyPicture(25,25)
  #copy the squares into newPic
  for x in range (0,25):
    for y in range (0,25):
      scrPixel=getPixelAt(smallPic,x,y)
      tgtPixel=getPixelAt(newPic,x,y) 
      color=getColor(scrPixel)  
      setColor(tgtPixel,color)
  #modify the first sectioin
  for y in range (0,8):
    for x in range (8,17):
      srcPixel1=getPixelAt(smallPic,x,y)
      #set the target pixel
      #active area: shift directly to the right
      if x+y<17:
        tgtPixel_1=getPixelAt(newPic,x+y,y)
        color=getColor(srcPixel1)
        setColor(tgtPixel_1,color)
      #to avoid top right square: x+y-9
      elif x+y<=24:
        tgtPixel_1=getPixelAt(newPic,x+y-9,y)
        color=getColor(srcPixel1)
        setColor(tgtPixel_1,color)
      #x+y>25: to avoid top left square: x+y-17
      else: 
        tgtPixel_2=getPixelAt(newPic,x+y-17,y)
        color=getColor(srcPixel1)
        setColor(tgtPixel_2,color)
  #modify the second section
  for y in range (8,17):
    for x in range (0,25):
      srcPixel2=getPixelAt(smallPic,x,y)
      #set the target pixel
      #x+y<=24 shift to the right directly      
      if x+y<=24:
        tgtPixel_1=getPixelAt(newPic,x+y,y)
        color=getColor(srcPixel2)
        setColor(tgtPixel_1,color)
      #x+y>24 warp
      else: 
        tgtPixel_2=getPixelAt(newPic,x+y-25,y)
        color=getColor(srcPixel2)
        setColor(tgtPixel_2,color)
  #modify the third section
  for y in range (17,25):
    for x in range (8,25):
      srcPixel3=getPixelAt(smallPic,x,y)
      #set the target pixel
      #x+y<=24 shift to the right directly
      if x+y<=24:
        tgtPixel_1=getPixelAt(newPic,x+y,y)
        color=getColor(srcPixel3)
        setColor(tgtPixel_1,color) 
      #to avoid bottom left square: x+y-17     
      elif x+y<42: 
        tgtPixel_2=getPixelAt(newPic,x+y-17,y)
        color=getColor(srcPixel3)
        setColor(tgtPixel_2,color)    
      #to avoid square but also shift into the right position         
      else: 
        tgtPixel_3=getPixelAt(newPic,x+y-34,y)
        color=getColor(srcPixel3)
        setColor(tgtPixel_3,color)     
  return newPic
  
  
#Task 11 Author: Nguyen Quang Trung
#Date: 18 March 2015
def merge(smallPicA, smallPicB, smallPicC):
  newPic=makeEmptyPicture(25,25)
  for x in range (0,25):
    for y in range (0,25):
      scrPixelA=getPixelAt(smallPicA,x,y)
      colorA=getColor(scrPixelA)
      scrPixelB=getPixelAt(smallPicB,x,y)
      colorB=getColor(scrPixelB)
      scrPixelC=getPixelAt(smallPicC,x,y)
      colorC=getColor(scrPixelC)
      if distance(colorA,colorB)==0:
        tgtPixel=getPixelAt(newPic,x,y)
        setColor(tgtPixel,colorA)
      else:
        tgtPixel=getPixelAt(newPic,x,y)
        setColor(tgtPixel,colorC)
  return newPic


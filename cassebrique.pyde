posRacketX = 0
posRacketY = 0

posBallX = 0
posBallY = 0

speedBallX = 3
speedBallY = 2

rectWidth = 50
rectHeight = 10

baseHeightRacket = 40
baseSizeBall = 20

baseWidthBrick = 50 
baseHeightBrick = 10 
niveau1 = [
           [1,1,1,1,1,1,1,1],
           [0,1,1,1,1,1,1,0],
           [0,0,1,1,1,1,0,0],
           [0,0,0,1,1,0,0,0],
           [0,0,0,1,1,0,0,0]
        ]

def setup():
    size(400,500)
    frameRate(75)

def draw():
    clear()
    drawRacket()
    drawBall()
    drawBricks()
    mouvBall()
    rebondRacket()
    rebondBrick()
    
def drawRacket():
    fill(255)
    global posRacketX,posRacketY, rectWidth, rectHeight, baseHeightRacket
    posRacketX = mouseX - rectWidth/2
    posRacketY = height - baseHeightRacket
    rect(posRacketX, posRacketY, rectWidth, rectHeight)
    
def drawBall():
    fill(255)
    global posBallX,posBallY, baseSizeBall
    circle(posBallX,posBallY, baseSizeBall)
    
def mouvBall():
    global posBallX,posBallY, speedBallX, speedBallY
    posBallX += speedBallX
    posBallY += speedBallY
    if posBallX >= width:
        speedBallX *= -1
    if posBallY >= height:
        speedBallY *= -1
    if posBallX <= 0:
        speedBallX *= -1
    if posBallY <= 0:
        speedBallY *= -1
        
def rebondRacket():
    global posRacketX,posRacketY, posBallX,posBallY, speedBallX, speedBallY,rectWidth, rectHeight
    if posBallY > posRacketY+rectHeight*2: 
        print("perdu")
        exit()
    if posBallY > posRacketY and posRacketX <= posBallX <= posRacketX+rectWidth:
        speedBallY *= -1
        
def drawBricks():
    global niveau1,baseWidthBrick,baseHeightBrick
    fill(255)
    for i in range(len(niveau1)):
        for j in range(len(niveau1[i])):
            if niveau1[i][j] == 1: 
                rect(j*baseWidthBrick,i*baseHeightBrick,baseWidthBrick ,baseHeightBrick)
            j += 1
        i += 1

def rebondBrick():
    global niveau1,posBallX,posBallY, speedBallX, speedBallY, baseWidthBrick,baseHeightBrick
    for i in range(len(niveau1)):
        for j in range(len(niveau1[i])):
            if j*baseWidthBrick <= posBallX <= j*baseWidthBrick +baseWidthBrick and i*baseHeightBrick <= posBallY <= i*baseHeightBrick+baseHeightBrick and niveau1[i][j] == 1:
                print("ca touche")
                niveau1[i][j] = 0                                             
        j += 1
    i += 1    
    

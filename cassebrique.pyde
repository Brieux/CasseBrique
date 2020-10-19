posRacketX = 0
posRacketY = 0

posBallX = 200
posBallY = 250

speedBallX = 0.20
speedBallY = 0.17
speedBall = 0.15
ballAngle = random(PI/6, 5*PI/6)
rectWidth = 75
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

lastFrameTime = 0
dt = 0
angleMax = PI/1.9

def setup():
    global lastFrameTime, dt
    size(400,500)
    frameRate(60)
    lastFrameTime = millis()

def draw():
    global lastFrameTime, dt
    dt = millis() - lastFrameTime
    lastFrameTime = millis()
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
    global posBallX,posBallY, speedBallX, speedBallY,dt, speedBall, ballAngle, baseSizeBall
    posBallX += cos(ballAngle) * speedBall * dt
    posBallY += sin(ballAngle) * speedBall * dt
    
    if posBallX >= width-baseSizeBall/2:
        posBallX = width - baseSizeBall/2
        ballAngle = PI-ballAngle
        
    if posBallY >= height-baseSizeBall/2:
        posBallY = height-baseSizeBall/2
        ballAngle = 2*PI - ballAngle
        
    if posBallX <= baseSizeBall/2:
        posBallX = baseSizeBall/2
        ballAngle = PI-ballAngle
        
    if posBallY <= baseSizeBall/2:
        posBallY =baseSizeBall/2
        ballAngle = 2*PI - ballAngle
        
def rebondRacket():
    global posRacketX,posRacketY, posBallX,posBallY, speedBallX, speedBallY,rectWidth, rectHeight
    if posBallY > posRacketY+rectHeight*2: 
        print("perdu")
        #exit()
    if posBallY > posRacketY and posRacketX <= posBallX <= posRacketX+rectWidth:
        print("rebond")
        
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
                niveau1[i][j] = 0                                             
        j += 1
    i += 1    
    

ballX = 0
ballY = 0

ballSpeed = 0.2
ballSpeedY = 0.2
ballSpeedX = 0.2
ballAngle = PI

ballRadius = 5
ballAngleMax = PI/1.9

racketWidth = 100
racketHeight = 10
racketX = 0
racketY = 0

lastFrameTime = 0
deltaTime = 0

baseWidthBrick = 50 
baseHeightBrick = 10 
niveau1 = [
           [1,1,1,1,1,1,1,1],
           [0,1,1,1,1,1,1,0],
           [0,0,1,1,1,1,0,0],
           [0,0,0,1,1,0,0,0],
           [0,0,0,1,1,0,0,0]
        ]

#ici on definit la fonction setup qui sera exécuté comme point d'entré dans mon code
def setup():
    #on dit qu'on va faire référence à la variable global
    global ballX, ballY, racketX, racketY, racketWidth
    global lastFrameTime
    #on appel la fonction print pour écrire dans la console
    print("Hello World")
    #on definit la taille de la fenêtre
    size(400, 400)
    #vide la fenêtre
    clear()
    #on change le frameRate de l'application
    frameRate(30)
    ballX = width/2
    ballY = height/2
    
    racketX = mouseX - (racketWidth/2)
    racketY = height - 50
    
    lastFrameTime = millis()
    
def draw():
    global deltaTime, lastFrameTime
    
    clear()
    
    deltaTime = millis() - lastFrameTime
    lastFrameTime = millis()
    
    drawRacket()
    drawBall()
    drawBricks()
    
    
    
def drawRacket():
    global racketX, racketY, racketWidth, racketHeight
    fill(255)
    #draw a rectangle in coords
    # x : mouseX minus half of width
    # y : height of the window minus 20
    # width : 50
    # height : 10
    racketX = mouseX - (racketWidth/2)
    rect(racketX, racketY, racketWidth, racketHeight)
    
def drawBall():
    global ballX, ballY, ballRadius, ballAngle, ballSpeed, ballSpeedX, ballSpeedY
    global racketX, racketY, racketWidth, racketHeight
    global deltaTime
    global ballAngleMax
    
    #idem a ce qu'il y a au dessus
    ballSpeedX = cos(ballAngle) * ballSpeed * deltaTime
    ballSpeedY = sin(ballAngle) * ballSpeed * deltaTime
    ballX += ballSpeedX
    ballY -= ballSpeedY
    
    #haut et bas   
    if(ballY-ballRadius < 0):
        ballAngle = -ballAngle
        ballY = ballRadius
    elif(ballY+ballRadius > height):
        ballAngle = -ballAngle
        ballY = height-ballRadius
    
    #droite et gauche
    if(ballX+ballRadius > width):
        ballAngle = PI - ballAngle
        ballX = width-ballRadius
    elif(ballX-ballRadius < 0):
        ballAngle = PI - ballAngle
        ballX = ballRadius
    
    if(racketY < ballY+ballRadius < racketY+racketHeight and ballSpeedY < 0):
        if(racketX < ballX < racketX + racketWidth):
            ratio = (ballX - racketX - racketWidth/2) / (racketWidth/2)
            ballAngle = PI/2 - ratio * ballAngleMax
            ballY = racketY-ballRadius
    
    
    #draw circle
    circle(ballX, ballY, 2*ballRadius);
    
def drawBricks():
    global niveau1,baseWidthBrick,baseHeightBrick
    global ballX, ballY, ballRadius
    global ballAngle, ballSpeedX, ballSpeedY,ballSpeed
    
    fill(255)
    # for i in range(len(niveau1)):
    #     for j in range(len(niveau1[i])):
    #         if niveau1[i][j] == 1: 
    #             rect(j*baseWidthBrick,i*baseHeightBrick,baseWidthBrick ,baseHeightBrick)
    #         j += 1
    #     i += 1
    
    # #Test de collision avec la balle
    
    # for k in range(len(niveau1)):
    #     for l in range(len(niveau1[k])):
    #         if niveau1[k][l] == 1: 
    #             #par dessous
    #             if ballSpeedY > 0 and j*baseWidthBrick < ballX + ballRadius < j*baseWidthBrick + baseWidthBrick and ballY + ballRadius  < i*baseHeightBrick :
    #                 print("ca tape par dessous")
                
    #             #par dessus
                
                
                
    #             #par la droite
                
                
                
    #             #par la gauche
                
                
                
    #         l += 1
    #     k += 1
    bX = 150
    bY = 150
    bW = 100
    bL = 100
    rect(bX, bY, bW, bL)
    if ballSpeedY > 0 and bX < ballX + ballRadius <bX + bW and ballY + ballRadius  <= bY + bL :
        print("ca tape par dessous")
    if ballSpeedY < 0 and bX < ballX + ballRadius <bX + bW and ballY + ballRadius  >= bY :
        print("ca tape par dessus")
    if ballSpeedX > 0 and ballX + ballRadius <= bX + bW and bY < ballY + ballRadius  < bY + bL :
        print("ca tape par la droite")
    if ballSpeedX < 0 and ballX + ballRadius >= bX and bY < ballY + ballRadius  < bY + bL :
        print("ca tape par la gauche")
                
                   
                      
                         
                            
        

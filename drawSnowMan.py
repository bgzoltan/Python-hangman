def drawSnowMan(badHits, moveTo,myTurtle):

    if badHits==1:
        # the ground
        moveTo(0,0)
        myTurtle.forward(100)
        myTurtle.backward(200)

    # body
    bodyRadius1=60
    bodyRadius2=40
    if badHits==2:
        # body 1
        moveTo(0,0)
        myTurtle.circle(bodyRadius1)

    body2Position=2*bodyRadius1
    if badHits==3:
        # body 2
        moveTo(0,body2Position)
        myTurtle.circle(bodyRadius2)
   
    # arms
    armDistanceFromBody2=50
    armLength=40
    if badHits==4:
        # arm rigth
        moveTo(bodyRadius2,2*bodyRadius1+armDistanceFromBody2)
        myTurtle.left(45)
        myTurtle.forward(armLength)
        myTurtle.left(90)

    if badHits==5:
        # arm left
        moveTo(-bodyRadius2,2*bodyRadius1+armDistanceFromBody2)
        myTurtle.forward(armLength)
        myTurtle.right(135)


    # head
    headRadius=30
    headPosition=body2Position+2*bodyRadius2
    if badHits==6:
        moveTo(0,headPosition)
        myTurtle.circle(headRadius)

    # eyes
    eyesPosition=headPosition+headRadius
    eyesRadius=4
    distanaceBetweenEyes=20
    if badHits==7:
        # left eye
        moveTo(-distanaceBetweenEyes/2,eyesPosition)
        myTurtle.circle(eyesRadius)

    if badHits==8:
        # right eye
        moveTo(distanaceBetweenEyes/2,eyesPosition)
        myTurtle.circle(eyesRadius)
  
    # mouth
    mouthPosition=headPosition+10
    if badHits==9:
        moveTo(0,mouthPosition)
        myTurtle.circle(20,60)
        moveTo(0,mouthPosition)
        myTurtle.right(240)
        myTurtle.circle(-20,60)
        myTurtle.right(120)

    # heat
    heatPosition=headPosition+2*headRadius
    heatTopWidth=30
    heatTopHeight=40
    if badHits==10:
        moveTo(0,heatPosition)
        myTurtle.forward(heatTopWidth)
        myTurtle.backward(2*heatTopWidth)
        moveTo(0,heatPosition)
        myTurtle.forward(heatTopWidth/2)
        myTurtle.left(90)
        myTurtle.forward(heatTopHeight)
        myTurtle.left(90)
        myTurtle.forward(heatTopWidth)
        myTurtle.left(90)
        myTurtle.forward(heatTopHeight)
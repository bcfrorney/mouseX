def setup():
    size(600, 400)
    
    rect( 180,70,300,300)
    rect( 245, 95, 230,240)
    fill(0,255,0)
    rect( 185,80,50,50)
    fill(0,0,255)
    rect( 185, 125, 50,50)
    fill(255,0,0)
    rect(185, 175,50,50)
    fill(255,205,200)
    rect(185,220,50,50)
    fill(200,185,255)
    rect(185,265,50,50)
    fill(100,100,100)
    rect(185,315,50,50)
    
def draw():
    if mousePressed and mouseX >= 245 and mouseX <= 475 and mouseY >= 95 and mouseY <= 335:
        line (pmouseX, pmouseY, mouseX, mouseY)
    

    


    
    

    
    
    

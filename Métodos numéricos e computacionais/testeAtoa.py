import math
import time

So = [0,0]
Pos = [0,0]

velAng = 0.01              #rad/s
timeAnt = time.time()
teta = (time.time() - timeAnt) * velAng

def distEpicentro():
    return math.sqrt((Pos[0]-So[0])**2 + (Pos[1]-So[1])**2)

if __name__ == "__main__":
    So = [0,0]
    Pos = [2,2]

    while(True):
        teta = (time.time() - timeAnt ) * velAng            # Angulo é o tempo * velocidade angular
        Pos[0] = distEpicentro() * math.cos(teta)           # Pos X é Cos(0)
        Pos[1] = distEpicentro() * math.sin(teta)           # Pos Y é Sen(0)        
        
        timeAnt = time.time()
        
        print(Pos)
        
        time.sleep(1)





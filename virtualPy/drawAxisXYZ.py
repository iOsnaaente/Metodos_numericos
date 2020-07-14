import vpython  as vp 

# USING VIRTUAL PYTHON TO PLOT THE XYZ AXIS 
def drawAxisXYZ(rangeX=[0,0], rangeY=[0,0], rangeZ=[0,0]):
    origin = vp.vector(0,0,0)
    radius = 0.3
    vp.sphere(pos = origin, radius = 2, color = vp.color.yellow)
    
    for i in range(2):
        vp.arrow (pos = origin, axis = vp.vector(rangeX[i],0,0), shaftwidth=radius, color = vp.color.green)
        vp.arrow (pos = origin, axis = vp.vector(0,rangeY[i],0), shaftwidth=radius, color = vp.color.red)
        vp.arrow (pos = origin, axis = vp.vector(0,0,rangeZ[i]), shaftwidth=radius, color = vp.color.blue)
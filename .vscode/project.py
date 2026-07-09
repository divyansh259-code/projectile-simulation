import numpy as np

def trajectory(v0, angle_degrees, drag_coeff=0.1, time_max=5, steps=200):
    g = 9.8
    anglerad = np.radians(angle_degrees)
    
    vx0 = v0 * np.cos(anglerad)
    vy0 = v0 * np.sin(anglerad)
    
    t = np.linspace(0, time_max, steps)
    
    xideal = vx0 * t
    yideal = vy0 * t - 0.5 * g * t**2
    yideal = np.maximum(0, yideal) 
    
    dt = t[1] - t[0]
    xreal = [0.0]
    yreal = [0.0]
    vx = vx0
    vy = vy0

    for i in range(1, len(t)):
        ax = -drag_coeff * vx
        ay = -g - drag_coeff * vy
        
        vx += ax * dt
        vy += ay * dt
        
        posx = xreal[-1] + vx * dt
        posy = yreal[-1] + vy * dt
        
        if posy < 0:
            posx = xreal[-1]
            posy = 0.0
            vx = 0.0
            vy = 0.0
            
        xreal.append(posx)
        yreal.append(posy)
        
    return t, xideal, yideal, np.array(xreal), np.array(yreal)
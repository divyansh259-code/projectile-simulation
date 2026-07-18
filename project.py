import numpy as np

def trajectory(v0, theta, dragcoeff=0.1, dt=0.01):
    g = 9.8
    theta_rad = np.radians(theta) #angle converted for numpy
    vx0 = v0 * np.cos(theta_rad)
    vy0 = v0 * np.sin(theta_rad) #def vx n vy initially

    x = [0]
    y = [0]           #real x, y and t
    t = [0]
    vx, vy = vx0, vy0   #real vx and vy equal to defined vx0 and vy0 initially
    tcurrent = 0        #t at 0

    while y[-1] >= 0: #while y is above ground
        ax = -dragcoeff * vx
        ay = -g - dragcoeff * vy
        vx += ax * dt
        vy += ay * dt   #updated the velocity
        tcurrent += dt      

        x.append(x[-1] + vx * dt)       #updated the position
        y.append(y[-1] + vy * dt)
        t.append(tcurrent)      

    x = np.array(x) #for plotting
    y = np.array(y)
    t = np.array(t)

    xideal = vx0*t
    yideal = vy0*t - 0.5*g*t**2 #ideal w/o drag

    return x, y, t, xideal, yideal

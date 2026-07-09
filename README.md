Projectile Motion with Fluid Drag---------

A physics simulation that uses numpy to model how linear air resistance affects a projectile's trajectory compared to it's theoretical path.

Mechanics and Method---------

In an ideal vacuum, the vertical coordinate is calculated using the standard kinematic equation:

y(t) = v0 * sin(theta) * t - 0.5 * g * t^2

However, when modeling air drag, the drag force acts directly opposite to the velocity vector. This simulation assumes a linear drag model where the acceleration components are dependent on velocity:

ax = -c * vx
ay = -g - c * vy

Because the total acceleration is non-constant, analytical equations become complex. Instead, the simulation uses the Euler method to numerically integrate the equations of motion across dt:

vx(t + dt) = vx(t) + ax * dt
vy(t + dt) = vy(t) + ay * dt

x(t + dt) = x(t) + vx(t + dt) * dt
y(t + dt) = y(t) + vy(t + dt) * dt

The loop runs sequentially across the time array and applies a condition to terminate updates once the projectile's vertical component drops below the ground (y < 0).

# Ray Tracing in a Weekend

I followed this tutorial but in Python: https://www.realtimerendering.com/raytracing/Ray%20Tracing%20in%20a%20Weekend.pdf

## Steps

### Chapter 1 . Output an image

We write the data into a .ppm (plain pixmap) file, which can be opened by a standard image viewer.

File structure:
- P3: indicates that the colors are in ASCII text format (RGB)
- 200 100: width × height in pixels
- 255: maximum color value per channel
- RGB values: the color codes for all 20,000 pixels follow in sequence

Using a nested for loop, we iterate through the pixels—moving from top to bottom, and row by row from left to right—to calculate their color values. From the loop variables, a relative value between 0.0 and 1.0 is derived, which is then scaled up to a range of 0 to 255.

The final result is an image with a color gradient:
- the R value increases from left to right
- the G value increases from bottom to top
- the B value remains constant (0.2)

### Chapter 2 - The Vec3 class

We will create the Vec3 class to replace the raw float variables (R, G, B) used in Chapter 1; it serves to store geometric vectors and colors. We will use it to store colors, positions, directions, offsets—essentially anything.

### Chapter 3 - Rays, a simple camera, and background

We introduce the Ray class, which sets up a virtual camera and generates the background using rays.
The mathematical formula for a ray is: P(t) = A + t * B

A – the starting point (origin) of the ray

B – the direction of the ray

t – a floating-point number (parameter); as we vary its value, we traverse the line defined by the ray.

The color(r: Ray) function is responsible for determining the color of the point hit by the ray. Since there are no objects yet, we perform a linear interpolation between white and pale blue based on the ray's Y-axis component.

### Chapter 4 - Adding a sphere

We place the first 3D shape: a sphere.

Center of the sphere: C = (cx, cy, cz)

Radius: R

For any arbitrary point P(x, y, z) on its surface, the following holds: (P - C) * (P - C) = R^2

Substituting the equation of the light ray into the equation of the sphere yields a quadratic equation for the parameter t:

t^2 * (B * B) + 2t * (B * (A - C)) + (A - C) * (A - C) - R^2 = 0

If its discriminant (b^2 - 4ac) > 0, then the ray intersects the sphere. This is what the hit_sphere function determines.

We modify the color function so that, before drawing the background, it checks whether the ray hits the sphere placed in the scene. If it does, the pixel becomes solid red (Vec3(1, 0, 0)); otherwise, it remains the familiar blue-and-white sky. We position the sphere slightly "inward" from the origin of the coordinate system—along the Z = -1 axis—with a radius of 0.5.

### Chapter 5 - Surface normals and multiple objects

We introduce surface normal vectors (which indicate the direction the sphere's surface is facing at a given point) and modify the code to handle an arbitrary number of objects (spheres) simultaneously.

The Sphere class represents spheres. When solving the equation for a sphere, we do not merely check whether the discriminant is greater than 0; we also calculate the specific value of $t$ (the smaller positive root of the quadratic equation). The normal vector is obtained as a vector pointing from the hit point toward the center of the sphere: N = (P - C) / R

### Chapter 6 - Antialiasing

Previously, the renderer cast a single ray straight through the center of each pixel. If the ray hit an object, the pixel took that color; otherwise, it took the background color. This binary approach created harsh, jagged edges ("jaggies") along object boundaries because pixels were treated as all-or-nothing.

To fix this, the program now launches multiple random rays distributed across the area of each individual pixel.

The colors returned by all these sub-rays are collected and averaged. For example, if a pixel sits right on the edge of a sphere where 50% of its sub-rays hit the object and 50% hit the background, its final color becomes a 50/50 blend. This produces a smooth, natural transition along the edges.

### Chapter 7 - Diffuse Materials

Unlike shiny, reflective surfaces, matte (diffuse) surfaces scatter reflected light in random directions rather than a precise angle.

Mathematical Modeling of Scattering:
- At the point of intersection, a surface normal vector (n) is established.
- A unit hemisphere is imagined around the tip of this normal vector, and a random point within it determines the new direction of the scattered ray.

With every diffuse bounce, rays lose light energy due to absorption (multiplying by the material's color). Because rays are generated recursively, a max_depth limit is enforced to prevent infinite loops. If a ray bounces too many times and hits this limit, it stops contributing light and turns black.

"Shadow Acne": Floating-point inaccuracies can cause a newly bounced ray to falsely intersect with the exact same surface it just left. To fix this, a minimum threshold (t_min = 0.001) ensures that intersection tests start slightly above the surface.

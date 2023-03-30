# Mandelbrot-Visualizer
This project uses the pygame library to visualize the Mandelbrot Set.
This set is an extremely popular image from mathematics. The series is found by computing
the function $f_c(z) = z^2 + c$. Z always begins at 0, but c can be any number in the complex plane.
Here is an example for c = 1. $f_1(0) = 0^2 + 1 = 1$, then $f_1(1) = 1^2 + 1 = 2$. This value carries on to
infinity, so 1 is not in the mandelbrot set. In our case, numbers in the mandelbrot set are colored white. Seeing if 
$f_c(f_c(f_c(...f_c(0))))$ converges or diverges and coloring that point $c$ based on that creates a fractal.  


To view the fractal more clearly my program lets users zoom and move in all four directions. Zooming in and out by a large factor is controlled by **g** and **h**. Zooming in and out by a small factor is controlled by **o** and **p**. Moving is controlled by the arrow keys, and for more precise movements you can use **q**,**w**,**e**, and **r** for right,left,up, and down respectively.  

**Here is a picture showing a visualization from my program**  
![PICTURE](https://user-images.githubusercontent.com/70726788/228690583-a756a40e-6c6b-40ad-b42a-dc2ca0419dfc.jpg)

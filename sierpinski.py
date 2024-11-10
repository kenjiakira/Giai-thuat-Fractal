import matplotlib.pyplot as plt

def draw_triangle(vertices, color='k'):
    triangle = plt.Polygon(vertices, color=color)
    plt.gca().add_patch(triangle)

def sierpinski(vertices, depth):
    if depth == 0:
        draw_triangle(vertices)
    else:
       
        midpoints = [
            [(vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2],
            [(vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2],
            [(vertices[2][0] + vertices[0][0]) / 2, (vertices[2][1] + vertices[0][1]) / 2]
        ]
        
        sierpinski([vertices[0], midpoints[0], midpoints[2]], depth - 1)
        sierpinski([vertices[1], midpoints[0], midpoints[1]], depth - 1)
        sierpinski([vertices[2], midpoints[1], midpoints[2]], depth - 1)

vertices = [[-1, -0.5], [1, -0.5], [0, np.sqrt(3) - 0.5]]
depth = 5 
plt.figure()
sierpinski(vertices, depth)
plt.gca().set_aspect('equal')
plt.axis('off')
plt.title("Sierpinski Triangle")
plt.show()

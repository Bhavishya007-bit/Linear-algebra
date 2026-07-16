import numpy as np
import matplotlib.pyplot as plt

num_of_vector = int(input("Enter 0 for 2D vector or 1 for 3D vector : "))

if num_of_vector == 0:
    v1 = list(map(int, input("Enter vector one coordinates: ").split()))
    v2 = list(map(int, input("Enter vector one coordinates: ").split()))

    print(f"Vector 1 : {v1}")
    print(f"Vector 2 : {v2}")

    plt.quiver(0, 0, v1[0], v1[1], angles = 'xy', scale_units = 'xy', scale = 1, color = "blue", label = "Vector 1")
    plt.quiver(0, 0, v2[0], v2[1], angles = 'xy', scale_units = 'xy', scale = 1, color = "green", label = "Vector 2")

    max_x = max(abs(v1[0]), abs(v2[0]))
    max_y = max(abs(v1[1]), abs(v2[1]))

    padding = 2

    plt.xlim(-(max_x + padding), max_x + padding)
    plt.ylim(-(max_y + padding), max_y + padding)

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    plt.grid(True)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')

    plt.legend()
    plt.show()

elif num_of_vector == 1:

    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection="3d") #Syntax --> fig.add_subplot(rows, columns, index)

    # Changing camera angle
    ax.view_init(elev=25, azim=35)
    '''
    I wrote projections = 3d so that it create a 3d axes
    '''
    v1 = list(map(int, input("Enter the first vector : ").split()))
    v2 = list(map(int, input("Enter the second vector : ").split()))

    ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color="blue", linewidth = 3)
    ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color = "limegreen", linewidth = 3)


    ax.text(v1[0], v1[1], v1[2], f"({v1[0]}, {v1[1]}, {v1[2]})", fontsize=12, color="blue")
    ax.text(v2[0], v2[1], v2[2], f"({v2[0]}, {v2[1]}, {v2[2]})", fontsize=12, color="orange")

    ax.scatter(0, 0, 0, color="black", s=80)
    # Adjusting the graph according to the coordinates
    padding = 2

    x = max(abs(v1[0]), abs(v2[0]))
    y = max(abs(v1[1]), abs(v2[1]))
    z = max(abs(v1[2]), abs(v2[2]))

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_xlim(-(padding+x), padding+x)
    ax.set_ylim(-(padding+y), padding+y)
    ax.set_zlim(-(padding+z), padding+z)
    ax.grid(alpha=0.4)

else:
    print("Enter a valid number")
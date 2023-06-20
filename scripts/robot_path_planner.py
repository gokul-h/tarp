import numpy as np
import random

def robot_path_planner(room_dimensions):
    # Create an empty list for the robot's path
    robot_path = []

    # Get the dimensions of the room
    x_dim, y_dim = room_dimensions

    # Generate a random starting point for the robot
    x_start, y_start = np.random.randint(0, x_dim), np.random.randint(0, y_dim)

    # Append the starting point to the robot's path
    robot_path.append((x_start, y_start))

    # Generate a random direction for the robot to move
    direction = np.random.randint(0, 4)

    # Keep track of the robot's current position
    x_current, y_current = x_start, y_start

    # Loop until the robot has reached the end of the room
    while x_current != x_dim-1 or y_current != y_dim-1:
        # Move the robot in the given direction
        if direction == 0:
            x_current += 1
        elif direction == 1:
            y_current += 1
        elif direction == 2:
            x_current -= 1
        else:
            y_current -= 1

        # Make sure the robot is still within the bounds of the room
        if x_current < 0:
            x_current = 0
        elif x_current > x_dim-1:
            x_current = x_dim-1
        elif y_current < 0:
            y_current = 0
        elif y_current > y_dim-1:
            y_current = y_dim-1

        # Append the new position to the robot's path
        robot_path.append((x_current, y_current))

        # Generate a new random direction for the robot
        direction = np.random.randint(0, 4)

    return robot_path
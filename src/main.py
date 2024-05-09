import math

def calculate_position(initial_position, initial_velocity, acceleration, time):
    # Calculate the position using the formula: position = initial_position + initial_velocity * time + 0.5 * acceleration * time^2
    position = initial_position + initial_velocity * time + 0.5 * acceleration * math.pow(time, 2)
    return position

# Example usage
initial_position = 0
initial_velocity = 10
acceleration = -9.8  # Assuming downward acceleration due to gravity
time = 2

final_position = calculate_position(initial_position, initial_velocity, acceleration, time)
print(f"The final position of the object after {time} seconds is: {final_position}")
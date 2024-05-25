# scripts/deforum_helpers/motion/coordinate_system.py

import numpy as np

class CoordinateSystem:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = {}

    def add_object(self, obj_id, initial_position):
        self.objects[obj_id] = np.array(initial_position)

    def update_position(self, obj_id, new_position):
        if obj_id in self.objects:
            self.objects[obj_id] = np.array(new_position)

    def get_position(self, obj_id):
        return self.objects.get(obj_id, None)

    def interpolate(self, start_pos, end_pos, num_steps, easing_function):
        steps = np.linspace(0, 1, num_steps)
        return [easing_function(step) * (end_pos - start_pos) + start_pos for step in steps]

# Example easing function
def linear_easing(t):
    return t

# Example quadratic easing function
def quadratic_easing(t):
    return t ** 2

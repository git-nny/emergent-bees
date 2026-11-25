import numpy as np

class dot_mother:

    def __init__(self):
        pass
        # random noise TODO 

class dot_type(dot_mother):

    def __init__(self, type_id, time_to_live, max_range):
        super().init()
        self.type_id = type_id
        self.time_to_live = time_to_live
        self.max_range = max_range

    #def interact():

class dot_instance(dot_type):

    def __init__(self, type_id, current_position):
        super().init(type_id)
        self.current_movement = [0, 0] 
        self.current_position = current_position

class create_simulation:
    
    def __init__(self, noise_start=0):
        print('Starting simulation')
        self.dots = None
        #self.noise = noise_start
        self.dot_types = [0, 1, 2, 3]
        # TODO: Bounding Box behaviour


    def add_dot(self, dot_type, pos_x, pos_y, current_movement_x=0, current_movement_y=0):
        """
        Adds dot to simulation
        """
        if dot_type not in self.dot_types:
            raise(ValueError(f"Dot Type {dot_type} is not available in simulation."))
        
        if (pos_x < 0) or (pos_y < 0):
            raise(ValueError("Position cannot be negative"))
            # TODO: This assumes that position extends from (0,0) to (screenheigth, screenwidth.) As god intended.

        new_dot = np.array([
            dot_type, 
            pos_x + self.noise, 
            pos_y + self.noise, 
            current_movement_x, 
            current_movement_y
            ])

        if self.dots is not None:
            self.dots = np.vstack([self.dots, new_dot])
            print(f'dots {self.dots.shape[0]} created')

        else:
            self.dots = new_dot
            print("first dot!")

    def update_dots(self):
        """ updates available dots per step
        """
        pass





# interaction matrix --> später mit Variablen über GUI regelbar
interaction_matrix = np.array(
    [
        [0.5, -0.3, 0.8, 0.0],
        [-0.7, 0.2, 0.0, 0.4], 
        [0.1, 0.6, -0.4, -0.2],
        [0.0, -0.5, 0.7, 0.3]
    ]
)

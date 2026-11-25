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



import numpy as np


class create_simulation:
    def __init__(self):
        self.dots = None
        self.dot_types = [0, 1, 2, 3]

    def add_dot(
        self, dot_type, pos_x, pos_y, current_movement_x=0, current_movement_y=0
    ):
        """
        Adds dot to simulation
        """
        if dot_type not in self.dot_types:
            raise (ValueError(f"Dot Type {dot_type} is not available in simulation."))

        if (pos_x < 0) or (pos_y < 0):
            raise (ValueError("Position cannot be negative"))
            # This assumes that position extends from (0,0) to (screenheigth, screenwidth.) As god intended.

        new_dot = np.array(
            [dot_type, pos_x, pos_y, current_movement_x, current_movement_y]
        )

        if self.dots is not None:
            self.dots = np.vstack([self.dots, new_dot])
            print(f"{self.dots.shape[0]} dots created")

        else:
            self.dots = new_dot

    def wiggle_dots(self, noise_strength=1):
        """updates available dot position per step with the noise strength set in simulation start.
        TODO: check if this looks good in GUI. Change if it looks ugly
        """

        rng = np.random.default_rng()
        noise = rng.normal(0, 1, 2)
        noise_x = int(noise[0] * noise_strength)
        noise_y = int(noise[1] * noise_strength)

        try:
            self.dots[:, 1:3] += np.array([noise_x, noise_y])

        except IndexError:
            self.dots[1:3] += np.array([noise_x, noise_y])

        except TypeError as e:
            print(f"{e}. Are there dots available to wiggle?")

        return self.dots


# interaction matrix --> später mit Variablen über GUI regelbar
interaction_matrix = np.array(
    [
        [0.5, -0.3, 0.8, 0.0],
        [-0.7, 0.2, 0.0, 0.4],
        [0.1, 0.6, -0.4, -0.2],
        [0.0, -0.5, 0.7, 0.3],
    ]
)

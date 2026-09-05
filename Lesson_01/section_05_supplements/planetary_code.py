

class Planet:

    def __init__(self, name, x_coord, y_coord, z_coord):
        self.name = name
        self.x = x_coord
        self.y = y_coord
        self.z = z_coord

    def __str__(self):
        return (
            f"planet '{self.name}'"
            f" at position ({self.x}, {self.y}, {self.z})"
        )

    def __repr__(self):
        return (
            f"Planet(name='{self.name}', "
            f"x_coord={self.x}, "
            f"y_coord={self.y}, "
            f"z_coord={self.z})"
        )

    def __lt__(self, other):
        # You need to type check and raise an error is there's an
        # incompatibility. We'll go over errors properly next lesson
        if not isinstance(other, type(self)):
            raise TypeError(
                "unsupported operand type(s) for <: "
                f"'Planet' and '{type(other)}'"
            )
        own_distance_to_origin_squared = (
            self.x ** 2
            + self.y ** 2
            + self.z ** 2
        )
        other_distance_to_origin_squared = (
            other.x ** 2
            + other.y ** 2
            + other.z ** 2
        )

        return (
            own_distance_to_origin_squared < other_distance_to_origin_squared
        )

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        own_position = (self.x, self.y, self.z)
        other_position = (other.x, other.y, other.z)
        return own_position == other_position

    def __hash__(self):
        own_position = (self.x, self.y, self.z)
        return hash(own_position)


if __name__ == "__main__":
    earth = Planet('Earth', 17394, 3728943, -3272672)
    also_earth = Planet(
        name='Earth',
        x_coord=17394,
        y_coord=3728943,
        z_coord=-3272672
    )
    venus = Planet('Venus', 73849050, 3487506026, -428649932)
    le_earth = Planet('Le Earth', 17394, 3728943, -3272672)
    not_a_planet = "I'm not a planet!"

    # Here's some of the examples run but just mess around with it for
    # your  own benefit. Maybe even try adding one of the other
    # comparative dunder methods
    print(f"{str(earth)=}")
    print(f"{repr(earth)=}")
    print(f"{repr(also_earth)=}")
    print(f"{earth < venus=}")
    print(f"{earth < not_a_planet=}")

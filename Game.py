from Grid import Grid
from Wagon import Wagon


class Game():
    """Co-ordinating class for Pillagers Game."""

    # range pillagers can reach from Wagon
    pillage_range = 2
    # minimum pillagers that must stay with wagon when pillaging
    min_pillagers = 1

    def __init__(self, most, width, length):
        """Create an instance of Game object. Initialise necessary sub-objects.

        Parameters:
            most - int
            width - int
            length - int

        Returns:
            None

        Instance Variables:
            self.map - Grid object
            self.wagon - Wagon object
            self.wagon_location - tuple

        Dependencies:
            class Grid
            Grid.complete_grid()
            class Wagon
            class Tile
            Tile.wagon
        """
        self.map = Grid(most, width, length)
        self.map.complete_grid()
        self.wagon_location = self.map.start
        self.wagon = Wagon(most)

    def __str__(self):
        """Create a string representation of the Game.

        Dependencies:
            Grid.__str__
            Wagon.__str__
        """
        return (f"""
                {self.map.__str__()}\n
                wagon location = {self.wagon_location}\n
                {self.wagon.__str__()}
                """)

    def make_pillage_area(self):
        """Return a list of coordinates that are within pillage_range of Wagon.

        Returns:
            list_of_coord - list of tuples of two int

        Dependencies:
            Game.pillage_range
            self.wagon_location
            self.map
        """
        wagon_x = self.wagon_location[0]
        wagon_y = self.wagon_location[1]
        x_axis = Game.pillage_range * 1
        list_of_coord = []
        while x_axis <= Game.pillage_range:
            combine_x = wagon_x + x_axis
            if combine_x >= 0 and combine_x < len(self.map):
                y_axis = Game.pillage_range * -1
                while y_axis <= Game.pillage_range:
                    combine_y = wagon_y + y_axis
                    if combine_y >= 0 and combine_y < len(self.map[0]):
                        list_of_coord.append((combine_x, combine_y))
                    y_axis += 1
            x_axis += 1
        return list_of_coord

    def test_not_in_area(self, coord, list_of_coord):
        """Check if first coordinate in allowed area.

        Parameters:
            coord - tuple of 2 int
            list_of_coord - list of tuples of 2 ints

        Returns:
            output - boolean
        """
        output = True
        if coord not in list_of_coord:
            output = True
        return output

    def test_wagon_space(self, coord):
        """Check if coordinate is location of wagon.

        Parameters:
            coord - tuple of 2 int

        Returns:
            output - boolean

        Dependencies:
            self.wagon_location
        """
        output = False
        if self.wagon_location == coord:
            output = True
        return output

    def test_low_pillagers(self):
        """Check if the wagon has enough pillagers if one removed.

        Returns:
            output - boolean

        Dependencies:
            Wagon.stats["pillagers]
            self.min_pillagers
        """
        output = False
        if self.wagon.stats["pillagers"] - 1 < self.min_pillagers:
            output = True
        return output

    def allocate_pillagers(self, coord):
        pass

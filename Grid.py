from Tile import Tile
from Village import Village
from Town import Town
from random import randrange


class Grid():
    """Class for making a grid of Tile objects

    Instance Variables:
        most - int - caps values in nested Tile objects
        village_coord - list of tuples - stores locations of villages
        grid - list of lists of Tile Objects - main focus of class
        town_coord - list of tuples - stores location of towns

    Functions:
        __init__(most, width, length) - builders function
        __str__() - make string representation of self.grid
        make_grid(width, length) - make self.grid
        make_start() - set one Tile location start value to True
        rand_village() - determines the likelyhood of Tile becoming village
        check_coord() - checks if Tile is in proximity to village
        check_town() - checks if village should be town.
        check_town_coord() - check if coord is in proximity to a town
        make_town() - assign towns to locations based on self.town_coord

    Dependencies:
        Tile
        Village
        Town
        randrange from Random
    """

    def __init__(self, most, width, length):
        """Constructor Function for Grid class.

        Parameters:
            most - int - maximum values of nested Tiles
            width - int - length of nested lists in self.grid
            length - int - number of nested lists in self.grid

        Instance Variables:
            most - int - caps values in nested Tile objects
            village_coord - list of tuples - stores locations of villages
            grid - list of lists of Tile Objects - main focus of class
            town_coord - list of tuples - stores location of towns

        Dependencies:
            self.make_grid()
            self.make_start()
            self.check_town()
            self.make_town()
        """
        self.most = most
        self.village_coord = [tuple(length // 2, 0)]
        self.grid = self.make_grid(width, length)
        self.make_start()
        self.town_coord = self.check_town()
        self.make_towns()

    def __str__(self):
        """Return a string representation of self.grid.

        Return:
            output - str

        for each nested list start a new line
        for each Tile object use T, V, or F if town, village or neither
        """
        output = ""
        for lst in self.grid:
            output += "\n"
            for space in lst:
                if isinstance(space, Town):
                    output += "T "
                elif isinstance(space, Village):
                    output += "V "
                else:
                    output += "F "
        return output

    def make_grid(self, width, length):
        """Return a list of list of Tile objects.

        Place of Villages determined by check_coord and rand_village.

        Parameters:
            length - int - number of nested lists
            width - int - length of nested lists

        Dependencies:
            self.rand_village()
            self.check_coord()
            self.village_coord()
            Tile
            Village
        """
        output = []
        len_count = 0
        width_count = 0
        while len_count < length:
            sub_list = []
            while width_count < width:
                add_village = False
                if self.check_coord(len_count, width_count):
                    if self.rand_village():
                        add_village = True
                if add_village:
                    sub_list.append(Village(self.most))
                    self.village_coord.append(tuple(len_count, width_count))
                else:
                    sub_list.append(Tile(self.most))
                width_count += 1
            output.append(sub_list)
            len_count += 1
        return output

    def make_start(self):
        """Make Tile object start variable equal True.

        start at index 0 of middle nested list

        Dependencies:
            self.grid
            Tile
        """
        length = len(self.grid)
        half = length // 2
        self.grid[half][0].start = True

    def rand_village(self):
        """Return True 1/3 of times called. Else False.

        Chance of returning True determined by randrange

        Returns:
            output - boolean

        Dependencies:
            randrange
        """
        limit = 4
        roll_die = randrange(1, limit)
        output = False
        if roll_die == limit-1:
            output = True
        return output

    def check_coord(self, length, width):
        """Return True if no tuple in self.village_coord within range

        Parameters:
            length - int - which nested list
            width - int - index of nested list

        Returns:
            output - boolean

        Dependencies:
            self.village_coord
        """
        output = True
        range = 2
        for tup in self.village_coord:
            if length > (tup[0] - range) and length < (tup[0] + range):
                if width > (tup[1] - range) and width < (tup[1] + range):
                    output = False
                    break
        return output

    def check_town(self):
        """Determine if Village should be Town and returns a list of tuples.

        Return:
            town_coord - list of tuples - coordinates to be made into town obj

        Dependencies:
            self.village_coord
            self.check_town_coord()
        """
        town_coord = []
        range = 3
        req_villages = 4
        for vil in self.village_coord[1:]:
            count = 0
            for tup in self.village_coord[1:]:
                if (vil[0] - range) < tup[0] and (vil[0] + range) > tup[0]:
                    if (vil[1] - range) < tup[1] and (vil[1] + range) > tup[1]:
                        count += 1
            if count > req_villages:
                if self.check_town_coord(vil[0], vil[1]):
                    town_coord.append(vil)
        return town_coord

    def check_town_coord(self, length, width):
        """Check if input coordinates in range of existing towns.

        Parameters:
            length - int - which nested list
            width - int - index within nested list

        Returns:
            add_town - boolean

        Dependencies:
            self.town_coord
        """
        add_town = True
        range = 3
        for coord in self.town_coord:
            if (length - range) < coord[0] and (length + range) > coord[0]:
                if (width - range) < coord[1] and (width + range) > coord[1]:
                    add_town = False
                    break
        return add_town

    def make_towns(self, town_coord):
        """Apply town objects to coordinates given as argument.

        Parameters:
            town_coord - list of tuples of int - collection of coordinates

        Dependencies:
            self.grid
            self.town_coord
            Town
        """
        for coord in town_coord:
            self.grid[coord[0]][coord[1]] = Town(self.most)

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
        start - tuple - location of tile where start is True

    Functions:
        __init__(most, width, length) - builders function
        __str__() - make string representation of self.grid
        make_grid(width, length) - make self.grid
        make_start() - set one Tile location start value to True
        rand_village() - determines the likelyhood of Tile becoming village
        check_vill_coord() - checks if Tile is in proximity to village
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
            length - int - number of nested lists in grid
            width - int - length of nested lists in grid
        """
        self.most = most
        half = length // 2
        self.start = (half, 0)
        self.village_coord = [self.start]
        self.grid = []
        self.town_coord = []
        self.length = length
        self.width = width

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
        """Return a list of nested lists containing tile objects

        The length of the parent list is length.
        The length of the nested list is width.

        Parameters:
            length - int - number of nested lists
            width - int - length of nested lists

        Dependencies:
            Tile
        """
        output = []
        len_count = 0
        while len_count < length:
            sub_list = []
            width_count = 0
            while width_count < width:
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
        start_location = self.grid[self.start[0]][self.start[1]]
        start_location.start = True

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

    def check_vill_coord(self, length, width):
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

        Dependencies:
            self.village_coord
            self.check_town_coord()
        """
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
                    self.town_coord.append(vil)

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

    def make_villages(self):
        """Replace objects in self.grid with village objects.

        Replace objects based on self.check_vill_coord and self.rand_village

        Dependencies:
            self.check_vill_coord()
            self.rand_village()
            self.grid
            self.village_coord
        """
        len_count = 0
        for sublist in self.grid:
            wid_count = 0
            for space in sublist:
                if self.rand_village():
                    if self.check_vill_coord(len_count, wid_count):
                        self.grid[len_count][wid_count] = Village(self.most)
                        self.village_coord.append((len_count, wid_count))
                wid_count += 1
            len_count += 1

    def complete_grid(self):
        """Coordinator function for Grid class

        Will repeat until at least one town made or 100 attempts.

        Returns:
            bool - True if map with town created

        Dependencies:
            self.village_coord
            self.town_coord
            self.make_towns()
            self.check_town()
            self.make_start()
            self.make_grid()
            seld.make_villages
        """
        any_towns = False
        count = 0
        while not any_towns and count < 100:
            self.grid = self.make_grid(self.width, self.length)
            self.make_start()
            self.make_villages()
            self.check_town()
            any_towns = len(self.town_coord)
            if not any_towns:
                self.village_coord = [(self.start)]
            count += 1
        return (bool(any_towns))

import random


class Tile():

    """Represents each square in a map grip.

    Class Variable:
        pillage_value = dictionary - str: int

    Instance Variables:
        pillagers = int
        defenders = int
        desolate = boolean
        abandoned = boolean
        start = boolean
        most = int

        Functions
        __init__()
        __str__()
        -change_pillagers()
        -change_defenders()
        -abandon()
        -pillage()
        -check_defence()
        -check_abandon()
        -roll_die()
        -complete_turn()
    """
    pillage_value = {"rations": 1, "fear": 1}

    def __init__(self, most):
        """Constructor for Tile Object. Takes int parameter max."""
        self.pillagers = 0
        self.defenders = 0
        self.desolated = False
        self.abandoned = False
        self.start = False
        self.most = most

    def __str__(self):
        """Returns value of instance variables"""
        return (f"""
                pillage_value = {Tile.pillage_value},
                defenders = {self.defenders},
                pillagers = {self.pillagers},
                desolated = {self.desolated},
                abandoned = {self.abandoned},
                start tile = {self.start}""")

    def change_pillagers(self, amount):
        """Change self.pillagers by int param amount.

        Parameters:
            amount - int

        Returns:
            boolean

        Side Effects:
            change self.pillagers
        """
        output = True
        if self.pillagers + amount < 0:
            output = False
            self.pillagers = 0
        elif self.pillagers + amount > self.most:
            output = False
            self.pillagers = self.most
        else:
            self.pillagers += amount
        return output

    def change_defenders(self, amount):
        """Change self.defenders by int param amount.

        Parameters:
            amount - int

        Returns:
            boolean

        Side Effects:
            change self.defenders
        """
        output = True
        if self.defenders + amount < 0:
            output = False
            self.defenders = 0
        elif self.defenders + amount > self.most:
            output = False
            self.defenders = self.most
        else:
            self.defenders += amount
        return output

    def abandon(self):
        """Change state of self.abandoned or self.desolated.

        Returns: none

        Side effects:
            self.desolated
            self.abandoned
        """
        if self.abandoned or self.desolated:
            self.desolated = True
            self.abandoned = False
        else:
            self.abandoned = True

    def pillage(self):
        """Return value of self.pillage_value if requirements met.

        Dependencies:
        self.pillage_value
        self.desolated
        self.abandoned
        self.roll_die()

        Returns:
        self.pillage_value unless:
            pillagers less than 1
            desolated is True
            abandoned is True half of the time
        in which case empty dictionary
        """
        output = self.pillage_value
        if self.pillagers < 1:
            output = {}
        elif self.desolated:
            output = {}
        elif self.abandoned:
            rnd_num = self.roll_die()
            if rnd_num < self.most/2:
                output = {}
        return output

    def roll_die(self):
        """Return random number between 1 and self.max.

        Dependencies:
            random.randrange()
            self.max
        """
        return (random.randrange(1, self.most))

    def check_defence(self):
        """Change self.defenders and self.pillagers based on die roll.

        Returns:
            None

        Dependencies:
            self.roll_die()
            self.change_defenders()
            self.change_pillagers()

        Side Effects:
            self.defenders
            self.pillagers
        """
        rnd_num = self.roll_die()
        subtotal = self.defenders + rnd_num
        surplus = subtotal - self.most
        if surplus > 0:
            self.change_defenders(-surplus)
            casualties = surplus - (self.pillagers - 1)
            if casualties > 0:
                self.change_pillagers(-casualties)

    def check_abandon(self, fear):
        """Change self.abandoned or self.desolated based on die roll.

        Parameters:
            fear - int

        Returns:
            None

        Dependencies:
            self.abandon()
            self.roll_die

        Side Effects:
            self.abandoned
            self.desolated
        """
        rnd_num = self.roll_die()
        if fear + rnd_num < 1:
            self.abandon()

    def complete_turn(self, fear):
        """Modify state of Tile.

        Parameters:
            fear - int

        Returns:
            Dictionary - str: int

        Dependencies:
            self.check_defence()
            self.pillage()
            self.check_abandon()
            self.change_pillagers()"""
        self.check_defence()
        output = self.pillage()
        self.check_abandon(fear)
        output["pillagers"] = self.pillagers
        self.change_pillagers(-self.pillagers)
        return output

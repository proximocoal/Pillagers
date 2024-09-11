from Tile import Tile


class Village(Tile):
    """Extend Tile to include trade option and value

    Class Variables:
        pillage_value - dict - str:int
        trade_value - dict - str:int

    Instance Variables:
        as super()

    Functions:
        as super()
        check_trade() - return trade_value or pillage_value or empty dict
        __init__(most) - overwritten to include self.trade - boolean
        __str__() - overwritten to include self.trade and self.trade_value
        complete_turn(fear)- overwritten to call check_trade() or pillage()

    Dependencies:
        as Super
        Tile
    """

    pillage_value = {"food": 1, "gold": 1, "hate": 1}
    trade_value = {"food": 1, "gold": -1, "fear": -1}

    def __init__(self, most):
        """Constructor for Village Class.

        Parameters:
            most - int

        Instance Variables:
            as Super()
            self.trade - boolean
        """
        super().__init__(most)
        self.trade = False

    def __str__(self):
        """Return string representation of instance variables."""
        output = super().__str__()
        output += f""",
                trade = {self.trade},
                trade_value = {self.trade_value}"""
        return output

    def check_trade(self):
        """Return self.trade_value if conditions met, else empty dict.

        Returns:
            output - dict - str:int

        Dependencies:
            self.pillagers
            self.desolated
            self.abandoned
            self.trade_value
        """
        output = {}
        if self.pillagers > 0 and not self.desolated and not self.abandoned:
            output = self.trade_value
        return output

    def complete_turn(self, fear):
        """Coordinating funct. Modify state of Tile and return stat modifiers.

        Parameters:
            fear - int

        Returns:
            Dictionary - str: int

        Dependencies:
            self.trade
            self.check_defence()
            self.check_trade()
            self.pillage()
            self.check_abandon()
            self.change_pillagers()
        """
        self.check_defence()
        output = {}
        if self.trade:
            output = self.check_trade()
        else:
            output = self.pillage()
        self.check_abandon(fear)
        output["pillagers"] = self.pillagers
        self.change_pillagers(-self.pillagers)
        self.trade = False
        return output

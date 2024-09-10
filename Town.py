from Village import Village


class Town(Village):
    """Extend Village Class to change class variables and min on self.defenders

    Class Variables:
        pillage_value - dict - str:int
        trade_value - dict - str:int

    Instance Variables:
        as super()

    Functions:
        as super()
        __init__() - overwritten to initialise self.defenders to 1
        change_defenders() - overwritten to make min self.defenders 1
    """

    pillage_value = {"food": 2, "gold": 2, "hate": 2}
    trade_value = {"food": 2, "gold": -1, "fear": -1}

    def __init__(self, most):
        """Constructor for Town Class.

        Parameters:
            most - int

        Instance Variables:
            as super()
        """
        super().__init__(most)
        self.defenders = 1

    def change_defenders(self, amount):
        """Change self.defenders by amount within boundaries.

        boundaries set by self.most and 1

        Parameters:
            amount - int

        Returns:
            None"""
        super().change_defenders(amount)
        if self.defenders < 1:
            self.defenders = 1

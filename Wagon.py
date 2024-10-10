class Wagon:
    """Primary administration object of a game

    Class Variables:
        stat_keys = List of strings - used to popular instance v. stats

    Instance Variables:
        stats - dict - key strings, value int
        most = int

    Instance Methods:
        __init__ - make instance of Wagon
        __str__ - represent Wagon instance in string form
        change_stat - modify instance variable self.stats
        check_loss - check if pillagers or rations are 0
    """

    stat_keys = ["fear", "hate", "gold", "rations", "pillagers"]

    def __init__(self, most):
        """Constructor for class Wagon objects.

        Parameters:
            most = int

        Instance Variables:
            stats - dict - keys taken from class v. stat_keys
            most = int
        """
        self.stats = {}
        for stat in Wagon.stat_keys:
            self.stats[stat] = 0
        self.most = most

    def __str__(self):
        """Represent object in string form."""
        return f"{self.stats}, max = {self.most}"

    def change_stat(self, stat, amount):
        """modify matching value in self.stats by given amount.

        Parameters:
        stat must be in self.stats else KeyError
        amount int else ValueError

        Returns:
        int - new amount of relevant stat

        Dependencies:
        self.stats
        self.most
        KeyError
        ValueError
         '"""
        output = 0
        if not isinstance(amount, int):
            raise ValueError
        elif stat not in self.stats:
            raise KeyError
        else:
            og_amount = self.stats[stat]
            if og_amount + amount < 0:
                output = 0
            elif og_amount + amount > self.most:
                output = self.most
            else:
                output = og_amount + amount
        self.stats[stat] = output
        return output

    def check_loss(self):
        """Check if rations or pillagers are 0. True if so."""
        output = False
        if self.stats["rations"] == 0:
            output = True
        elif self.stats["pillagers"] == 0:
            output = True
        return output

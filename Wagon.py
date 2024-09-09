class Wagon:
    """Primary administration object of a game

    Instance Variables:
        max = int
        fear = int
        hate = int
        gold = int
        rations = int
        location = Tuple
        pillagers = int
    """

    def __init__(self, max):
        """Constructor for class Wagon objects.

        Parameters:
            max = int

        Instance Variables:
            fear = int
            hate = int
            gold = int
            rations = int
            location = tuple
            pillagers = int
            max = int
        """
        self.fear = 0
        self.hate = 0
        self.gold = 0
        self.rations = 0
        self.location = (0, 0)
        self.pillagers = 0
        self.max = max

    def __str__(self):
        return f"""fear = {self.fear},
                   hate = {self.hate},
                   gold = {self.gold},
                   rations = {self.rations},
                   location = {self.location}
                   pillagers = {self.pillagers}
                   """

    def change_stat(self, stat, amount):
        """Set method for external objects.

        Parameters:
        stat - must be 'fear', 'hate', 'gold', 'rations' or 'location
        else ValueError
        amount - int or tuple of ints for location
        else TypeError

        Returns:
        Boolean - of successful instance variable change made

        Dependencies:
        self.change_gold
        self.change_rations
        self.change_location
        self.change_raiders
        self.change_hate
        self.change_fear
        ValueError
        self.max
         '"""
        output = False
        if stat == "fear":
            output = self.change_fear(amount)
        elif stat == "hate":
            output = self.change_hate(amount)
        elif stat == "gold":
            output = self.change_gold(amount)
        elif stat == "rations":
            output = self.change_rations(amount)
        elif stat == "location":
            output = self.change_location(amount)
        elif stat == "pillagers":
            output = self.change_pillagers(amount)
        else:
            raise ValueError("""Stat not recognised. Must be:
                fear,
                hate,
                gold,
                rations,
                pillagers
                or location""")
        return output

    def change_fear(self, amount):
        """Modify fear instance variable.

        Parameters:
        amount - int
        else TypeError

        Returns:
        boolean - if successfull modification made

        Dependencies:
        self.max
        """
        output = False
        if self.fear + amount < 0:
            self.fear = 0
        elif self.fear + amount > self.max:
            self.fear = self.max
            output = True
        else:
            self.fear += amount
            output = True
        return output

    def change_hate(self, amount):
        """Modify hate instance variable.

        Parameters:
        amount - int
        else TypeError

        Returns:
        boolean - if successfull modification made

        Dependencies:
        self.max
        """
        output = False
        if self.hate + amount < 0:
            self.hate = 0
        elif self.hate + amount > self.max:
            self.hate = self.max
            output = True
        else:
            self.hate += amount
            output = True
        return output

    def change_gold(self, amount):
        """Modify gold instance variable.

        Parameters:
        amount - int
        else TypeError

        Returns:
        boolean - if successfull modification made

        Dependencies:
        self.max
        """
        output = False
        if self.gold + amount < 0:
            self.gold = 0
        elif self.gold + amount > self.max:
            self.gold = self.max
            output = True
        else:
            self.gold += amount
            output = True
        return output

    def change_rations(self, amount):
        """Modify rations instance variable.

        Parameters:
        amount - int
        else TypeError

        Returns:
        boolean - if successfull modification made

        Dependencies:
        self.max
        """
        output = False
        if self.rations + amount < 0:
            self.rations = 0
        elif self.rations + amount > self.max:
            self.rations = self.max
            output = True
        else:
            self.rations += amount
            output = True
        return output

    def change_location(self, amount):
        """Modify location instance variable.

        Parameters:
        amount - Tuple
        else TypeError

        Returns:
        boolean - if successfull modification made

        Dependencies:
        self.max
        """
        pass

    def change_pillagers(self, amount):
        """Modify raiders instance variable.

        Parameters:
        amount - int
        else TypeError

        Returns:
        boolean - if successfull modification made

        Dependencies:
        self.max
        """
        output = False
        if self.pillagers + amount < 0:
            self.pillagers = 0
        elif self.pillagers + amount > self.max:
            self.pillagers = self.max
            output = True
        else:
            self.pillagers += amount
            output = True
        return output

    def check_loss(self):
        """Check if rations or pillagers are 0. True if so."""
        output = False
        if self.rations == 0:
            output = True
        elif self.pillagers == 0:
            output = True
        return output

Change Log

1. a)Change all instances of raiders to pillagers (each stat has different    starting letter)
   b)test_change_pillagers() written in TestWagon
   c)Added max variable to control largest stat size and replaced all previous max values with it
   d)Added Class Overview, Extant Questions and Rules txt files
   e)Added check_loss() to Wagon and relevant unit tests to TestWagon
   f)Changed <= to less than in change functions in Wagon (don't return False unless total less than 0)

2. a)Added Tile Class
   b)Change Wagon to have max as instance variable not Class Variable.
   c)Updated Docstring and Test Wagon to match b)
   d)Answered rng and subclass question in Extant questions
   e)Added where should Wagon location be stored in Extant Questions
   f)Changed Rules.txt to make move wagon first
   g)Changed Rules.txt so defence based on defenders not hate and lose defenders regardless of pillagers
   h)Changed Rules.txt so loss based on rations and pillagers not gold
   i)Deviate from class outline to make rnd_num local variable rather than instance variable (diff to board game)

3. a) Added TestTile Class
   b) Change all instances of max to most
   c) change_pillagers result if total greater than most to most not 0
   d) Make md versions of all txt files and delete txt files
   e) change point of abandon to 0 not -1 in Tile
   f) rewrite Tile.abandon
   g) add missed () from roll_die on line 135 of Tile
   h) make subfolder info and moved all md and license file to there

4. a) Updated Rules to replace max with most
   b) Updated Tile.complete_turn() docstring to say returns stat modifiers
   c) Changed Rules to lose fear not hate and costs only 1 gold to trade with Town
   d) Make Village class extending Tile
   e) Make Town class extending Village
   f) Change __str__ of tile to return self.pillage_value rather than Tile.pillage_value (for child class purposes)
   g) Make TestVillage class
   h) Make TestTown class
   i) change TestTile line 85 to refer to defenders not pillagers

5. a) Village.complete_turn now also sets self.trade to false. Updated unit tests to reflect this
   b) Change docstring of Tile __init__ to say most and not max
   c) Change roll_die so range top end is most + 1 as randrange is not inclusive
   d) Change Tile to only import randrange and not all of random
   e) Change TestWagon to use assertTrue and assertEqual rather than assert ... == for consistency
   f) Make Grid Class
   h) Make TestGrid Class stub

6. a) change setUp in TestGrid to use class variables most, length and width as arguments
   b) change set_up and tear_down to setUp and tearDown in TestGrid
   c) remove tuple keyword from line 111 and 56 in Grid
   d) signficant refactoring of Grid Class
      1. __init__ rewritten to initialise empty objects
      2. added start, length and width instance variables
      3. make_grid() now only fills the grid with tile objects
      4. move width_count local variable to within length_count loop
      5. make_start() now uses self.start instance variable
      6. change check_coord name to check_vill_coord
      7. check_town directly modifies self.town_coord
      8. added make_villages() function
      9. added complete_grid() function
   e) Complete TestGrid Class

7. a) merged all instance variable apart from most in Wagon into a dictionary
   b) remove location as a stat
   c) merged all change stat methods into a single method in Wagon
   d) make class variable stat_keys in wagon to control contents of instance variable self.stats
   e) update unit tests to match update in Wagon

Wagon - store stats
tile - store stats
map - store tile
session - co-ordinator
UI - outside scope

Wagon

Instance Variables
-fear int
-hate int
-gold int
-rations int
-pillagers int
-location Tuple

Class Variables
-max int

Functions
-check loss
-change stats

Tile

Instance Variables
-type string
-pillagers int
-defenders int
-desolate boolean
-abandoned Boolean
-start Boolean
-pillage tile
-trade tile

Class Variables
-available types list

Functions
-change stats
-check defence
-check abandonment

Map
Instance Variables
-map list of lists of tiles
Functions
-generate mini map
-update tile
-check village
-check town

Session
Instance Variables
-map -list of lists of tiles
-map width
-map length
-mini map
Functions
-generate map
-generate minimap
-generate wagon
-start game (init?)
-allocate pillagers
-generate events
-move wagon
-check loss
-check end
-return pillagers
-check defence
-muster defenders
-place muster
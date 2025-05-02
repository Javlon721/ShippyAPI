from existing_ships import get_ship_by_name
from ship import Ship


ship_1 = get_ship_by_name("Belfast")
ship_2 = get_ship_by_name("Hood")
# print(ship_1 )
Ship.print_ships([ship_1, ship_2])
ship_3 = get_ship_by_name("Hoo2d")



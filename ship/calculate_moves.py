def calculate_moves(ship1, ship2, ships_direction):
    max_distance_between_ships = max(ship1.attack_range, ship2.attack_range)
    match ships_direction:
        case '0':
            while ship2.pos - ship1.pos > 0 or ship1.pos - ship2.pos <= max_distance_between_ships:
                ship1.change_pos()
                ship2.change_pos(-1)
        case '1':
            while ship2.pos - ship1.pos <= max_distance_between_ships:
                ship1.change_pos(-1)
                ship2.change_pos()
        case '2':
            can_ship1_chase = ship1.velocity > ship2.velocity or ship2.pos - \
                ship1.pos <= max_distance_between_ships
            if can_ship1_chase:
                while abs(ship1.pos - ship2.pos) <= max_distance_between_ships or (ship1.pos < ship2.pos and ship1.velocity > ship2.velocity):
                    ship1.change_pos()
                    ship2.change_pos()
        case '3':
            can_ship2_chase = ship2.velocity > ship1.velocity or abs(
                ship2.pos - ship1.pos) <= max_distance_between_ships
            if can_ship2_chase:
                while (ship2.pos > ship1.pos and ship2.velocity > ship1.velocity) or abs(ship2.pos - ship1.pos) <= max_distance_between_ships:
                    ship1.change_pos(-1)
                    ship2.change_pos(-1)



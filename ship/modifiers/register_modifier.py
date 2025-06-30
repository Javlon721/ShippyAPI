def register_modifier(a_register):
    def wrapper(modifier):
        a_register['items'].append(modifier)
        return modifier

    return wrapper

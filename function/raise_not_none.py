def some_body(some_condition: str):
    if some_condition:
        raise ValueError  # Do not just return None here, since this is a dangling value when using if else
    else:
        return some_condition[2:]
    

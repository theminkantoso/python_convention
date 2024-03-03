# Don't do this
sample_dict = {"one": "one", "two": "two"}
do_not_do_this = sample_dict.get("one", '')[0] or '0'  # Get the first element of the given key

def get_first_character_or_assign_default_value(input_dict: dict, key: str, default: str = '0'):
    value = input_dict.get(key, '')
    if value:
        return value[0]
    else:
        return default
    
do_this = get_first_character_or_assign_default_value(input_dict=sample_dict, key="one", default='0')
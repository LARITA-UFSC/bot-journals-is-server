def trim_all(text):
    return text.strip()

def replace_new_line(text):
    return text.replace('\r', '').replace('\n', '').replace('\t', '')

def parenthesis_to_bracket(text):
    return '[' + text[1:-1] + ']'

def to_list(text):
    import json
    return json.loads(text)

def get_value_list(value, index):
    return (value or [None])[index]
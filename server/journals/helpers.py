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


class Colors:
    GREEN='\033[1;32m'
    RED='\033[1;31m'
    YELLOW='\033[1;33m'
    WHITE='\033[1;37m'
    NO_COLOUR='\033[0m'
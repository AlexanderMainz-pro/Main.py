calls = 0

def count_calls(string_info, is_contains):
    global calls
    calls += 1


def string_info(string):
    global calls
    len(string)
    string.lower()
    string.upper()
    print(calls)
    return print(len(string), string.lower(), string.upper()), calls + 1


def is_contains(string, list_to_search):
    print(calls)
    if string in list_to_search:
        return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('urban', ['ban', 'BaNaN', 'urban'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

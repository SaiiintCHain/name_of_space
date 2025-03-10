calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return ((len(string), string.upper(), string.lower()))

def is_contains(string, list_to_search):
    count_calls()
    string1 = string.upper()
    list_to_search1 = [item.upper() for item in list_to_search]
    if string1 in list_to_search1:
        return(True)
    else:
        return(False)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
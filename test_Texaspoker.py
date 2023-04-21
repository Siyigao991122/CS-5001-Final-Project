from Texaspoker import start, continue_game, rules, run, menu
fail = 0
def test_continue_game():
    pair = [['1','2','3'],['A','B','C'],['!','*']]
    try:
        continue_game(pair) == [['!','*','1','2','3'],['!','*','A','B','C']]
        print(continue_game(pair))
    except:
        fail += 1
        print('continue game failed')

def test_start():
    try:
        len(start(['A','B','C'],['1','2','4'])) == 3
    except:
        fail += 1
        print('start function failed')

def test_menu():
    try:
        menu('Test') == 'test'
    except:
        fail += 1
        print('menu() function failed')

def test_rules():
    try:
        rules(['A','B'],['B','C'],5,6)
    except:
        fail += 1
        print('rules() function failed')

print(f'function failed {fail}')

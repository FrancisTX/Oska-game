from movegen.py import *

def test(los, turn):
    print(movegen(los, turn))
    
test(['wwww', '---', '--', '---', 'bbbb'], 'w')
test(['wwww', '---', '--', '---', 'bbbb'], 'b')
test(['wwww', '---', '--', 'b--', 'b---'], 'b')
test(['wwww', '---', '--', '--b', '---b'], 'b')
test(['wwww', '---', '--', '--w', '---b'], 'b')
test(['wwww', '---', '--', 'w--', 'b---'], 'b')
test(['wwww', '---', '--', 'w--', '-b--'], 'b')
test(['wwww', '---', 'w-', 'w--', 'b---'], 'b')
test(['wwww', '---', 'b-', 'w--', 'b---'], 'b')
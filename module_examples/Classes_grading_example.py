import numpy as np
import pandas as pd

class Team:
  def __init__(self, name, angle=90, twist=False, c=12.65, a=3.75, b=3.75,
               ratio=3.75, square=True, Al1='y', Sr_c='y', Sr_t='y',
               O1='y', O2='y', occ1='y', occ2='y', complete_color='y',
               sturdy='y', ugly='y', squat='y', poly_qual='y',
               poly_tb='y', score=100):
    self.name = name

teams={}

team_names_full = ['maverick', 'goose','iceman','viper','hollywood','cougar','jester','rooster','hangman','phoenix','payback','fanboy','bob','chipper','charlie','merlin','slider','flounder','Baby Yoda','stinger']
team_names = ['Baby Yoda', 'goose']

for x in team_names:
    p = Team(x)
    p.score = 100
    print(f'Team: {p.name}')
    p.angle = input('angle? perfect, ok, or bad (p,o,b):')
    if p.angle == 'o':
        p.score -= 2
    elif p.angle == 'b':
        p.score -= 4
    p.twist = input('twist? perfect, ok, or bad (p,o,b):')
    if p.twist == 'o':
        p.score -= 2
    elif p.twist == 'b':
        p.score -= 4
    p.a = float(input('a?:'))
    p.b = float(input('b?:'))
    p.c = float(input('c?:'))
    if abs(p.a-p.b)/p.a > 0.2:
        p.square = False
        p.score -= 3
    elif (abs(p.a-p.b)/p.a > 0.1) and abs(p.a-p.b)/p.a<0.2:
        p.square =False
        p.score -= 2
    p.ratio = p.c/((p.a+p.b)/2)
    if (p.ratio-3.75)/3.75 > 0.25:
        p.score -= 7
    elif ((p.ratio-3.75)/3.75 < 0.25) and ((p.ratio-3.75)/3.75 > 0.15):
        p.score -= 5
    elif ((p.ratio-3.75)/3.75 < 0.15) and ((p.ratio-3.75)/3.75 > 0.05):
        p.score -= 2
    p.Al = input('Al on corner? y/n:')
    if p.Al == 'n':
        p.score -= 5
    p.Sr_c = input('Sr center square? perfect, ok, bad (p,o,b):')
    if p.Sr_c == 'b':
        p.score -= 2
    if p.Sr_c == 'b':
        p.score -= 1
    p.Sr_t = input('Sr top/bot staggered? y/n:')
    if p.Sr_t == 'n':
        p.score -= 1
    p.O1 = input('O1 centered? y/n:')
    if p.O1 == 'n':
        p.score -= 3
    p.O2 = input('O2 closer to Al? y/n:')
    if p.O2 == 'n':
        p.score -= 2
    p.occ1 = input('Occupancy of Al, O 100%? y/n:')
    if p.occ1 == 'n':
        p.score -= 3
    p.occ2 = input('50% occ of Sr/La? y/n:')
    if p.occ2 == 'n':
        p.score -= 3
    p.complete_color = input('colors complete? perfect, ok, bad (p,o,b):')
    if p.complete_color == 'b':
        p.score -= 4
    if p.complete_color == 'o':
        p.score -= 2
    p.sturdy = input('sturdy? strong, ish, breaking s/i/b:')
    if p.sturdy == 'i':
        p.score -= 3
    elif p.sturdy == 'b':
        p.score -= 5
    p.ugly = input('beautiful, meh, ugly? (b,m,u):')
    if p.ugly == 'm':
        p.score -= 1
    if p.ugly == 'u':
        p.score -= 3
    p.squat = input('strectched polyhedra? y/n:')
    if p.squat == 'n':
        p.score -= 3
    p.poly_qual = input('Quality polyhedra? y/n:')
    if p.poly_qual == 'n':
        p.score -= 3
    p.poly_tb = input('Top/Bot polyhedra correct? y/n:')
    if p.poly_tb == 'n':
        p.score -= 5
    teams[p.name] = p







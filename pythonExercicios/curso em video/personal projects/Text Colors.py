
c = '\033[m'
print(f'''
\033[0m/033[0m{c}
\033[1m/033[1m{c}
\033[4m/033[4m{c}
\033[7m/033[7m{c}

\033[30m/033[30m{c}
\033[40m/033[40m{c}

\033[31m/033[31m{c}
\033[41m/033[41m{c}

\033[32m/033[32m{c}
\033[42m/033[42m{c}

\033[33m/033[33m{c}
\033[43m/033[43m{c}

\033[34m/033[34m{c}
\033[44m/033[44m{c}

\033[35m/033[35m{c}
\033[45m/033[45m{c}

\033[36m/033[36m{c}
\033[46m/033[46m{c}

\033[37m/033[37m{c}
\033[47m/033[47m{c}

\033[7;30;43m gilded {c}
\033[7;30;48;2;255;200;0m Gilded {c}
\033[1;4;30;41m /033[1;4;30;41m {c}
\033[7;30;41m marked {c}
\033[7;30;48;2;255;0;0m MARKED {c}
\033[7;30m /033[0;30m {c}
''')

f = {'': '\033[m',
     '100': '\033[38;2;55;145;0m',
     '80': '\033[38;2;150;180;0m',
     '60': '\033[38;2;200;175;0m',
     '40': '\033[38;2;200;110;0m',
     '20': '\033[38;2;200;13;0m'}
print(f'{f["100"]}100-81{f[""]}\n'
      f'{f["80"]}80-61{f[""]}\n'
      f'{f["60"]}60-41{f[""]}\n'
      f'{f["40"]}40-21{f[""]}\n'
      f'{f["20"]}20-1{f[""]}')
# [7m invert the colors from [30m and [40m
# 0 = 30 text   40 BACK
# 7 = 30 BACK   40 text
#
# [7;30;48;2;255;0;0m black background red text : MARKED
# [7;30m    black background grey text : ASHEN
#

"""
0 clear
1 bold
3 italic
4 underline
9 crossed out
21 double underline
22 no color or intesity
23 not italic
24 no underline
29 not crossed out

38/48;2;<r>;<g>;<b> rgb control
"""

# alt
# 16 ►
# 92 \
# 124 |
# 175 »
# 179 │
# 180 ┤
# 186 ║
# 191 ┐
# 192 └
# 193 ┴
# 194 ┬
# 195 ├
# 196 ─
# 197 ┼
#
# copied this
#  ̶ ̶ ̶ i̶t can b̶e̶ used ̶o̶n̶ t̶o̶p̶ the̶ l̶et̶t̶e̶r̶s̶
# ͟
# ――― ―
# –––  minus----
# ───
#
# box drawing
# ├ ┌ ┐ │ └ ┘ ┤ ─
# ═ ║ ╔ ╗ ╚ ╝ ╠ ╣
# ░▒▓
# ░
# ▒
# ▓

C = '\033[m'
O = '\033[7;30;44m'
R = '\033[41m'

print(f'{O}█░▒▓{C} {R} {C} buckshot roulette')
input()

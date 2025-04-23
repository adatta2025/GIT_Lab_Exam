print('\nProgram to Print Character Patterns\n')
print("\n====================================\n")
num_line_top = 7
num_line_bot = 6
ch_p = '#'
for num in range(1, num_line_top):
    for num0 in range(1, num_line_top-num):
        print(' ', end=' ')
    for num1 in range(1, 2*num):
        print(ch_p, end=' ')
    print('\n')
for num in range(1, num_line_bot):
    for num0 in range(1, (num+1)):
        print(' ', end=' ')
    for num1 in range(1, (num_line_bot-num)*2):
        print(ch_p, end=' ')
    print('\n')
print("\n====================================\n")

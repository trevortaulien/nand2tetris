def popLabelDeclarations(lines):
    for location, line in enumerate(lines):
        print(lines)
        if(line[0] == '('):
            lines.pop(location)

    return lines

lines =[
    [142, 'D=A'],
    [143, '@95'],
    [144, '0;JMP'],
    [145, '@15'],
    '(ball.new)',
    '(RET_ADDRESS_CALL0)',
    [146, 'D=A'],
    [147, '@SP'],
    ]

result = popLabelDeclarations(lines)
print(lines)

right = {"S":"W", "W":"N", "N":"E","E":"S"}
left = {"S":"E","E":"N","N":"W","W":"S"}
DIRECTIONS = 4

def doesCircleExist(commands):
    result = []
    a,b = 0,0
    current = "N"
    for command in commands:
        for i in range(DIRECTIONS):
            for c in command:
                if c == 'G':
                    if current == "N":
                        b += 1
                    if current == "S":
                        b -= 1
                    if current == "E":
                        a += 1
                    if current == "W":
                        a -= 1
                elif c == 'R':
                    current = right[current]
                elif c == 'L':
                    current = left[current]
        result.append('YES') if a == 0 and b == 0 else result.append('NO')
        current = 'N'
        a,b = 0,0
    return result
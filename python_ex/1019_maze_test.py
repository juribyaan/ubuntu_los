# f2 = open("playMaze.txt" , 'w');
# f2.close();

# f2 = open("playMaze.txt" , 'w')


# lines = f1.read()
# type(lines)
# print(lines)
# lines.count('P')

# print("".join(list(lines)))
# len(lines)

f1 = open("maze.txt" , 'r')
lines = f1.readlines(0)
Y = lines
print(Y)
type(Y)


f1.close()

lines[0]
lines[1]

X = list(lines)
# for i in range(len(Y)):
#     X.append((Y[i]))
X

X.index('F')
X[8]
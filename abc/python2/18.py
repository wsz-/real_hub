a = [[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]]


path = [[a[0][0], [a[0][0]]]]
for i in xrange(1, len(a)):
	newpath = []
	tmp = path[0][1][:]
	tmp.append(a[i][0])
	newpath.append([path[0][0] + a[i][0], tmp])
	for j in xrange(1, i):
		flag = (path[j - 1][0] > path[j][0]) and -1 or 0
		tmp = path[j + flag][1][:]
		tmp.append(a[i][j])
		newpath.append([path[j + flag][0] + a[i][j], tmp])
	tmp = path[i - 1][1][:]
	tmp.append(a[i][i])
	newpath.append([path[i - 1][0] + a[i][i], tmp])
	path = newpath

maxx = [0, 0]
for i in path:
	if i[0] > maxx[0]:
		maxx = i
print maxx

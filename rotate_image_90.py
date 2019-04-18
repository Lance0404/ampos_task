# rotate_image_90().py



def print_arr(arr: list):
	for i in arr:
		print(i)

def rotate_image_90(arr: list):
	pass
	databycol = {}

	for i, x in enumerate(arr): # i is row num
		# print(i, x)
		for ii, y in enumerate(x): # ii is col num
			databycol.setdefault(ii, [])
			databycol[ii].append(y)
			# print(ii, y)

	ret_arr = []
	for i,a in databycol.items():
		b = a[::-1]
		# print(f'{b}')
		ret_arr.append(b)

	return ret_arr





T = [[11, 12, 5, 2], [15, 7, 6,10], [10, 8, 12, 5], [12,15,8,6]]

ans = rotate_image_90(T)
print(ans)

def print_arr(arr: list):
	for i in arr:
		print(i)

def rotate_image_90(arr: list):
	databycol = {}

	for i, x in enumerate(arr): # i is row num
		for ii, y in enumerate(x): # ii is col num
			databycol.setdefault(ii, [])
			databycol[ii].append(y)

	ret_arr = []
	for i,a in databycol.items():
		b = a[::-1]
		ret_arr.append(b)

	return ret_arr

T = [[11, 12, 5, 2], [15, 7, 6,10], [10, 8, 12, 5], [12,15,8,6]]

# before
# print(T)
print_arr(T)
print('----------------------------------')
# after
ans = rotate_image_90(T)
# print(ans)
print_arr(ans)
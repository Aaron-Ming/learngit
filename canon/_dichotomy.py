#arr = [1,2,4,7,20,80,99,111,123,345,1111,3456,7890]
#res = 2
#length = len(arr)
arr = [1,2,4,7,20,80,99,111,123,345,1111,3456,7890]
res = 2
start = 0
end = len(arr)
count = 0
while True:
    count += 1
    mid = (start + end) / 2
    mid_num = arr[mid]
    if res == mid_num:
        print "The num %d index is %d." % (res, mid)
        break
    elif res > mid_num:
	start = mid + 1
    elif res < mid_num:
	end = mid - 1
print "The count is %d" % (count)

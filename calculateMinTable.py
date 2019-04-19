# calculateMinTable.py

'''
Sample test:
	List<TableReservation> customerList = ArrayList<TableReservation>();
	customerList.add(new TableReservation("11:00", "12:00"));
	customerList.add(new TableReservation("11:30", "12:30"));
	customerList.add(new TableReservation("11:40", "12:40"));
	customerList.add(new TableReservation("13:00", "14:00"));

 	calculateMinTable(customerList); // return 3
'''

# find out the minimum num of tables required for serving this business
# find out the number with the most overlap


def calculateMinTable(customerList: list):
    check = {}

    # check everyone at most overlap how many people
    first_loop_cnt = 0
    for x, y in customerList:
        first_loop_cnt += 1
        i_tup = (x, y)
        overlap_cnt = 1  # including self
        second_loop_cnt = 0
        for a, b in customerList:
            second_loop_cnt += 1
            ii_tup = (a, b)
            if first_loop_cnt == second_loop_cnt:  # don't do self compare
                continue
            else:
                if x >= a and x < b:
                    # print(f'{i_tup} overlap with {ii_tup}')
                    overlap_cnt += 1
                    continue
                if y > a and y <= b:
                    # print(f'{i_tup} overlap with {ii_tup}')
                    overlap_cnt += 1
                    continue
        check[i_tup] = overlap_cnt

    table_num = 0

    for i in check.values():
        if i > table_num:
            table_num = i

    return table_num


# 2 element tuple of check in out time
c = [
    ("11:00", "12:00"),
    ("11:30", "12:30"),
    ("11:40", "12:40"),
    ("13:00", "14:00"),
    ("13:00", "14:00"),
    ("11:40", "12:00"),  # additional
    ("11:40", "12:00"),  # additional, 2 customer w/ the same time range

]

table_num = calculateMinTable(c)

print(table_num)

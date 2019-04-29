
### **DIFFICULTY: EASY**
### **CANDIDATE CHOOSE TO FINISH ONLY ONE QUESTION**

**QUESTION EASY#1**

Implement method input string and return number of parenthesis count in that string. In case parenthesis pair is missing or invalid, the method return -1.

```
Sample test:
	parenthesisCount(“(a)(b)()c”)		  // return 3
	parenthesisCount(“(a(b(c)d))”)	  // return 3
	parenthesisCount(“oauaoeuu”)	    // return 0
	parenthesisCount(“o(uaoeuu”)	    // return -1
```

---

**QUESTION EASY#2**

Given two dimension array of image pixels in integers. Implement function to rotate image 90 degrees

```
Sample test:
```

![](https://s3-ap-southeast-1.amazonaws.com/interview.ampostech.com/backend/Q2.png)

---

**QUESTION EASY#3**

Find the beginning of circular reference of link list.
The application must be able to 
* Add the linked list
* Find the beginning node of the circular linked list


![](https://s3-ap-southeast-1.amazonaws.com/interview.ampostech.com/backend/Q3.png)

```
Sample test:
	Node a = new Node();
	Node b = new Node();
	Node c = new Node();
	Node d = new Node();
	a.next = b;
	b.next = c;
	c.next = d;
	d.next = b;

findCircularLinkedList(a) 	// return node b
```

---

**QUESTION EASY#4**

Write a method lengthOfLongestSubstring that take an input string, and return length of longest substring without repeating characters.

```
Sample test:
lengthOfLongestSubstring(“abcabcabc”)	return 3	// abc
lengthOfLongestSubstring(“aaaaa”)			return 1	// a
lengthOfLongestSubstring(“arrghare”)	return 5	// ghare
```

---

## **DIFFICULTY: MODERATE**
## **CANDIDATE CHOOSE TO FINISH ONLY ONE QUESTION**

**QUESTION MODERATE#1**

Implement a function that returns the minimum number of tables needed for a restaurant given the reserved check-in and check-out time.

```
Find number of table needed for those customers.
(More Explanation)
Customer D uses table#1 for 11:00 - 12:00
Customer B uses table#2 for 11:30 - 12:30
Customer C uses table#3 for 11:40 - 12:40
Customer A uses table#1 for 13:00 - 14:00 (Table#1 is available after 12:00 when Customer D checked out.)  
```

![](https://s3-ap-southeast-1.amazonaws.com/interview.ampostech.com/backend/QM1-2.png)

```
Sample test:
	List<TableReservation> customerList = ArrayList<TableReservation>();
	customerList.add(new TableReservation("11:00", "12:00"));
	customerList.add(new TableReservation("11:30", "12:30"));
	customerList.add(new TableReservation("11:40", "12:40"));
	customerList.add(new TableReservation("13:00", "14:00"));

 	calculateMinTable(customerList); // return 3
```

---

**QUESTION MODERATE#2**

Write a method diagonalTable that given an integer n (size of table), return a table of n*n, 2-dimensional array, that contains number 1 to n*n. The number 1 is in the upper right corner and other numbers should be arranged along the diagonals from the top to the bottom. The last number (n*n) is in the lower left corner.

```
Sample test:
```

![](https://s3-ap-southeast-1.amazonaws.com/interview.ampostech.com/backend/QM2.png)



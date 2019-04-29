
### **ข้อง่าย EASY**
### **เลือกทำ 1 ข้อ**

**คำถาม EASY#1**

เขียนโปรแกรม parenthesisCount() รับ string เข้ามา เพื่อนับจำนวนคู่ของวงเล็บและให้ return จำนวนคู่ของวงเล็บที่นับได้  ซึ่งถ้าคู่ของวงเล็บเปิด-ปิดไม่ครบคู่ หรือลำดับเปิด-ปิดไม่ถูกต้องให้ return -1.

```
ตัวอย่าง:
	parenthesisCount(“(a)(b)()c”)		  // return 3
	parenthesisCount(“(a(b(c)d))”)	  // return 3
	parenthesisCount(“oauaoeuu”)	    // return 0
	parenthesisCount(“o(uaoeuu”)	    // return -1
```

---

**คำถาม EASY#2**

เขียนโปรแกรมเพื่อหมุนค่าใน array ทวนเข็มนาฬิกาตามรูป

```
ตัวอย่าง(ดูรูป):
```

![](https://s3-ap-southeast-1.amazonaws.com/interview.ampostech.com/backend/Q2.png)

---

**คำถาม EASY#3**

เขียนโปรแกรม findCircularLinkedList() หา node ที่เป็นจุดเริ่มของ Circular linked list โดยโปรแกรมจะต้อง
- เพิ่ม node ตัวใหม่เข้า linked list ได้
- หา node ที่เป็นจุดเริ่มของ Circular linked list ได้


![](https://s3-ap-southeast-1.amazonaws.com/interview.ampostech.com/backend/Q3.png)

```
ตัวอย่าง:
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

**คำถาม EASY#4**

เขียนโปรแกรม lengthOfLongestSubstring() รับ string เข้ามา เพื่อหาจำนวนตัวอักษรที่ติดกันและยาวที่สุดโดยไม่ซ้ำ

```
ตัวอย่าง:
lengthOfLongestSubstring(“abcabcabc”)	return 3	// abc
lengthOfLongestSubstring(“aaaaa”)			return 1	// a
lengthOfLongestSubstring(“arrghare”)	return 5	// ghare
```

---

## **ข้อปานกลาง MODERATE**
## **เลือกทำ 1 ข้อ**

**คำถาม MODERATE#1**

เขียนโปรแกรม calculateMinTable() รับช่วงเวลาที่จองโต๊ะอาหาร เพื่อคำนวณหาจำนวนโต๊ะที่น้อยที่สุดที่ต้องใช้

```
ตัวอย่างช่วงเวลาที่จองโต๊ะ(ดูรูป):
Customer D uses table#1 for 11:00 - 12:00
Customer B uses table#2 for 11:30 - 12:30
Customer C uses table#3 for 11:40 - 12:40
Customer A uses table#1 for 13:00 - 14:00 (Table#1 ว่างหลังจาก 12:00 เมื่อ Customer D เสร็จแล้ว)
```

![](https://s3-ap-southeast-1.amazonaws.com/interview.ampostech.com/backend/QM1-2.png)

```
ตัวอย่าง:
	List<TableReservation> customerList = ArrayList<TableReservation>();
	customerList.add(new TableReservation("11:00", "12:00"));
	customerList.add(new TableReservation("11:30", "12:30"));
	customerList.add(new TableReservation("11:40", "12:40"));
	customerList.add(new TableReservation("13:00", "14:00"));

 	calculateMinTable(customerList); // return 3
```

---

**คำถาม MODERATE#2**
เขียนโปรแกรมรับ integer n (ขนาดของ table) โดยผลลัพทธ์ของ table เป็น array 2มิติที่เป็นเลขเรียงตั้งแต่ 1 จนถึง n*n และเรียงแบบเส้นทแยงมุม (diagonalTable), ลองดูรูปตัวอย่าง

![](https://s3-ap-southeast-1.amazonaws.com/interview.ampostech.com/backend/QM2.png)



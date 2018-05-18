In [12]: salesReceipt = collections.namedtuple("salesReceipt", ["storeID", "saleDate", "saleAmount", "totalGuests"])

In [13]: store22 = salesReceipt(22, "12-14-2017", 45.32, 3)

In [14]: store15 = salesReceipt(15, "12-14-2017", 22.50, 1)

In [15]: print("Store ID = ", store22.storeID)
Store ID =  22

In [16]: print("Sales amount = ", store15.saleAmount)
Sales amount =  22.5

In [17]: for i in store22:
    ...:     print(i)
    ...:     
22
12-14-2017
45.32
3

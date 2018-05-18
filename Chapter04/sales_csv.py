In [22]: from csv import reader

In [23]: with open("sales_record.csv", "r") as input_file:
    ...:     csv_fields = reader(input_file)
    ...:     for field_list in csv_fields:
    ...:         store_record = salesReceipt._make(field_list)
    ...:         total_sales += float(store_record.saleAmount)
    ...:         

In [24]: print("Total sales = ", total_sales)
Total sales =  105.97

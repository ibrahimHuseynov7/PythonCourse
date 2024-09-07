
nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False, True))


tuple1, tuple2, tuple3 = nested_tuple


b_index = tuple2.index("b")


true_count = tuple3.count(True)


print("First nested tuple:", tuple1)
print("Second nested tuple:", tuple2)
print("Third nested tuple:", tuple3)
print('"b" element index:', b_index)
print("The number of Trues:", true_count)

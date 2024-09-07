
nested_tuple = (("a", "b", "c"), (1, 2, 3), (True, False, True))



new_tuple = (nested_tuple[0][0],  
              nested_tuple[1][0], 
              nested_tuple[1][2],  
              nested_tuple[2][0],  
              nested_tuple[2][2])  


print("New tuple:", new_tuple)

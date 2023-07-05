import ctypes

# add path to so file
clibrary = ctypes.CDLL(
    "C:/Users/jayan/code_fun/LearnC/ctypes_test/ctypes-demo/clibrary.so"
)

array_add = clibrary.arrayAdd

array_add.argtypes = [
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int,
]
array_add.restype = ctypes.POINTER(ctypes.c_int)
values = [1, 2, 4, 5, 6, 7, 8, 9, 11, 12]
values2 = [2, 4, 6, 11, 19, 21, 23, 24, 11, 13]
array = (ctypes.c_int * len(values))(*values)
array2 = (ctypes.c_int * len(values2))(*values2)
test = array_add(array, array2, len(values))
for i in range(len(values)):
    print(test[i], end=", ")
free_mem = clibrary.free_memory
free_mem.arg_types = [ctypes.c_void_p]
free_mem(test)

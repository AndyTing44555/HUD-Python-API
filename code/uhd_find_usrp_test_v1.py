import uhd
try:
    u = uhd.usrp.MultiUSRP()  # no device present
    print("Unexpectedly created USRP:", u.get_pp_string())
except Exception as e:
    print("Expected failure (no device):", type(e).__name__)
    print(e)

# import sys
# print("Python executable:", sys.executable)
# # print("sys.path:", sys.path)

# import uhd
# print(uhd.__file__)
import uhd, sys
print("python:", sys.executable)
print("uhd file:", uhd.__file__)
print("uhd version:", getattr(uhd, "__version__", "unknown"))
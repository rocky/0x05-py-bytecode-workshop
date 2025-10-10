def to_int(x):
    return int(x)

x = "5"
try:
    x[4]
except IndexError:
    try:
        print(to_int(x))
    except Exception:
        print("This should not get reached")

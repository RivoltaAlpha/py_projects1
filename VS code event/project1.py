test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

def my_function():
    print("Hello World")
    n = int(input("Check this number: "))
prime_checker(number=n)
    def paint_calc(height, width, cover):
        print(f"The wall is {height} x {width} x {cover} cm")
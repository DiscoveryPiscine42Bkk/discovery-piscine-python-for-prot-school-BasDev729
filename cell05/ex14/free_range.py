import sys

if len(sys.argv) != 3:
    print("none")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    
    range_values = list(range(num1, num2))
        
    print(range_values)

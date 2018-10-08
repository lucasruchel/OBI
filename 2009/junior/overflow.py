max_op = int(input())

n1, op, n2 = input().split()

value = 0

if op == "*":
    value = int(n1) * int(n2)
else:
    value = int(n1) + int(n2)

if ( value > max_op ) :
    print("OVERFLOW")
else:
    print("OK")

def solution(N):
    integer = N
    for num in range(1, integer):
        if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
            print("CodilityTestCoders")
        elif num % 2 == 0 and num % 3 == 0:
            print("CodilityTest")
        elif num % 5 == 0 and num % 2 == 0:
            print("CodilityCoders")
        elif num % 2 == 0 and num % 5 == 0:
            print("CodilityTest")
        elif num % 2 == 0 and num % 5 == 0:
            print("CodilityTest")
        elif num % 2 == 0:
            print("Codility")
        elif num % 3 == 0:
            print("Test")
        elif num % 5 == 0:
            print("Coders")
        else:
            print(num)


solution(24)

print("-------")
print(2 % 2)
print(2 % 3)
print(2 % 5)

if 1 == 1 and 2 == 2:
    print("Both statements are true")
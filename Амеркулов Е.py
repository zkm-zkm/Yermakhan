# Арифметика
print(10 - 3)           # 7
print(5 + 4)              # 9
print( 6 * 7)           # 42
print( 2 ** 3)  # 8
print(10 / 4)             # 2.5
print(10 // 4)      # 2
print(10 % 4)           # 2

# while
i = 1
while i <= 5:
    print("while:", i)
    i += 1

# for 
for j in range(1, 6):
    print("for:", j)

# 1. кері рет
Yermakhan = [1, 2, 3, 4, 5]
print(":", Yermakhan)
print(":", Yermakhan[::-1])

# 2.  кему рет
def ls(lst):
    return sorted(Yermakhan, key=lambda x: abs(x), reverse=True)

print("abs:", ls([3, -10, 5, -2, 7]))

# 3. Бірінші және соңғы элементті орын ауыстыру
def change(Yermakhan):
    if len(Yermakhan) >= 2:
        Yermakhan[0], Yermakhan[-1] = Yermakhan[-1], Yermakhan[0]
    return Yermakhan

print(":", change([1, 2, 3, 4, 5]))
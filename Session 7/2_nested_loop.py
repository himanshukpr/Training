# test

bricks = int(input("Enter the number of bricks: "))

print("Wall must be constructed with", bricks, "bricks.")

total_brick = bricks
left_brick = 0
jack_brick = 1
john_brick = 1

for j in range(1, bricks + 1,3):
    jack_brick = j
    john_brick = jack_brick + 2

    if jack_brick > bricks:
        left_brick = total_brick-john_brick + 3
        print("Jack", jack_brick - 3)
        break

    if john_brick > bricks:
        left_brick = total_brick-john_brick + 3
        print('john', john_brick - 3)
        break

    print("Jack's brick is", jack_brick)
    print("John's brick is", john_brick)


print('left Bricks',left_brick)

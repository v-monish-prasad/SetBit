def setBit(firstBit, secondBit):
    zero = 0

    zero ^= 1 << firstBit

    if firstBit != secondBit:
        zero ^= 1 << secondBit

    return zero


if __name__ == "__main__":
    A = int(input())
    B = int(input())

    print(setBit(A, B))

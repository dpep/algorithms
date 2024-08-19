#!/usr/bin/env python


def toNum(binary):
    num = 0
    while binary:
        num *= 2

        if binary[0] == "1":
            num += 1

        binary = binary[1:]

    return num


def toBin(num):
    bin = ""

    while num:
        if num % 2:
            bin = "1" + bin
        else:
            bin = "0" + bin

        num = int(num / 2)

    return bin


def binAdd(bin1, bin2):
    res = ""
    carry = 0

    while bin1 or bin2:
        bit1 = 1 if bin1 and bin1[-1] == "1" else 0
        bit2 = 1 if bin2 and bin2[-1] == "1" else 0

        nextBit = (bit1 + bit2 + carry) % 2
        carry = int((bit1 + bit2 + carry) / 2)

        if nextBit:
            res = "1" + res
        else:
            res = "0" + res

        bin1 = bin1[:-1]
        bin2 = bin2[:-1]

    if carry:
        res = "1" + res

    return res



bin1 = "101"
bin2 = "111"

print(toBin(toNum(bin1) + toNum(bin2)))
print(binAdd(bin1, bin2))

# -----------------------
#   Advent of Code 2021
#   Day 16 Part 1
#   Author: James Hess
# -----------------------

hexInput = ''

# Parse puzzle input file and store necessary data in list
with open("Day16Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        hexInput = line.strip()

# Convert to binary
binInput = bin(int(hexInput, 16))[2:].zfill(len(hexInput)*4)

versions = []

print("Binary Input: " + binInput)

def lengthSubDecoder(length,packet):
    # trim packet to length
    packet = packet[:length]

def countSubDecoder(count,packet):
    test=1

def decoder(packet):
    # Extract version, type, and contents
    version = int(packet[:3], 2)
    typeID = int(packet[3:6], 2)
    packet = binInput[6:]

    print("Version: " + str(version), end='; ')
    print("Type ID: " + str(typeID), end='; ')
    print("Packet: " + packet)

    # if packet is type literal
    if typeID == 4:
        litEnd = 1
        litBinary = ''
        while litEnd == 1:
            literalGroup = packet[0:5]
            litBinary = litBinary + literalGroup[1:]
            litEnd = int(literalGroup[0])
            packet = packet[5:]
        litDecimal = int(litBinary, 2)
        print("Literal Value: " + str(litDecimal))

    # if packet is type operator
    else:
        lengthTypeID = int(packet[0])
        print("Length Type ID: " + str(lengthTypeID), end='')
        # if operator packet is type total length in bits
        if lengthTypeID == 0:
            print(" (length in bits)")
            totalLength = int(packet[1:16],2)
            print("Sub-packets Total Length: " + str(totalLength), end='; ')
            remainPacket = packet[16:]
            print("Remaining Packet: " + remainPacket)
            lengthSubDecoder(totalLength, remainPacket)
        # if operator packet is type number of sub-packets
        elif lengthTypeID == 1:
            print(" (number of sub packets)")
            countPackets = int(packet[1:12],2)
            print("Sub-packets Count: " + str(countPackets), end='; ')
            remainPacket = packet[12:]
            print("Remaining Packet: " + remainPacket)
            countSubDecoder(countPackets, remainPacket)
decoder(binInput)
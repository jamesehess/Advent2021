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

#print("Binary Input: " + binInput)

def literaldecorder(packet):
    groupCount = 0
    litEnd = 1
    litBinary = ''
    while litEnd == 1:
        literalGroup = packet[0:5]
        litBinary = litBinary + literalGroup[1:]
        litEnd = int(literalGroup[0])
        packet = packet[5:]
        groupCount += 1
    litDecimal = int(litBinary, 2)
    print("Literal Value: " + str(litDecimal))
    #print("Consumed: " + str(groupCount * 5))
    return groupCount * 5

def operatordecorder(packet):
    lengthTypeID = int(packet[0])
    print("Length Type ID: " + str(lengthTypeID), end='')
    # if operator packet is type total Length in bits
    if lengthTypeID == 0:
        print(" (length in bits)")
        totalLength = int(packet[1:16], 2)
        print("Sub-packets Total Length: " + str(totalLength), end='; ')
        remainPacket = packet[16:]
        print("Remaining Packet: " + remainPacket)
        decoder(remainPacket, 'length', totalLength)
        return remainPacket, totalLength

    # if operator packet is type Count of sub-packets
    elif lengthTypeID == 1:
        print(" (number of sub packets)")
        countPackets = int(packet[1:12], 2)
        print("Sub-packets Count: " + str(countPackets), end='; ')
        remainPacket = packet[12:]
        print("Remaining Packet: " + remainPacket)
        totalConsumed = decoder(remainPacket, 'count', countPackets)
        return remainPacket, totalConsumed

def decoder(packet,subtype,subcount=1):
    print("###")
    consumed = 0
    totConsumed = 0
    while subcount > 0:
        packet = packet[consumed:]
        print("packet: " + packet + "; subtype: " + subtype + "; subcount: " + str(subcount))
        # Extract version, type, and packet contents
        version = int(packet[:3], 2)
        typeID = int(packet[3:6], 2)
        packet = packet[6:]

        print("Version: " + str(version), end='; ')
        print("Type ID: " + str(typeID), end='; ')
        print("Packet: " + packet)

        versions.append(version)

        if typeID == 4:  # if packet is type literal
            consumed = literaldecorder(packet)
        else:  # if packet is type operator
            packet, consumed = operatordecorder(packet)

        if subtype == 'main' or subtype == 'count':
            subcount -= 1
        elif subtype == 'length':
            subcount -= consumed + 6
        totConsumed += consumed
    return totConsumed

decoder(binInput,'main')
print(versions)
print(sum(versions))
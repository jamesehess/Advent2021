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

def decoder(packet,subtype,subcount=1):
    print("###")
    consumed = 0
    while subcount > 0:
        print("packet: " + packet + "; subtype: " + subtype + "; subcount: " + str(subcount))
        # Extract version and type then trim packet
        version = int(packet[:3], 2)
        typeID = int(packet[3:6], 2)
        packet = packet[6:]
        consumed += 6

        print("Version: " + str(version), end='; ')
        print("Type ID: " + str(typeID), end='; ')
        print("Packet: " + packet)

        versions.append(version)

        if typeID == 4:  # if packet is type literal
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
            consumed += groupCount * 5

        else:  # if packet is type operator
            lengthTypeID = int(packet[0])
            print("Length Type ID: " + str(lengthTypeID), end='')

            # if operator packet is type total Length in bits
            if lengthTypeID == 0:
                print(" (length in bits)")
                totalLength = int(packet[1:16], 2)
                print("Sub-packets Total Length: " + str(totalLength), end='; ')
                remainPacket = packet[16:]
                print("Remaining Packet: " + remainPacket)
                consumed += decoder(remainPacket, 'length', totalLength)
                consumed += 16

            # if operator packet is type Count of sub-packets
            elif lengthTypeID == 1:
                print(" (number of sub packets)")
                countPackets = int(packet[1:12], 2)
                print("Sub-packets Count: " + str(countPackets), end='; ')
                remainPacket = packet[12:]
                print("Remaining Packet: " + remainPacket)
                consumed += decoder(remainPacket, 'count', countPackets)
                consumed += 12

        if subtype == 'main' or subtype == 'count':
            subcount -= 1
        elif subtype == 'length':
            subcount -= consumed

        packet = packet[consumed:]
    return consumed

decoder(binInput,'main')
print(versions)
print(sum(versions))
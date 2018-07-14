node_id_to_thing_map = []
thing_to_node_id_map = {}

for X in range(1, 9):
    for Y in range(6):
        # print(X, Y)

        if X == 1 or X == 8:
            if Y == 0 or Y == 5:
                continue

            for I in range(5):
                # print(X, Y, I)
                node_id_to_thing_map.append(('IO_DATAIN SINK', X, Y, I))
                thing_to_node_id_map[('IO_DATAIN SINK', X, Y, I)] = len(node_id_to_thing_map) - 1
                node_id_to_thing_map.append(('OE SINK', X, Y, I))
                thing_to_node_id_map[('OE SINK', X, Y, I)] = len(node_id_to_thing_map) - 1
                node_id_to_thing_map.append(('IO_DATAOUT SOURCE', X, Y, I))
                thing_to_node_id_map[('IO_DATAOUT SOURCE', X, Y, I)] = len(node_id_to_thing_map) - 1
            for I in range(5):
                # print(X, Y, I)
                node_id_to_thing_map.append(('IO_DATAIN', X, Y, I))
                thing_to_node_id_map[('IO_DATAIN', X, Y, I)] = len(node_id_to_thing_map) - 1
                node_id_to_thing_map.append(('OE', X, Y, I))
                thing_to_node_id_map[('OE', X, Y, I)] = len(node_id_to_thing_map) - 1
                node_id_to_thing_map.append(('IO_DATAOUT', X, Y, I))
                thing_to_node_id_map[('IO_DATAOUT', X, Y, I)] = len(node_id_to_thing_map) - 1
        else:
            if Y == 0 or Y == 5:
                for I in range(4):
                    # print(X, Y, I)
                    node_id_to_thing_map.append(('IO_DATAIN SINK', X, Y, I))
                    thing_to_node_id_map[('IO_DATAIN SINK', X, Y, I)] = len(node_id_to_thing_map) - 1
                    node_id_to_thing_map.append(('OE SINK', X, Y, I))
                    thing_to_node_id_map[('OE SINK', X, Y, I)] = len(node_id_to_thing_map) - 1
                    node_id_to_thing_map.append(('IO_DATAOUT SOURCE', X, Y, I))
                    thing_to_node_id_map[('IO_DATAOUT SOURCE', X, Y, I)] = len(node_id_to_thing_map) - 1
                for I in range(4):
                    # print(X, Y, I)
                    node_id_to_thing_map.append(('IO_DATAIN', X, Y, I))
                    thing_to_node_id_map[('IO_DATAIN', X, Y, I)] = len(node_id_to_thing_map) - 1
                    node_id_to_thing_map.append(('OE', X, Y, I))
                    thing_to_node_id_map[('OE', X, Y, I)] = len(node_id_to_thing_map) - 1
                    node_id_to_thing_map.append(('IO_DATAOUT', X, Y, I))
                    thing_to_node_id_map[('IO_DATAOUT', X, Y, I)] = len(node_id_to_thing_map) - 1
            else:
                for I in range(26):
                    node_id_to_thing_map.append(('LOCAL_INTERCONNECT SINK', X, Y, I))
                    thing_to_node_id_map[('LOCAL_INTERCONNECT SINK', X, Y, I)] = len(node_id_to_thing_map) - 1
                node_id_to_thing_map.append(('LAB CIN SINK', X, Y, I))
                thing_to_node_id_map[('LAB CIN SINK', X, Y, I)] = len(node_id_to_thing_map) - 1
                for I in range(20):
                    node_id_to_thing_map.append(('LE_BUFFER SOURCE', X, Y, I))
                    thing_to_node_id_map[('LE_BUFFER SOURCE', X, Y, I)] = len(node_id_to_thing_map) - 1
                node_id_to_thing_map.append(('LAB COUT SOURCE', X, Y, I))
                thing_to_node_id_map[('LAB COUT SOURCE', X, Y, I)] = len(node_id_to_thing_map) - 1
                for I in range(4):
                    node_id_to_thing_map.append(('GCLK SINK', X, Y, I))
                    thing_to_node_id_map[('GCLK SINK', X, Y, I)] = len(node_id_to_thing_map) - 1

                for I in range(26):
                    node_id_to_thing_map.append(('LOCAL_INTERCONNECT', X, Y, I))
                    thing_to_node_id_map[('LOCAL_INTERCONNECT', X, Y, I)] = len(node_id_to_thing_map) - 1
                node_id_to_thing_map.append(('LAB CIN', X, Y, I))
                thing_to_node_id_map[('LAB CIN', X, Y, I)] = len(node_id_to_thing_map) - 1
                for I in range(20):
                    node_id_to_thing_map.append(('LE_BUFFER', X, Y, I))
                    thing_to_node_id_map[('LE_BUFFER', X, Y, I)] = len(node_id_to_thing_map) - 1
                node_id_to_thing_map.append(('LAB COUT', X, Y, I))
                thing_to_node_id_map[('LAB COUT', X, Y, I)] = len(node_id_to_thing_map) - 1
                for I in range(4):
                    node_id_to_thing_map.append(('GCLK', X, Y, I))
                    thing_to_node_id_map[('GCLK', X, Y, I)] = len(node_id_to_thing_map) - 1

assert len(node_id_to_thing_map) == 3024
assert len(thing_to_node_id_map) == 3024

# print(node_id_to_thing_map)
# print(thing_to_node_id_map)

NODESNODESNODES = ''
PTCPTC = {}

# R wires
for X in range(1, 8):
    for Y in range(1, 5):
        for I in range(8):
            nodeidx = len(node_id_to_thing_map)

            ptcval = PTCPTC.get(('R', X, Y), 0)
            PTCPTC[('R', X, Y)] = ptcval + 1

            node_id_to_thing_map.append(('R', X, Y, I))
            thing_to_node_id_map[('R', X, Y, I)] = nodeidx

            NODESNODESNODES += """<node id="{}" type="CHANX" direction="INC_DIR" capacity="1">
    <loc xlow="{}" ylow="{}" xhigh="{}" yhigh="{}" ptc="{}"/>
    <segment segment_id="0"/>
</node>
""".format(nodeidx, X, Y, min(X + 4, 7), Y, ptcval)

for i in range(len(node_id_to_thing_map)):
    print("Node {} is {}".format(i, node_id_to_thing_map[i]))

# print(NODESNODESNODES)

with open('rrgraph.xml', 'r') as f:
    lines = f.readlines()

with open('rrgraph-newnew.xml', 'w') as f:
    for l in lines:
        f.write(l)
        if "~+~+~+ PUT CHANNELS HERE +~+~+~" in l:
            f.write(NODESNODESNODES)

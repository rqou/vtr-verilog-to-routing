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

            node_id_to_thing_map.append(('R', X, Y, I))
            thing_to_node_id_map[('R', X, Y, I)] = nodeidx

            endX = min(X + 4, 7)

            ptcval = None
            for i in range(64):
                usedinany = False
                for j in range(X, endX + 1):
                    usedindices = PTCPTC.get(('R', j, Y), [])
                    if i in usedindices:
                        usedinany = True
                        break
                if not usedinany:
                    ptcval = i
                    break
            assert ptcval is not None

            for i in range(X, endX + 1):
                if ('R', i, Y) not in PTCPTC:
                    PTCPTC[('R', i, Y)] = set()
                PTCPTC[('R', i, Y)].add(ptcval)

            NODESNODESNODES += """<node id="{}" type="CHANX" direction="INC_DIR" capacity="1">
    <loc xlow="{}" ylow="{}" xhigh="{}" yhigh="{}" ptc="{}"/>
    <segment segment_id="0"/>
</node>
""".format(nodeidx, X, Y, endX, Y, ptcval)

# L wires
for X in range(2, 8):
    for Y in range(1, 5):
        for I in range(8):
            nodeidx = len(node_id_to_thing_map)

            node_id_to_thing_map.append(('L', X, Y, I))
            thing_to_node_id_map[('L', X, Y, I)] = nodeidx

            startX = max(X - 4, 1)

            ptcval = None
            for i in range(64):
                usedinany = False
                for j in range(startX, X + 1):
                    usedindices = PTCPTC.get(('L', j, Y), [])
                    if i in usedindices:
                        usedinany = True
                        break
                if not usedinany:
                    ptcval = i
                    break
            assert ptcval is not None

            for i in range(startX, X + 1):
                if ('L', i, Y) not in PTCPTC:
                    PTCPTC[('L', i, Y)] = set()
                PTCPTC[('L', i, Y)].add(ptcval)

            NODESNODESNODES += """<node id="{}" type="CHANX" direction="DEC_DIR" capacity="1">
    <loc xlow="{}" ylow="{}" xhigh="{}" yhigh="{}" ptc="{}"/>
    <segment segment_id="0"/>
</node>
""".format(nodeidx, startX, Y, X, Y, ptcval)

# L2 wires
X = 7
for Y in range(1, 5):
    for I in range(8):
        nodeidx = len(node_id_to_thing_map)

        node_id_to_thing_map.append(('L2', X, Y, I))
        thing_to_node_id_map[('L2', X, Y, I)] = nodeidx

        ptcval = None
        for i in range(64):
            usedindices = PTCPTC.get(('L', j, Y), [])
            if i not in usedindices:
                ptcval = i
                break
        assert ptcval is not None

        if ('L', X, Y) not in PTCPTC:
            PTCPTC[('L', X, Y)] = set()
        PTCPTC[('L', X, Y)].add(ptcval)

        NODESNODESNODES += """<node id="{}" type="CHANX" direction="DEC_DIR" capacity="1">
    <loc xlow="{}" ylow="{}" xhigh="{}" yhigh="{}" ptc="{}"/>
    <segment segment_id="0"/>
</node>
""".format(nodeidx, X, Y, X, Y, ptcval)

# U wires
for X in range(1, 8):
    Y = 0
    for I in range(10):
        nodeidx = len(node_id_to_thing_map)

        node_id_to_thing_map.append(('U', X, Y, I))
        thing_to_node_id_map[('U', X, Y, I)] = nodeidx

        endY = 4 if I < 7 else 1

        ptcval = None
        for i in range(56):
            usedinany = False
            for j in range(Y, endY + 1):
                usedindices = PTCPTC.get(('U', X, j), [])
                if i in usedindices:
                    usedinany = True
                    break
            if not usedinany:
                ptcval = i
                break
        assert ptcval is not None

        for i in range(Y, endY + 1):
            if ('U', X, i) not in PTCPTC:
                PTCPTC[('U', X, i)] = set()
            PTCPTC[('U', X, i)].add(ptcval)

        NODESNODESNODES += """<node id="{}" type="CHANY" direction="INC_DIR" capacity="1">
    <loc xlow="{}" ylow="{}" xhigh="{}" yhigh="{}" ptc="{}"/>
    <segment segment_id="0"/>
</node>
""".format(nodeidx, X, 1, X, endY, ptcval)

for X in range(1, 8):
    for Y in range(1, 5):
        for I in range(7):
            nodeidx = len(node_id_to_thing_map)

            node_id_to_thing_map.append(('U', X, Y, I))
            thing_to_node_id_map[('U', X, Y, I)] = nodeidx

            endY = min(Y + 4, 4)

            ptcval = None
            for i in range(56):
                usedinany = False
                for j in range(Y, endY + 1):
                    usedindices = PTCPTC.get(('U', X, j), [])
                    if i in usedindices:
                        usedinany = True
                        break
                if not usedinany:
                    ptcval = i
                    break
            assert ptcval is not None

            for i in range(Y, endY + 1):
                if ('U', X, i) not in PTCPTC:
                    PTCPTC[('U', X, i)] = set()
                PTCPTC[('U', X, i)].add(ptcval)

            NODESNODESNODES += """<node id="{}" type="CHANY" direction="INC_DIR" capacity="1">
    <loc xlow="{}" ylow="{}" xhigh="{}" yhigh="{}" ptc="{}"/>
    <segment segment_id="0"/>
</node>
""".format(nodeidx, X, Y, X, endY, ptcval)

# D wires
for X in range(1, 8):
    Y = 5
    for I in range(10):
        nodeidx = len(node_id_to_thing_map)

        node_id_to_thing_map.append(('D', X, Y, I))
        thing_to_node_id_map[('D', X, Y, I)] = nodeidx

        startY = 1 if I < 7 else 4

        ptcval = None
        for i in range(56):
            usedinany = False
            for j in range(startY, Y + 1):
                usedindices = PTCPTC.get(('D', X, j), [])
                if i in usedindices:
                    usedinany = True
                    break
            if not usedinany:
                ptcval = i
                break
        assert ptcval is not None

        for i in range(startY, Y + 1):
            if ('D', X, i) not in PTCPTC:
                PTCPTC[('D', X, i)] = set()
            PTCPTC[('D', X, i)].add(ptcval)

        NODESNODESNODES += """<node id="{}" type="CHANY" direction="DEC_DIR" capacity="1">
    <loc xlow="{}" ylow="{}" xhigh="{}" yhigh="{}" ptc="{}"/>
    <segment segment_id="0"/>
</node>
""".format(nodeidx, X, startY, X, 4, ptcval)

for X in range(1, 8):
    for Y in range(1, 5):
        for I in range(7):
            nodeidx = len(node_id_to_thing_map)

            node_id_to_thing_map.append(('D', X, Y, I))
            thing_to_node_id_map[('D', X, Y, I)] = nodeidx

            startY = max(Y - 4, 1)

            ptcval = None
            for i in range(56):
                usedinany = False
                for j in range(startY, Y + 1):
                    usedindices = PTCPTC.get(('D', X, j), [])
                    if i in usedindices:
                        usedinany = True
                        break
                if not usedinany:
                    ptcval = i
                    break
            assert ptcval is not None

            for i in range(startY, Y + 1):
                if ('D', X, i) not in PTCPTC:
                    PTCPTC[('D', X, i)] = set()
                PTCPTC[('D', X, i)].add(ptcval)

            NODESNODESNODES += """<node id="{}" type="CHANY" direction="DEC_DIR" capacity="1">
    <loc xlow="{}" ylow="{}" xhigh="{}" yhigh="{}" ptc="{}"/>
    <segment segment_id="0"/>
</node>
""".format(nodeidx, X, startY, X, Y, ptcval)

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

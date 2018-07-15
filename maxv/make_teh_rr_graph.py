import json
with open('initial-interconnect.json', 'r') as f:
    interconnectinterconnect = json.load(f)

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
                for I in range(4):
                    node_id_to_thing_map.append(('GCLK SINK', X, Y, I))
                    thing_to_node_id_map[('GCLK SINK', X, Y, I)] = len(node_id_to_thing_map) - 1
                for I in range(20):
                    node_id_to_thing_map.append(('LE_BUFFER SOURCE', X, Y, I))
                    thing_to_node_id_map[('LE_BUFFER SOURCE', X, Y, I)] = len(node_id_to_thing_map) - 1
                node_id_to_thing_map.append(('LAB COUT SOURCE', X, Y, I))
                thing_to_node_id_map[('LAB COUT SOURCE', X, Y, I)] = len(node_id_to_thing_map) - 1

                for I in range(26):
                    node_id_to_thing_map.append(('LOCAL_INTERCONNECT', X, Y, I))
                    thing_to_node_id_map[('LOCAL_INTERCONNECT', X, Y, I)] = len(node_id_to_thing_map) - 1
                node_id_to_thing_map.append(('LAB CIN', X, Y, I))
                thing_to_node_id_map[('LAB CIN', X, Y, I)] = len(node_id_to_thing_map) - 1
                for I in range(4):
                    node_id_to_thing_map.append(('GCLK', X, Y, I))
                    thing_to_node_id_map[('GCLK', X, Y, I)] = len(node_id_to_thing_map) - 1
                for I in range(20):
                    node_id_to_thing_map.append(('LE_BUFFER', X, Y, I))
                    thing_to_node_id_map[('LE_BUFFER', X, Y, I)] = len(node_id_to_thing_map) - 1
                node_id_to_thing_map.append(('LAB COUT', X, Y, I))
                thing_to_node_id_map[('LAB COUT', X, Y, I)] = len(node_id_to_thing_map) - 1

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

            node_id_to_thing_map.append(('L', X + 1, Y, I))
            thing_to_node_id_map[('L', X + 1, Y, I)] = nodeidx

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

        node_id_to_thing_map.append(('L2', X + 1, Y, I))
        thing_to_node_id_map[('L2', X + 1, Y, I)] = nodeidx

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

    if X == 1:
        rrr = range(0, 5)
    elif X == 7:
        rrr = range(5, 10)
    else:
        rrr = range(10)

    for I in rrr:
        nodeidx = len(node_id_to_thing_map)

        adjX = X
        if X == 1:
            adjI = I
        else:
            adjI = I + 5
            if adjI >= 10:
                adjI -= 10
                adjX += 1
        if adjX == 1:
            adjX = 2
        if adjX == 8:
            adjX = 7
            adjI += 5

        node_id_to_thing_map.append(('U', adjX, Y, adjI))
        thing_to_node_id_map[('U', adjX, Y, adjI)] = nodeidx

        # endY = 4 if I < 7 else 1
        endY = 4

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

            node_id_to_thing_map.append(('U', X + 1, Y, I))
            thing_to_node_id_map[('U', X + 1, Y, I)] = nodeidx

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

    if X == 1:
        rrr = range(0, 5)
    elif X == 7:
        rrr = range(5, 10)
    else:
        rrr = range(10)

    for I in rrr:
        nodeidx = len(node_id_to_thing_map)

        adjX = X
        if X == 1:
            adjI = I
        else:
            adjI = I + 5
            if adjI >= 10:
                adjI -= 10
                adjX += 1
        if adjX == 1:
            adjX = 2
        if adjX == 8:
            adjX = 7
            adjI += 5

        node_id_to_thing_map.append(('D', adjX, Y, adjI))
        thing_to_node_id_map[('D', adjX, Y, adjI)] = nodeidx

        # startY = 1 if I == 6 or I == 8 or I == 9 else 4
        startY = 1

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

            node_id_to_thing_map.append(('D', X + 1, Y, I))
            thing_to_node_id_map[('D', X + 1, Y, I)] = nodeidx

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

# local interconnect for left/right IOs
for (myX, vtrX) in [(1, 1), (8, 7)]:
    for Y in range(1, 5):
        for I in range(18):
            nodeidx = len(node_id_to_thing_map)

            node_id_to_thing_map.append(('LOCAL_INTERCONNECT', myX, Y, I))
            thing_to_node_id_map[('LOCAL_INTERCONNECT', myX, Y, I)] = nodeidx

            ptcval = None
            for i in range(64):
                usedindices = PTCPTC.get(('R', vtrX, Y), [])
                if i not in usedindices:
                    ptcval = i
                    break
            assert ptcval is not None

            if ('R', vtrX, Y) not in PTCPTC:
                PTCPTC[('R', vtrX, Y)] = set()
            PTCPTC[('R', vtrX, Y)].add(ptcval)

            NODESNODESNODES += """<node id="{}" type="CHANX" direction="INC_DIR" capacity="1">
    <loc xlow="{}" ylow="{}" xhigh="{}" yhigh="{}" ptc="{}"/>
    <segment segment_id="0"/>
</node>
""".format(nodeidx, vtrX, Y, vtrX, Y, ptcval)

# local interconnect for top/bottom IOs
for X in range(2, 8):
    for (myY, vtrY) in [(0, 1), (5, 4)]:
        for I in range(10):
            nodeidx = len(node_id_to_thing_map)
            vtrX = X - (1 if I < 5 else 0)

            node_id_to_thing_map.append(('LOCAL_INTERCONNECT', X, myY, I))
            thing_to_node_id_map[('LOCAL_INTERCONNECT', X, myY, I)] = nodeidx

            ptcval = None
            for i in range(76):
                usedindices = PTCPTC.get(('U', vtrX, vtrY), [])
                if i not in usedindices:
                    ptcval = i
                    break
            assert ptcval is not None

            if ('U', vtrX, vtrY) not in PTCPTC:
                PTCPTC[('U', vtrX, vtrY)] = set()
            PTCPTC[('U', vtrX, vtrY)].add(ptcval)

            NODESNODESNODES += """<node id="{}" type="CHANY" direction="INC_DIR" capacity="1">
    <loc xlow="{}" ylow="{}" xhigh="{}" yhigh="{}" ptc="{}"/>
    <segment segment_id="0"/>
</node>
""".format(nodeidx, vtrX, vtrY, vtrX, vtrY, ptcval)

assert len(node_id_to_thing_map) == len(thing_to_node_id_map)
for i in range(len(node_id_to_thing_map)):
    print("Node {} is {}".format(i, node_id_to_thing_map[i]))

# print(NODESNODESNODES)

def parse_xyi(inp):
    xpos = inp.find('X')
    ypos = inp.find('Y')
    ipos = inp.find('I')

    assert xpos >= 0
    assert ypos > xpos
    assert ipos > ypos

    return (int(inp[xpos + 1:ypos]), int(inp[ypos + 1:ipos]), int(inp[ipos + 1:]))

def parse_xysi(inp):
    xpos = inp.find('X')
    ypos = inp.find('Y')
    spos = inp.find('S')
    ipos = inp.find('I')

    assert xpos >= 0
    assert ypos > xpos
    assert spos > ypos
    assert ipos > spos

    sval = int(inp[spos + 1:ipos])
    assert sval == 0

    return (int(inp[xpos + 1:ypos]), int(inp[ypos + 1:spos]), int(inp[ipos + 1:]))

def parse_xysi2(inp):
    xpos = inp.find('X')
    ypos = inp.find('Y')
    spos = inp.find('S')
    ipos = inp.find('I')

    assert xpos >= 0
    assert ypos > xpos
    assert spos > ypos
    assert ipos > spos

    return (int(inp[xpos + 1:ypos]), int(inp[ypos + 1:spos]), int(inp[spos + 1:ipos]), int(inp[ipos + 1:]))

def parse_thing(node):
    ret = None
    if node.startswith("R:"):
        x, y, i = parse_xyi(node[2:])
        ret = ('R', x, y, i)
    if node.startswith("L:"):
        x, y, i = parse_xyi(node[2:])
        ret = ('L', x, y, i)
    if node.startswith("L2:"):
        x, y, i = parse_xyi(node[3:])
        ret = ('L2', x, y, i)
    if node.startswith("U:"):
        x, y, i = parse_xyi(node[2:])
        ret = ('U', x, y, i)
    if node.startswith("D:"):
        x, y, i = parse_xyi(node[2:])
        ret = ('D', x, y, i)
    if node.startswith("LE_BUFFER:"):
        x, y, i = parse_xysi(node[10:])
        ret =  ('LE_BUFFER', x, y, i)
    if node.startswith("LOCAL_INTERCONNECT:"):
        x, y, i = parse_xysi(node[19:])
        ret =  ('LOCAL_INTERCONNECT', x, y, i)
    if node.startswith("IO_DATAIN:"):
        x, y, s, _ = parse_xysi2(node[10:])
        # XXX naming things
        ret = ('IO_DATAOUT', x, y, s)

    if ret is None:
        return None
    if ret not in thing_to_node_id_map:
        print(ret)
    assert ret in thing_to_node_id_map
    return thing_to_node_id_map[ret]

EDGESEDGESEDGES = ''

for dstnode, srcnodes in interconnectinterconnect.items():
    for srcnode in srcnodes:
        srcthing = parse_thing(srcnode)
        dstthing = parse_thing(dstnode)

        if srcthing is not None and dstthing is not None:
            # print("{} -> {}".format(srcnode, dstnode))
            EDGESEDGESEDGES += '<edge src_node="{}" sink_node="{}" switch_id="0"/>\n'.format(srcthing, dstthing)
        else:
            print("SKIPPED {} -> {}".format(srcnode, dstnode))

# IO local interconnect to output
for X in [1, 8]:
    for Y in range(1, 5):
        for outI in range(5):
            for llI in range(18):
                EDGESEDGESEDGES += '<edge src_node="{}" sink_node="{}" switch_id="0"/>\n'.format(
                    thing_to_node_id_map[('LOCAL_INTERCONNECT', X, Y, llI)],
                    thing_to_node_id_map[('IO_DATAIN', X, Y, outI)])
                EDGESEDGESEDGES += '<edge src_node="{}" sink_node="{}" switch_id="0"/>\n'.format(
                    thing_to_node_id_map[('LOCAL_INTERCONNECT', X, Y, llI)],
                    thing_to_node_id_map[('OE', X, Y, outI)])
for X in range(2, 8):
    for Y in [0, 5]:
        for outI in range(4):
            for llI in range(10):
                EDGESEDGESEDGES += '<edge src_node="{}" sink_node="{}" switch_id="0"/>\n'.format(
                    thing_to_node_id_map[('LOCAL_INTERCONNECT', X, Y, llI)],
                    thing_to_node_id_map[('IO_DATAIN', X, Y, outI)])
                EDGESEDGESEDGES += '<edge src_node="{}" sink_node="{}" switch_id="0"/>\n'.format(
                    thing_to_node_id_map[('LOCAL_INTERCONNECT', X, Y, llI)],
                    thing_to_node_id_map[('OE', X, Y, outI)])

# top/bottom to connections
Y = 5
for X in range(2, 8):
    for pinI in range(4):
        for outI in [[4, 2, 0, 9, 7, 5], [0, 3, 5, 8], [1, 2, 6, 7], [1, 3, 4, 6, 8, 9]][pinI]:
            EDGESEDGESEDGES += '<edge src_node="{}" sink_node="{}" switch_id="0"/>\n'.format(
                thing_to_node_id_map[('IO_DATAOUT', X, Y, pinI)],
                thing_to_node_id_map[('D', X, Y, outI)])
Y = 0
for X in range(2, 8):
    for pinI in range(4):
        for outI in [[4, 2, 0, 9, 7, 5], [1, 4, 6, 9], [2, 3, 7, 8], [0, 1, 3, 5, 6, 8]][pinI]:
            EDGESEDGESEDGES += '<edge src_node="{}" sink_node="{}" switch_id="0"/>\n'.format(
                thing_to_node_id_map[('IO_DATAOUT', X, Y, pinI)],
                thing_to_node_id_map[('U', X, Y, outI)])

with open('rrgraph.xml', 'r') as f:
    lines = f.readlines()

with open('rrgraph-newnew.xml', 'w') as f:
    for l in lines:
        f.write(l)
        if "~+~+~+ PUT CHANNELS HERE +~+~+~" in l:
            f.write(NODESNODESNODES)
        if "~+~+~+ PUT EDGES HERE +~+~+~" in l:
            f.write(EDGESEDGESEDGES)


with open('rrgraph-construction-node-to-thing-map.json', 'w') as f:
    json.dump(node_id_to_thing_map, f)

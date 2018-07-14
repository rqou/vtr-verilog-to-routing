import json
import sys
import xml.etree.ElementTree as ET

with open('rrgraph-construction-node-to-thing-map.json', 'r') as f:
    node_id_to_thing_map = json.load(f)

# print(node_id_to_thing_map)

netfn = sys.argv[1]
placefn = sys.argv[2]
routefn = sys.argv[3]
jsonfn = sys.argv[4]

################# THIS PART READS YOSYS JSON

def expandlut(width, bits):
    assert width >= 1 and width <= 4

    if width == 4:
        return bits
    if width == 3:
        return bits | (bits << 8)
    if width == 2:
        return bits | (bits << 4) | (bits << 8) | (bits << 12)
    if width == 1:
        return (bits | (bits << 1) | (bits << 2) | (bits << 31) |
                (bits << 4) | (bits << 5) | (bits << 6) | (bits << 7) |
                (bits << 8) | (bits << 9) | (bits << 10) | (bits << 11) |
                (bits << 12) | (bits << 13) | (bits << 14) | (bits << 15))

with open(jsonfn, 'r') as f:
    yosysjson = json.load(f)

# print(yosysjson)
mainmod = None
for _, module in yosysjson['modules'].items():
    if module['attributes'].get('top', 0):
        assert mainmod is None
        mainmod = module
assert mainmod is not None
# print(mainmod)

# Just want the mask and width, index by output wire
lutlutlut = {}
for _, cell in mainmod['cells'].items():
    if cell['type'] == '$lut':
        # print(cell)
        width = cell['parameters']['WIDTH']
        bits = cell['parameters']['LUT']
        outwire = cell['connections']['Y'][0]

        # print(width, bits, outwire)
        assert outwire not in lutlutlut
        lutlutlut[outwire] = expandlut(width, bits)

# print(lutlutlut)

netnamenetname = {}
for name, obj in mainmod['netnames'].items():
    # print(name, obj)
    assert len(obj['bits']) == 1
    assert name not in netnamenetname
    netnamenetname[name] = obj['bits'][0]

# print(netnamenetname)

################ THIS PART READS PLACE

placeplaceplace = {}
with open(placefn, 'r') as f:
    # skip this header or whatever
    f.readline()
    f.readline()

    while True:
        l = f.readline()
        if not l:
            break

        l = l.strip()
        if not l or l.startswith("#"):
            continue

        # print(l)
        block_name, x, y, i, _ = l.split()
        placeplaceplace[block_name] = (x, y, i)

# print(placeplaceplace)

OUTOUTOUT = ''

def encode_thing(thing):
    if thing[0] == "R" or thing[0] == "L" or thing[0] == "U" or thing[0] == "D" or thing[0] == "L2":
        return "{}:X{}Y{}I{}".format(thing[0], thing[1], thing[2], thing[3])
    if thing[0] == "IO_DATAOUT":
        return "IO_DATAIN:X{}Y{}S{}I0".format(thing[1], thing[2], thing[3])
    if thing[0] == "IO_DATAIN":
        return "IO_DATAOUT:X{}Y{}S{}I0".format(thing[1], thing[2], thing[3])
    if thing[0] == "LOCAL_INTERCONNECT":
        return "LOCAL_INTERCONNECT:X{}Y{}S0I{}".format(thing[1], thing[2], thing[3])
    if thing[0] == "LE_BUFFER":
        return "LE_BUFFER:X{}Y{}S0I{}".format(thing[1], thing[2], thing[3])
    assert False

######################## THIS PART READS ROUTE

last_node = None
with open(routefn, 'r') as f:
    while True:
        l = f.readline()
        if not l:
            break
        # print(l)

        l = l.strip()
        if l.startswith("Node:"):
            if last_node != None:
                last_node_split = last_node.split()
                this_node_split = l.split()
                last_node_idx = last_node_split[1]
                this_node_idx = this_node_split[1]
                last_node_kind = last_node_split[2]
                this_node_kind = this_node_split[2]

                if last_node_kind != "SOURCE" and this_node_kind != "SOURCE" and last_node_kind != "SINK" and this_node_kind != "SINK":
                    # print("{} ({})-> {} ({})".format(last_node_idx, last_node_kind, this_node_idx, this_node_kind))

                    last_node_thing = node_id_to_thing_map[int(last_node_idx)]
                    this_node_thing = node_id_to_thing_map[int(this_node_idx)]

                    # print("{} -> {}".format(last_node_thing, this_node_thing))

                    encoded_src = encode_thing(last_node_thing)
                    encoded_dst = encode_thing(this_node_thing)

                    OUTOUTOUT += "{} -> {}\n".format(encoded_src, encoded_dst)

            last_node = l

################## THIS PART READS NET


def shufflelut(origbits, rotdata):
    rotdata = rotdata.split()
    rotdata = [4 if x == 'open' else int(x) for x in rotdata]
    rotdatainv = {}
    for i in range(4):
        rotdatainv[rotdata[i]] = i
    # print(rotdata, rotdatainv)

    def findorig(x, b0new, b1new, b2new, b3new):
        if x not in rotdatainv:
            return False
        return [b0new, b1new, b2new, b3new][rotdatainv[x]]

    # print(rotdata)

    newbits = 0

    for i in range(16):
        b0new = bool(i & 1)
        b1new = bool(i & 2)
        b2new = bool(i & 4)
        b3new = bool(i & 8)

        # print(b3new, b2new, b1new, b0new)

        b0orig = findorig(0, b0new, b1new, b2new, b3new)
        b1orig = findorig(1, b0new, b1new, b2new, b3new)
        b2orig = findorig(2, b0new, b1new, b2new, b3new)
        b3orig = findorig(3, b0new, b1new, b2new, b3new)

        # print(b3orig, b2orig, b1orig, b0orig)

        oldbitinlut = bool(origbits & (1 << (b3orig * 8 + b2orig * 4 + b1orig * 2 + b0orig)))
        if oldbitinlut:
            newbits |= 1 << i

    # print("{:016b} {:016b}".format(origbits, newbits))

    return newbits

netroot = ET.parse(netfn).getroot()
# print(netroot)

for node in netroot:
    if node.tag == "block":
        if node.attrib['instance'].startswith('lab'):
            # print('LAB {}'.format(node.attrib['name']))
            labloc = placeplaceplace[node.attrib['name']]
            labnode = node
            # print(labloc)
            for node in labnode:
                if node.tag == "outputs":
                    for node in node:
                        if node.attrib['name'] == 'lab_outputs':
                            labouts = node.text.split()
                            # print(labouts)
                            for lebufferi in range(20):
                                if labouts[lebufferi] != open:
                                    # print(labouts[lebufferi])
                                    if "combout" in labouts[lebufferi]:
                                        OUTOUTOUT += "COMBOUT -> LE_BUFFER:X{}Y{}S0I{}\n".format(labloc[0], labloc[1], lebufferi)
                                    else:
                                        ...
            for node in labnode:
                if node.tag == "block" and node.attrib['instance'].startswith('lut'):
                    # print(node.attrib['instance'])
                    # print(node.attrib['instance'].startswith('lut'))

                    lutidx = node.attrib['instance'][4]
                    # print(lutidx)
                    lutnode = node

                    for node in lutnode:
                        if node.tag == "inputs":
                            for node in node:
                                # print(node.attrib)
                                inpname = node.attrib['name']
                                # print(inpname)
                                if inpname == "dataa" or inpname == "datab" or inpname == "datac" or inpname == "datad":
                                    inpval = node.text
                                    if inpval != "open":
                                        # print(inpname, inpval)
                                        # TODO: datac/datad special cases
                                        assert inpval.startswith('lab.lab_line')
                                        inpval = inpval[13:].split(']')[0]
                                        # print(inpval)
                                        OUTOUTOUT += "LOCAL_INTERCONNECT:X{}Y{}S0I{} -> LUT{}:{}\n".format(
                                            labloc[0], labloc[1], inpval, lutidx, inpname.upper())
                                elif inpname == "cin":
                                    ...
                                elif inpname == "inverta":
                                    ...
                                else:
                                    assert False
                        if node.tag == "block":
                            lutname = node.attrib['name']
                            lutbits = lutlutlut[netnamenetname[lutname]]
                            # print(lutname, lutbits)

                            rotdata = node.find('block').find('inputs').find('port_rotation_map').text
                            # print(rotdata)

                            rotlutbits = shufflelut(lutbits, rotdata)

                            OUTOUTOUT += "LUTBITS:X{}Y{}N{} = {:16b}\n".format(labloc[0], labloc[1], lutidx, rotlutbits)

        elif node.attrib['instance'].startswith('row_io_tile') or node.attrib['instance'].startswith('col_io_tile'):
            # print('IO {}'.format(node.attrib['name']))
            loc = placeplaceplace[node.attrib['name']]
            # print(loc)

            if node.attrib['mode'] == 'blif_simple_out':
                OUTOUTOUT += "IO_TILE:X{}Y{}I{}:INVERTOUT = false\n".format(loc[0], loc[1], loc[2])
            elif node.attrib['mode'] == 'blif_simple_in':
                OUTOUTOUT += "IO_TILE:X{}Y{}I{}:ENABLEIBUF = true\n".format(loc[0], loc[1], loc[2])
                OUTOUTOUT += "IO_TILE:X{}Y{}I{}:INVERTOE = true\n".format(loc[0], loc[1], loc[2])
            else:
                assert False
        else:
            assert False
        # print(node.attrib)

print(OUTOUTOUT)

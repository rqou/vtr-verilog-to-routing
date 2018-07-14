import json
import sys
import xml.etree.ElementTree as ET

with open('rrgraph-construction-node-to-thing-map.json', 'r') as f:
    node_id_to_thing_map = json.load(f)

# print(node_id_to_thing_map)

netfn = sys.argv[1]
placefn = sys.argv[2]
routefn = sys.argv[3]

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

print(placeplaceplace)

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
netroot = ET.parse(netfn).getroot()
# print(netroot)

for node in netroot:
    if node.tag == "block":
        if node.attrib['instance'].startswith('lab'):
            print('LAB {}'.format(node.attrib['name']))
        elif node.attrib['instance'].startswith('row_io_tile') or node.attrib['instance'].startswith('col_io_tile'):
            print('IO {}'.format(node.attrib['name']))
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

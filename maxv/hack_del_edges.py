import re

with open('rrgraph-newnew-wtf.xml', 'r') as f:
    lines = f.readlines()

rere = re.compile('\t\t<edge src_node="([0-9]+)" sink_node="([0-9]+)" switch_id="."/>')

with open('rrgraph-out.xml', 'w') as f:
    for l in lines:
        if not "<edge src_node" in l:
            f.write(l)
        else:
            matches = rere.match(l)
            if matches is None:
                print(l)
            assert matches is not None
            src_node = int(matches[1])
            sink_node = int(matches[2])
            # print(src_node, sink_node)
            if src_node <= 3095 and sink_node <= 3095:
                f.write(l)

def has_overlaps(p1, p2):

    dict_list = []
    
    for i in range(3):
        dict_sublist = []
        for j in range(6):
            dict_sublist.append(dict())
        dict_list.append(dict_sublist)
    
    for c1 in p1:
        for c2 in p2:
            for idx, i in enumerate(c1):
                for jdx, j in enumerate(c2):
                    
                    if i - j not in dict_list[idx][jdx]:
                        dict_list[idx][jdx][i - j] = 0
                        
                    if i + j not in dict_list[idx][jdx + 3]:
                        dict_list[idx][jdx+3][i + j] = 0                    

                    dict_list[idx][jdx][i - j] += 1
                    dict_list[idx][jdx+3][i + j] += 1

    count = -1       
    index_0 = -1
    offset_0 = -1
    for i, d in enumerate(dict_list[0]):
        for k in d:
            
            if d[k] > 11 and d[k] > count:
                count = d[k]
                index_0 = i
                offset_0 = k
              
    count = -1
    index_1 = -1
    offset_1 = -1
    for i, d in enumerate(dict_list[1]):
        for k in d:
            
            if d[k] >= 11 and d[k] > count:
                count = d[k]
                index_1 = i
                offset_1 = k
                
    count = -1
    index_2 = -1
    offset_2 = -1
    for i, d in enumerate(dict_list[2]):
        for k in d:
            
            if d[k] >= 11 and d[k] > count:
                count = d[k]
                index_2 = i
                offset_2 = k
                    
    return ((offset_0, index_0), (offset_1, index_1), (offset_2, index_2))          
   
def get_manhatten_distance(p1, p2):
    return (p1[0] - p2[0]) + (p1[1] - p2[1]) + (p1[2] - p2[2])         
        

# Open input and read as lines
f = open('input.txt', 'r')
lines = f.read().split('\n')

probes = []

probe = set()

for l in lines:
    if not l:
        probes.append(probe)
        continue
    
    if l[-1] == '-':
        probe = set()
        continue
    
    probe.add(tuple([int(i) for i in l.split(',')]))
    
concatonated_nodes = [0]

offsets = dict()

discovered = [0]
undiscovered = [i for i in range(1, len(probes))]
checked = set()

mappings = dict()

while len(mappings) < len(probes) - 1:
    for d in discovered:
        for u in undiscovered:
            
            if (d, u) in checked:
                continue
            
            dists = has_overlaps(probes[d], probes[u])
            checked.add((d, u))
            
            if dists[0][0] == -1 or dists[1][0] == -1 or dists[2][0] == -1:
                continue
            
            mappings[u] = ((d, dists))
            undiscovered.remove(u)
            discovered.append(u)


scannerlocations = [(0, 0, 0)]

for k in mappings:
    
    if k == 0:
        continue
    
    beacons = probes[k]
    transformed_beacons = set()
    
    target = -1
    origin = k
    scannerlocation = [0, 0, 0]
    while target != 0:
        target = mappings[origin][0]
        instructions = mappings[origin][1]
        
        for idx, i in enumerate(instructions):
            
            if target == 0:
                scannerlocation[idx] += instructions[idx][0]
                continue
            
            if abs(mappings[target][1][idx][1] - mappings[origin][1][mappings[target][1][idx][1] % 3][1]) < 2:
                scannerlocation[idx] -= instructions[mappings[target][1][idx][1] % 3][0]
            else:
                scannerlocation[idx] += instructions[mappings[target][1][idx][1] % 3][0]
            
            """
            if mappings[target][1][idx][1] > 2:
                scannerlocation[idx] -= instructions[mappings[target][1][idx][1] - 3][0]
            else:
                scannerlocation[idx] += instructions[mappings[target][1][idx][1]][0]
            """
            """
            if instructions[idx][1] > 2:
                scannerlocation[idx] = instructions[instructions[idx][1] - 3][0] - scannerlocation[idx]
            else:
                scannerlocation[idx] += instructions[instructions[idx][1]][0]
            """
            
        for b in beacons:
            probe = [0,0,0]
            for j, c in enumerate(b):
                if instructions[j][1] > 2 :
                    probe[j] = instructions[j][0] - b[instructions[j][1] - 3]
                else:
                    probe[j] = b[instructions[j][1]] + instructions[j][0]
        
            if probe[0] == 2:
                print(probe[0])
        
            transformed_beacons.add((probe[0], probe[1], probe[2]))
        
        origin = target
        beacons = transformed_beacons.copy()
        transformed_beacons = set()
        
    scannerlocations.append((scannerlocation[0], scannerlocation[1], scannerlocation[2]))
    probes[0].update(beacons)

print(len(probes[0]))                
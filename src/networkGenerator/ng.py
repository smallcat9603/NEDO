'''
Created on 2017/04/10

@author: smallcat
'''
#network generator

import algorithm
import tp
import datetime
import networkx as nx
import matplotlib.pyplot as plt

traffic_pattern = tp.traffic_pattern
degree = tp.degree 
nodes = tp.nodes  #number of nodes
sw = 1  #total number of switches
sw_bp = 1 #number of switches before each partition
sw_node = {}  #nodes connected to a switch
sw_sw = {}  #switches connected to a switch

partition = True

#Initialize
sw_node[0] = []
for i in range(nodes):
    sw_node[0].append(i)
sw_sw[0] = []

starttime = datetime.datetime.now()
print "begin"
print "sw_node: " + str(sw_node)
print "sw_sw: " + str(sw_sw)
print "=============================================== partition start ==============================================="

# min_nodes_per_sw = 1
while partition:
    for i in range(sw_bp):
        if len(sw_node[i]) + len(sw_sw[i]) > degree and len(sw_node[i])/2 > 0:
#             print "   " + str(i)
#             print len(sw_node[i])
#             print len(sw_sw[i])
            sw_sw[sw] = []
            sw_sw[i].append(sw)  #append switch connection 
            sw_sw[sw].append(i)  #append switch connection            
            for c_sw in sw_sw[i]:  #append connected switches
                if c_sw != sw and len(sw_sw[c_sw]) + len(sw_node[c_sw]) < degree:
                    sw_sw[c_sw].append(sw)  
                    sw_sw[sw].append(c_sw)
            sw_node[sw] = []  
            if len(sw_sw[i]) >= degree-1:  #avoid len(sw_sw[i]) >= degree
                for x in range(len(sw_node[i])-1):
                    sw_node[sw].append(sw_node[i].pop())
            else:
                for x in range(len(sw_node[i])/2):
                    sw_node[sw].append(sw_node[i].pop())
            sw = sw + 1
        if i == sw_bp - 1 and sw_bp == sw:
            partition = False
    sw_bp = sw
    #print sw_bp
    
print "finally"                
print "sw_node: " + str(sw_node)
print "sw_sw: " + str(sw_sw)
print "number of switches: " + str(len(sw_sw))

c = 0
for i in range(len(sw_sw)):
    d = len(sw_sw[i])+len(sw_node[i])-degree
    if d > 0:
        c = c + 1
print "design constraint: ", str(c)

# fn = "node_" + str(nodes) + "_degree_" + str(degree) + "_time_" + str(datetime.datetime.now()).replace(" ", "-").replace(".", "-").replace(":", "-") + str(".txt")
# f = open(fn, "w")
# for i in range(len(sw_sw)):
#     f.write(str(i) + "    ")
#     for j in range(len(sw_sw[i])):
#         f.write(str(sw_sw[i][j]) + "    ")
#     f.write("\n")
# f.close()
# G=nx.read_adjlist(fn)
# nx.draw(G, node_size=80)
# #nx.draw(G, node_size=30, with_labels=True)  
# #nx.draw_networkx_nodes(RG,pos,nodelist=nodelist,node_color='b')
# plt.show()

topo = algorithm.get_topo(sw_sw)

#print "topo: " + str(topo)

edges = algorithm.get_edges(topo)    

# print "=== Dijkstra ==="  
# length,Shortest_path = algorithm.dijkstra(edges, 2, 5)  
# print 'length = ', length  
# print 'The shortest path is ', Shortest_path

# count = 0
# total = 0
# for i in range(len(topo)):  
#     for j in range(len(topo[0])):  
#         if i!=j: 
#             length, Shortest_path = algorithm.dijkstra(edges, i, j)
#             total += length
#             count = count + 1
# avg = (float)(total)/count
# print "average hops: ", str(avg)

# erase = 0
# for i in range(len(sw_sw)):
#     dis = len(sw_sw[i])+len(sw_node[i])-degree
#     if dis > 0:
#         for j in range(dis):
#             sw_sw[i].pop()
#         erase = erase + 1
# print "erase: ", str(erase)    
# print "sw_sw (erased): ", str(sw_sw)

data = tp.data
num_dataflow = len(data)
src_dst = {}
for i in range(num_dataflow):
    src_dst[i] = (data["src"][i], data["dst"][i])
src_dst_sw = algorithm.get_src_dst_sw(src_dst, sw_node)
print "src_dst: ", str(src_dst)
print "src_dst_sw: ", str(src_dst_sw)

slot_num, total, max_hops, routes = algorithm.get_slot_num(edges, src_dst, src_dst_sw)    
slots, congestion, avg = algorithm.print_result(routes, total, src_dst_sw, slot_num)

# print "=============================================== node_swap start ==============================================="
# 
# node_switch, dataflow = algorithm.get_node_switch(routes, congestion)
# print "node_switch: ", str(node_switch)
# 
# import copy  
# node_switch_improve = []
# node_switch_improve.append(sw_node)         
# for ns in node_switch:
#     sw_node_switch = copy.deepcopy(sw_node) 
#     for i in range(len(sw_node_switch)):
#         if ns[0] in sw_node_switch[i] and ns[1] not in sw_node_switch[i]:
#             sw_node_switch[i].remove(ns[0])
#             sw_node_switch[i].append(ns[1])
#         elif ns[1] in sw_node_switch[i] and ns[0] not in sw_node_switch[i]:
#             sw_node_switch[i].remove(ns[1])
#             sw_node_switch[i].append(ns[0])   
#     print "sw_node after node switch: ", str(sw_node_switch)           
#     src_dst_sw_switch = algorithm.get_src_dst_sw(src_dst, sw_node_switch)
#     print "src_dst_sw after node switch: ", str(src_dst_sw_switch)    
#     slot_num_switch, total_switch, routes_switch = algorithm.get_slot_num(edges, src_dst, src_dst_sw_switch)    
#     print "routes after node switch: ", routes_switch
#     avg_switch = (float)(total_switch)/len(src_dst_sw_switch)
#     print "average hops after node switch: ", str(avg_switch)
#     slots_switch = max(slot_num_switch.values())
#     print "max number of slots after node switch: ", str(slots_switch)
#     print "links with max number of slots after node switch:",
#     congestion_switch = []
#     for i in slot_num_switch.keys():
#         if slot_num_switch[i] == slots_switch:
#             congestion_switch.append(i)   
#     print congestion_switch  
# #     if ns == (1, 11): #todo
# #         sw_node = copy.deepcopy(sw_node_switch) 
# #         print "node switch because # of slots is reduced"
# #         break
#     if slots_switch <= slots:
#         node_switch_improve.append(sw_node_switch)
# print "node_switch_improve: ", str(node_switch_improve)
# 
# slots_min = slots
# winner = sw_node
# for item in node_switch_improve:
#     sw_node_ = copy.deepcopy(item)
#     sw_sw_ = copy.deepcopy(sw_sw)
#     edges_ = copy.deepcopy(edges)
#     slots, avg, sws, links = algorithm.optimize_links(sw_sw_, sw_node_, degree, edges_, src_dst)
#     if slots < slots_min:
#         slots_min = slots
#         winner = sw_node_
# print "slots_min: ", str(slots_min)       
# sw_node = winner 
# print "sw_node winner: ", str(sw_node)
# 
# slots, avg, sws, links = algorithm.optimize_links(sw_sw, sw_node, degree, edges, src_dst)
# print "=============================================== results ==============================================="
# print "MS: ", str(slots)
# print "average hops: ", str(avg)
# print "number of switches: ", str(sws)
# print "number of links: ", str(links)

print "=============================================== link_add start ==============================================="        
sw_sw, added_links = algorithm.get_update_sw_sw(sw_sw, sw_node, degree, edges)
print "added_links: ", str(added_links)
print "sw_sw (renewed): ", str(sw_sw)      
topo = algorithm.get_topo(sw_sw)
edges = algorithm.get_edges(topo) 
# src_dst_sw = algorithm.get_src_dst_sw(src_dst, sw_node)
# print "src_dst: ", str(src_dst)
# print "src_dst_sw: ", str(src_dst_sw)   
slot_num, total, max_hops, routes = algorithm.get_slot_num(edges, src_dst, src_dst_sw)    
slots, congestion, avg = algorithm.print_result(routes, total, src_dst_sw, slot_num)     

print "=============================================== node_swap start ==============================================="         
node_switch, dataflow = algorithm.get_node_switch(routes, congestion)
print "node_switch: ", str(node_switch)
import copy
current_slots = slots
node_switch_improve = []
sw_node_before = sw_node
node_switch_improve.append(sw_node_before)         
for ns in node_switch:
    sw_node_switch = copy.deepcopy(sw_node_before) 
    for i in range(len(sw_node_switch)):
        if ns[0] in sw_node_switch[i] and ns[1] not in sw_node_switch[i]:
            sw_node_switch[i].remove(ns[0])
            sw_node_switch[i].append(ns[1])
        elif ns[1] in sw_node_switch[i] and ns[0] not in sw_node_switch[i]:
            sw_node_switch[i].remove(ns[1])
            sw_node_switch[i].append(ns[0])   
    print "sw_node after node switch: ", str(sw_node_switch)           
    src_dst_sw_switch = algorithm.get_src_dst_sw(src_dst, sw_node_switch)
    print "src_dst_sw after node switch: ", str(src_dst_sw_switch)    
    slot_num_switch, total_switch, max_hops_switch, routes_switch = algorithm.get_slot_num(edges, src_dst, src_dst_sw_switch)    
    slots_switch, congestion_switch, avg_switch = algorithm.print_result(routes_switch, total_switch, src_dst_sw_switch, slot_num_switch)
#     print "routes after node switch: ", routes_switch
#     avg_switch = (float)(total_switch)/len(src_dst_sw_switch)
#     print "average hops after node switch: ", str(avg_switch)
#     slots_switch = max(slot_num_switch.values())
#     print "max number of slots after node switch: ", str(slots_switch)
#     print "links with max number of slots after node switch:",
#     congestion_switch = []
#     for i in slot_num_switch.keys():
#         if slot_num_switch[i] == slots_switch:
#             congestion_switch.append(i)   
#     print congestion_switch  
#     if ns == (1, 11): #todo
#         sw_node = copy.deepcopy(sw_node_switch) 
#         print "node switch because # of slots is reduced"
#         break
    if slots_switch <= current_slots:
        node_switch_improve.append(sw_node_switch)
        
        print "=============================================== indirect_parallel start after node_switch ", str(ns), "===============================================" 
        node_switch, dataflow_switch = algorithm.get_node_switch(routes_switch, congestion_switch)
        slot_num_switch, total_switch, routes_switch = algorithm.replace_indirect_parallel_path(added_links, slots_switch, dataflow_switch, sw_sw, slot_num_switch, total_switch, routes_switch)                    
        slots_switch, congestion_switch, avg_switch = algorithm.print_result(routes_switch, total_switch, src_dst_sw_switch, slot_num_switch)
        if slots_switch < slots:
            slots = slots_switch
            avg = avg_switch
            
            slot_num = slot_num_switch
            total = total_switch
            max_hops = max_hops_switch
            routes = routes_switch
            congestion = congestion_switch
            
            sw_node = sw_node_switch

print "=============================================== indirect_parallel end ==============================================="  
print "node_switch_improve: ", str(node_switch_improve)
#algorithm.print_result(routes, total, src_dst_sw_switch, slot_num)
print "routes: ", str(routes)
print "max number of slots: ", str(slots)
print "average switch hops: ", str(avg)
print "sw_node: ", str(sw_node)       
print "sw_sw: ", str(sw_sw)
print "slot_num: ", str(slot_num)
print "number of switches: ", str(len(sw_sw))
links = 0
for item in sw_sw.values():
    links = links + len(item)
links = links/2
print "number of links: ", str(links)
endtime = datetime.datetime.now()
print "simulation time: ", (endtime-starttime).microseconds

# print "=============================================== indirect_parallel start ===============================================" 
# node_switch, dataflow = algorithm.get_node_switch(routes, congestion)
# slot_num, total, routes = algorithm.replace_indirect_parallel_path(added_links, slots, dataflow, sw_sw, slot_num, total, routes)                    
# slots, congestion = algorithm.print_result(routes, total, src_dst_sw, slot_num)

loop = True
while loop:
#     slots_before = slots
    print "=============================================== bypass_path start ==============================================="
    print "routes (before): ", routes
    diverted_paths = []
    for c in congestion:
        cfound = False
        for i in range(len(routes)):
    #         if len(sw_sw[routes[i][1]]) + len(sw_node[routes[i][1]]) < degree and len(sw_sw[routes[i][-2]]) + len(sw_node[routes[i][-2]]) < degree:
            for r in range(1, len(routes[i])-2):
                if c == (routes[i][r], routes[i][r+1]):
                    diverted_paths.append(i)
                    cfound = True
                    break
            if cfound == True:
                break
    diverted_paths = list(set(diverted_paths))
    print "diverted_paths: ", diverted_paths
#     if sw in sw_sw and sw+1 in sw_sw and sw in sw_node and sw+1 in sw_node:
#         if (len(sw_sw[sw]) + len(sw_node[sw]) > degree - 1 or len(sw_sw[sw+1]) + len(sw_node[sw+1]) > degree - 1) or ((sw, sw+1) in slot_num and slot_num[(sw, sw+1)] > slots-2):
#             sw = sw + 2
#             sw_sw[sw] = []       
#             sw_node[sw] = []   
#             sw_sw[sw+1] = []       
#             sw_node[sw+1] = []  
#             sw_sw[sw].append(sw+1)
#             sw_sw[sw+1].append(sw)            
#     else:        
    if sw not in sw_sw and sw+1 not in sw_sw and sw not in sw_node and sw+1 not in sw_node:
        sw_sw[sw] = []       
        sw_node[sw] = []   
        sw_sw[sw+1] = []       
        sw_node[sw+1] = []  
        sw_sw[sw].append(sw+1)
        sw_sw[sw+1].append(sw)
    for dp in diverted_paths:            
    #     for i in range(1, len(routes[dp])-2):
        for i in range(0, len(routes[dp])-1):
            slot_num[(routes[dp][i], routes[dp][i+1])] = slot_num[(routes[dp][i], routes[dp][i+1])] - 1    
    #     if len(sw_sw[sw]) > degree -2:
#         if (len(sw_sw[sw]) + len(sw_node[sw]) > degree - 1 or len(sw_sw[sw+1]) + len(sw_node[sw+1]) > degree - 1) or slot_num[(sw, sw+1)] > slots_before-1:
#     #         sw = sw + 1
#             sw = sw + 2
#             sw_sw[sw] = [] 
#             sw_node[sw] = []  
#             sw_sw[sw+1] = []       
#             sw_node[sw+1] = []  
#             sw_sw[sw].append(sw+1)
#             sw_sw[sw+1].append(sw) 

        if routes[dp][1] not in sw_sw[sw]:    
            sw_sw[sw].append(routes[dp][1]) 
            sw_sw[routes[dp][1]].append(sw)
        if routes[dp][-2] not in sw_sw[sw+1]:    
            sw_sw[sw+1].append(routes[dp][-2]) 
            sw_sw[routes[dp][-2]].append(sw+1) 
        if routes[dp][0]-10000 in sw_node[routes[dp][1]]:
            sw_node[routes[dp][1]].remove(routes[dp][0]-10000) 
        if routes[dp][-1]-10000 in sw_node[routes[dp][-2]]:    
            sw_node[routes[dp][-2]].remove(routes[dp][-1]-10000) 
    
        if routes[dp][0]-10000 not in sw_node[sw]:    
            sw_node[sw].append(routes[dp][0]-10000) 
        if routes[dp][-1]-10000 not in sw_node[sw+1]:    
            sw_node[sw+1].append(routes[dp][-1]-10000)    
    #     if sw not in sw_sw[routes[dp][1]]:    
    #         sw_sw[routes[dp][1]].append(sw)
    #     if routes[dp][1] not in sw_sw[sw]:
    #         sw_sw[sw].append(routes[dp][1])
    #     if sw not in sw_sw[routes[dp][-2]]:    
    #         sw_sw[routes[dp][-2]].append(sw)
    #     if routes[dp][-2] not in sw_sw[sw]:
    #         sw_sw[sw].append(routes[dp][-2])
    #     if (routes[dp][1], sw) not in slot_num:
    #         slot_num[(routes[dp][1], sw)] = 1
    #     else:
    #         slot_num[(routes[dp][1], sw)] = slot_num[(routes[dp][1], sw)] + 1    
    #     if (sw, routes[dp][-2]) not in slot_num:
    #         slot_num[(sw, routes[dp][-2])] = 1
    #     else:
    #         slot_num[(sw, routes[dp][-2])] = slot_num[(sw, routes[dp][-2])] + 1         
        if (routes[dp][0], sw) not in slot_num:
            slot_num[(routes[dp][0], sw)] = 1
        else:
            slot_num[(routes[dp][0], sw)] = slot_num[(routes[dp][0], sw)] + 1
        if (sw, sw+1) not in slot_num:
            slot_num[(sw, sw+1)] = 1
        else:
            slot_num[(sw, sw+1)] = slot_num[(sw, sw+1)] + 1    
        if (sw+1, routes[dp][-1]) not in slot_num:
            slot_num[(sw+1, routes[dp][-1])] = 1
        else:
            slot_num[(sw+1, routes[dp][-1])] = slot_num[(sw+1, routes[dp][-1])] + 1             
        hc_before = len(routes[dp])
    #     routes[dp] = [routes[dp][0], routes[dp][1], sw, routes[dp][-2], routes[dp][-1]]
        routes[dp] = [routes[dp][0], sw, sw+1, routes[dp][-1]]
        hc_after = len(routes[dp])
        total = total - hc_before + hc_after
        avg = (float)(total)/len(src_dst)
        if hc_after - hc_before > max_hops:
            max_hops = hc_after - hc_before
        slots = max(slot_num.values())
        #print slot_num
        
        if slots == tp.MS:
            loop = False
            break
        
        if (len(sw_sw[sw]) + len(sw_node[sw]) > degree - 1 or len(sw_sw[sw+1]) + len(sw_node[sw+1]) > degree - 1) or slot_num[(sw, sw+1)] > slots-2:
            sw = sw + 2
            sw_sw[sw] = []       
            sw_node[sw] = []   
            sw_sw[sw+1] = []       
            sw_node[sw+1] = []  
            sw_sw[sw].append(sw+1)
            sw_sw[sw+1].append(sw)        
    print "routes (after): ", routes
    
    congestion = []
    for i in slot_num.keys():
        if slot_num[i] == slots:
            congestion.append(i)    
    
#     if slots >= slots_before:
#         slots = slots_before
#         loop = False

#huyao 171023
num_max = 0
for i in slot_num.values():
    if i == slots:
        num_max = num_max + 1        

print "=============================================== results ==============================================="
# algorithm.print_result(routes, total, src_dst_sw_switch, slot_num)
print "slot_num:", slot_num
print "sw_node: ", sw_node
print "sw_sw: ", sw_sw
print "MS: ", str(slots)
print "num_max: ", str(num_max), " / ", str(len(slot_num))
print "average hops: ", str(avg)
print "max hops: ", str(max_hops)
print "number of switches: ", str(len(sw_sw))
links = 0
for item in sw_sw.values():
    links = links + len(item)
links = links/2
print "number of links: ", str(links)
#endtime = datetime.datetime.now()
print "simulation time: ", (endtime-starttime).microseconds

print "=============================================== draw graph ==============================================="
fn = "node_" + str(nodes) + "_degree_" + str(degree) + "_time_" + str(datetime.datetime.now()).replace(" ", "-").replace(".", "-").replace(":", "-") + str(".txt")
f = open(fn, "w")
for i in range(len(sw_sw)):
    f.write(str(i) + "    ")
    for j in range(len(sw_sw[i])):
        f.write(str(sw_sw[i][j]) + "    ")
    f.write("\n")
f.close()
G=nx.read_adjlist(fn)
nx.draw(G, node_size=80)
#nx.draw(G, node_size=30, with_labels=True)  
#nx.draw_networkx_nodes(RG,pos,nodelist=nodelist,node_color='b')
plt.show()
     
            
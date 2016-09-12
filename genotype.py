
#!/usr/bin/python3
from __future__ import print_function
import numpy as np 
from collections import Counter

'''
scaffold_0	177878	.	G	A	3.64	.	DP=679;VDB=6.080000e-02;RPB=7.415572e-01;AF1=0.006496;AC1=2;DP4=469,205,1,1;MQ=42;FQ=3.66;PV4=0.52,0.12,1,0.27	GT:PL:DP:SP:GQ	0/0:0,9,102:3:0:30	0/0:0,15,143:5:0:36	0/0:0,0,0:0:0:21	0/0:0,39,255:13:0:60	0/0:0,0,0:0:0:21	0/0:0,42,255:14:0:63	0/0:0,45,255:15:0:66	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,21,165:7:0:42	0/0:0,6,74:2:0:27	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,30,254:10:0:51	0/0:0,6,75:2:0:27	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,6,74:2:0:27	0/0:0,0,0:0:0:21	0/0:0,12,125:4:0:33	0/0:0,9,102:3:0:30	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,18,155:6:0:39	0/0:0,0,0:0:0:21     0/0:0,0,0:0:0:21	0/0:0,3,40:1:0:24	0/0:0,27,183:9:0:48	0/0:0,36,255:12:0:57	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,9,102:3:0:30	0/0:0,21,171:7:0:42	0/0:0,148,255:49:0:99	0/0:0,27,249:9:0:48	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,6,67:2:0:27	0/0:0,24,176:8:0:45	0/0:0,3,40:1:0:24	0/0:0,0,0:0:0:21	0/0:0,9,100:3:0:30   0/0:0,0,0:0:0:21	0/0:0,18,157:6:0:39	0/0:0,0,0:0:0:21	0/0:0,3,41:1:0:24	0/0:0,0,0:0:0:21	0/0:0,6,75:2:0:27	0/0:0,54,255:18:0:75	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,9,101:3:0:30	0/0:0,3,27:1:0:24	0/0:0,18,162:6:0:39	0/0:0,24,232:8:0:45	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,51,255:17:0:72	0/0:0,6,75:2:0:27	0/0:0,0,0:0:0:21	0/0:0,99,255:33:0:99 0/0:0,63,255:21:0:84	0/0:0,3,41:1:0:24	0/0:0,27,254:9:0:48	0/0:0,166,255:55:0:99	0/0:0,30,239:10:0:51	0/0:0,12,142:4:0:33	0/1:50,0,151:7:0:29	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,24,234:8:0:45	0/0:0,30,255:10:0:51	0/0:0,15,142:5:0:36	0/0:0,12,119:4:0:33	0/0:0,15,129:5:0:36	0/0:0,24,241:8:0:45	0/0:0,51,255:17:0:72	0/0:0,33,255:11:0:54	0/0:0,81,255:27:0:99	0/0:0,9,99:3:0:30	0/0:0,123,255:41:0:99	0/0:0,0,0:0:0:21	0/0:0,51,255:17:0:72	0/0:0,93,255:31:0:99	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,9,96:3:0:30	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,18,187:6:0:39	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,12,138:4:0:33  0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,6,75:2:0:27	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,3,37:1:0:24	0/0:0,21,218:7:0:42	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,3,41:1:0:24	0/0:0,6,71:2:0:27	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,3,41:1:0:24	0/0:0,0,0:0:0:21     0/0:0,9,102:3:0:30	0/0:0,3,39:1:0:24	0/0:0,9,101:3:0:30	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,9,102:3:0:30	0/0:0,12,124:4:0:33	0/0:0,9,98:3:0:30	0/0:0,0,0:0:0:21	0/0:0,3,41:1:0:24	0/0:0,0,0:0:0:21	0/0:0,3,40:1:0:24	0/0:0,0,0:0:0:21	0/0:0,9,102:3:0:30	0/0:0,0,0:0:0:21	0/0:0,12,133:4:0:33	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,12,115:4:0:33	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,0,0:0:0:21	0/0:0,12,123:4:0:33	0/0:0,0,0:0:0:21
'''


import sys

## sample label dic

file_gbs_label = 'gbs_lable.txt'
o        = open(file_gbs_label).readlines()
key      = [x.strip().split('\t')[0] for x in o]
value    = [x.strip().split('\t')[1] for x in o]
dicLabel = dict(zip(key,value))




n_pop = 177
Outfile = open('all.gt.label.txt','w')
for line in sys.stdin:
        if line[0:6] == '#CHROM':
                samples       = [x.split('/')[0].split('.')[0] for x in line.strip().split('\t')[9:]]   # ../81ea/mapped/TN1512L0433_CTAGC.sorted.bam
                parent_A1 = samples.index('TN1508L0713_CTCC')
                parent_A2 = samples.index('TN1512L0433_CTCC')
                parent_A3 = samples.index('TN1512L0433_TAGGCCAT')
                parent_B1 = samples.index('TN1512L0433_TGCA')
                parent_B2 = samples.index('TN1512L0433_CCGGATAT')
                parent_B3 = samples.index('TN1508L0713_TGCA')
                print(parent_A1,parent_A2,parent_A3,parent_B1,parent_B2,parent_B3) 
                continue 
        elif line[0] == '#' or line.strip() == '':
                continue
        cell = line.strip().split('\t')
        strS = cell[0]
        strL = cell[1]
        strRef = cell[3]
        strVar = cell[4].split(',')[0]
        strQ = cell[5]
        if 'INDEL' == cell[7][0:5]:
                continue
        infolist = cell[7].split(';')
        dicInfo = dict(zip([x.split('=')[0] for x in infolist],[x.split('=')[1] for x in infolist]))
        keylist = cell[8].split(':')
        GT_list = []
        for acc in cell[9:]:
                vallist = acc.split(':')
                dic = dict(zip(keylist,vallist))
                if int(dicInfo['DP']) > 100:
                        if dic['GT'] == '1/1':
                                GT = strRef
                        elif dic['GT'] == '0/1':
                                GT = 'H'
                        elif dic['GT'] == '0/0':
                                GT = strVar
                        else:
                                print('!',dic['GT'])
                                exit()
                else : 
                        GT = 'N'
                GT_list.append(GT)
        ## Genotype matrix construction except parents call, all parent repeat should be consistent each other.
        parent_A = Counter([GT_list[parent_A1], GT_list[parent_A2], GT_list[parent_A3]])
        parent_B = Counter([GT_list[parent_B1], GT_list[parent_B2], GT_list[parent_B3]])
        if max(parent_A.values()) > 1 and max(parent_B.values()) > 1:
                parent_A_GT = parent_A.keys()[np.argmax(parent_A.values())]
                parent_B_GT = parent_B.keys()[np.argmax(parent_B.values())]
                if parent_A_GT == parent_B_GT:
                        continue # same genotype between parents skip 
                if 'H' in [parent_A_GT,parent_B_GT]:
                        continue # hetero in parents genotype skip 
        else:
                a         = Counter(GT_list)
                base_list = a.keys() 
                base_list.sort(key=lambda x : a[x], reverse=True)
                if 'N' not in base_list[0:2] and 'H' not in base_list[0:2]:
                        if max(parent_A.values()) > 1:
                                parent_A_GT = parent_A.keys()[np.argmax(parent_A.values())]
                                parent_B_GT = list(set(base_list[0:2]) - set([parent_A_GT]))[0]
                        elif max(parent_B.values()) > 1:
                                parent_B_GT = parent_B.keys()[np.argmax(parent_B.values())]
                                parent_A_GT = list(set(base_list[0:2]) - set([parent_B_GT]))[0]
                else:
                        continue 
        if len(GT_list) != n_pop:
                print(line,GT_list)
                exit()
       
        GT_list_noParent      = []
        sample_list           = []
        for n,each in enumerate(GT_list):
                if n in [parent_A1,parent_A2,parent_A3,parent_B1,parent_B2,parent_B3]:
                        continue
                GT_list_noParent.append(each)
                sample_list.append(samples[n])
        ## end
        sample_list_rename = [dicLabel[x] for x in sample_list]
       
        

        if len(GT_list_noParent) != 171:
                print('sample number error')
                exit()
        GT_list_noParent = np.array(GT_list_noParent)
        GT_list_noParent[GT_list_noParent == parent_A_GT] = 'a'
        GT_list_noParent[GT_list_noParent == parent_B_GT] = 'b'
        GT_list_noParent[GT_list_noParent == 'H'] = 'h'
        GT_list_noParent[GT_list_noParent == 'N'] = '-'

        allele      = Counter(GT_list_noParent)
        if len(set(allele.keys()) - set(['a','h','b','-'])) > 0 : 
                print (parent_A_GT,parent_B_GT,set(allele.keys()))
                continue # genotypes that are different with parent may removed. 
        #print(strS,strL,strRef,parent_A_GT,parent_B_GT,GT_list_noParent)
        num_a       = allele['a']
        num_b       = allele['b']
        if num_a + num_b == 0:
                print(parent_A_GT,parent_B_GT,allele,GT_list_noParent)
                continue
        minor_freq  = float(min(num_a,num_b))/(num_a + num_b) 
        if len(allele.keys()) < 2:
                continue
        elif float(allele['-'])/sum(allele.values()) > 0.3: # percentage of N
		
                continue
        elif float(allele['h'])/sum(allele.values()) > 0.1:
                continue
        elif minor_freq < 0.1: # Minor allele freq
                continue
        else:
                print(strS,strL,strRef,parent_A_GT,parent_B_GT,','.join(GT_list_noParent),sep='\t',file=Outfile)
        
print(','.join(sample_list_rename),sep='\t',file=Outfile)

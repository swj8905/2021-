data = "0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	189	190	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	143	247	153	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	136	247	242	86	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	192	252	187	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	62	185	18	0	0	0	0	89	236	217	47	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	216	253	60	0	0	0	0	212	255	81	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	206	252	68	0	0	0	48	242	253	89	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	131	251	212	21	0	0	11	167	252	197	5	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	29	232	247	63	0	0	0	153	252	226	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	45	219	252	143	0	0	0	116	249	252	103	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	4	96	253	255	253	200	122	7	25	201	250	158	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	92	252	252	253	217	252	252	200	227	252	231	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	87	251	247	231	65	48	189	252	252	253	252	251	227	35	0	0	0	0	0	0	0	0	0	0	0	0	0	0	190	221	98	0	0	0	42	196	252	253	252	252	162	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	111	29	0	0	0	0	62	239	252	86	42	42	14	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	15	148	253	218	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	121	252	231	28	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	31	221	251	129	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	218	252	160	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	122	252	82	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0"
data = data.split()

cnt = 0
for i in data:
    print("{:3}".format(i), end=" ")
    cnt += 1
    if cnt % 28 == 0:
        print()
import pandas as pd 

f = open('monojet_Zp2000.0_DM_50.0_chan3.csv', 'r+')
f2 = open('final_data.csv', 'w')

for line in f:
  line = line.replace(";", ",")
  b = line[:-2]
  c = b.split(',')
  indices = [i for i, x in enumerate(c) if x == 'j']
  empty_str = ""
  for index in indices:
    particle_info = c[index+1:index+5]
    particle_info = ','.join(particle_info)
    particle_info += '\n'
    f2.write(particle_info)
f.close()
f2.close()
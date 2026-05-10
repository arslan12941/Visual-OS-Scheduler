import numpy as np

input_path = input("Enter File Path/Name : ")
file = open(input_path, "r")
data = []
for line in file:
    endl = line.find('\n')
    if endl != -1 :
        line = line[:endl]
    data.append(line)
file.close()
pnum = data[0]
mu_ariv , sig_ariv = data[1].split(' ')
mu_run , sig_run = data[2].split(' ')
lmda = data[3]
pnum = int(pnum)
mu_ariv , sig_ariv = float(mu_ariv) , float(sig_ariv)
mu_run , sig_run = float(mu_run ) , float(sig_run)
lmda = float(lmda)


arrival_time = np.random.normal(mu_ariv, sig_ariv, pnum)
run_time = np.random.normal(mu_run,sig_run, pnum)
priority = np.random.poisson(lmda, pnum)
file = open('output.txt', "w")
for i in range (pnum):
    file.write(str(i+1)+" "+str(arrival_time[i])+" "+str(run_time[i])+" "+str(priority[i])+'\n')
file.close()
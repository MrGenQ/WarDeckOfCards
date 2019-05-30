count=0
f=open('winners.txt','r')
player=f.readlines()
for line in player:
    if counter_n_1 in line:
        count=count+1
print(count)
f.close()

#python counter reikia importuotis
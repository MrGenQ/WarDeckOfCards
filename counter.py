
def counter():
        '''A function to count how many times a specific word occurs in a text'''
        count=0
        
        for line in player:
                if player_name in line:
                        count += 1
        return count
        
f=open('winners.txt','r')
player=f.readlines()
should_continue = 'yes'

while should_continue != 'no' and should_continue == 'yes':
        player_name = input("Please select which player's win count you want to know: ")
        counted = counter()
        print("player ", player_name, "won ", counted, " times")
        should_continue = input("Do you wish to check another player? type: 'yes' or 'no' ")
        if_true = True
        while if_true == True:
                if should_continue == 'yes':
                        pass
                elif should_continue =='no':
                        pass
                else:
                        print ("Selected wrong command, try again")
                        should_continue = input("Do you wish to check another player? type: 'yes' or 'no' ")  
                if_true = False     

f.close()
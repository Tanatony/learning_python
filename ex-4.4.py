command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

#beat string
command1 = command1.strip().split()
command2 = command2.strip().split()

command1 = command1[-1].split(',')
command2 = command2[-1].split(',')

list1 = list(command1)
ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'


output = '\n{:25} {}' * 6

# Первый вариант: использование срезов
route = ospf_route.split()

print(output.format('Protocol:', 'OSPF',
                    'Prefix:', route[1],
                    'AD/Metric:', route[2][1:-1],
                    'Next-Hop:', route[4][:-1],
                    'Last update:', route[5][:-1],
                    'Outbound Interface:', route[6]))

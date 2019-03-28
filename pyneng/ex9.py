#items = [1, 2, 3]

#print('One: {}, Two: {}, Three: {}'.format(*items))


def config_interface(intf_name, ip_address, cidr_mask):
    interface = 'interface {}'
    no_shut = 'no shutdown'
    ip_addr = 'ip address {} {}'
    result = []
    result.append(interface.format(intf_name))
    result.append(no_shut)

    mask_bits = int(cidr_mask.split('/')[-1])
    bin_mask = '1' * mask_bits + '0' * (32 - mask_bits)
    dec_mask = [str(int(bin_mask[i:i + 8], 2)) for i in range(0, 25, 8)]
    dec_mask_str = '.'.join(dec_mask)

    result.append(ip_addr.format(ip_address, dec_mask_str))
    return result

config_interface("Fa0/1", '10.1.1.1', '/25')
config_interface('Fa0/3', '10.0.0.1', '/18')
config_interface('Fa0/3', '10.0.0.1', '/32')
config_interface('Fa0/3', '10.0.0.1', '/30')
config_interface('Fa0/3', '10.0.0.1', '30')

interfaces_info = [['Fa0/1', '10.0.1.1', '/24'],
                   ['Fa0/2', '10.0.2.1', '/24'],
                   ['Fa0/3', '10.0.3.1', '/24'],
                   ['Fa0/4', '10.0.4.1', '/24'],
                   ['Lo0', '10.0.0.1', '/32']]

print('#' * 10)

for info in interfaces_info:
    print(config_interface(*info))

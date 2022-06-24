def int32_to_ip(int32):
    ip_list = []
    for n in range(3, -1, -1):
        ip_list.append(int32 // 256 ** n)
        int32 -= (int32 // 256 ** n) * (256 ** n)
    return f'{ip_list[0]}.{ip_list[1]}.{ip_list[2]}.{ip_list[3]}'

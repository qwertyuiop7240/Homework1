def domain_name(url):
    # A loop for splitting URLs into basic blocks
    part_url = url
    for i in ['//', '@']:
        part_url = part_url.partition(i)
        if part_url[-1] == '':
            part_url = part_url[0]
        else:
            part_url = part_url[-1]
    part_url = part_url.partition('/')[0]

    # Domain name parsing
    part_url = part_url.partition('.')
    last_part1, last_part2 = part_url[0], part_url[-1]
    if any((
            last_part1 == 'www',
            last_part1 == 'ru',
            last_part1 == 'app',
            last_part1 == 'ww3',
    )):
        dname = last_part2.partition('.')[0]
    else:
        dname = last_part1.partition('.')[0]

    return dname

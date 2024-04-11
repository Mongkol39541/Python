"""Netflix"""
 
def stanmium(screen, package):
    """Netflix"""
    package['time'] = screen // package['screens']
    screen -= package['screens'] * package['time']
    return screen, package
 
def main():
    """Netflix"""
    req = {
        'screens': int(input()),
        'downloads': int(input()),
        'unlimited': input(),
        'mobile': input(),
        'laptop': input(),
        'hd': input(),
        'ultrahd': input()
    }
    mobile = {
        'name': 'Mobile',
        'price': 99,
        'screens': 1,
        'time': 0,
    }
    basic = {
        'name': 'Basic',
        'price': 279,
        'screens': 1,
        'time': 0,
    }
    standard = {
        'name': 'Standard',
        'price': 349,
        'screens': 2,
        'time': 0,
    }
    premium = {
        'name': 'Premium',
        'price': 419,
        'screens': 4,
        'time': 0,
    }
    screen = max(req['screens'], req['downloads'])
    selects = [mobile]
    if req['ultrahd'] == "Yes":
        selects = [premium]
    elif req['hd'] == "Yes":
        selects = [standard, premium]
    elif req['laptop'] == "Yes":
        selects = [basic, standard, premium]
    packages = []
    for package in selects[::-1]:
        screen, package = stanmium(screen, package)
        packages.append(package)
    if screen > 0:
        for index in range(len(packages)):
            if packages[index]['name'] == selects[0]['name'] and len(packages) != 2:
                packages[index]['time'] += 1
            elif packages[index]['name'] == selects[0]['name'] and len(packages) == 2:
                if packages[index]['time'] == 0:
                    packages[index]['time'] += 1
                    continue
                packages[index]['time'] -= 1
                packages[index - 1]['time'] += 1
    if screen == 0 and len(packages) == 3 and packages[1]['time'] == 1 and packages[2]['time'] == 1:
        packages[0]['time'] = 1
        packages[1]['time'] = 0
        packages[2]['time'] = 0
    total = 0
    for package in packages:
        if package['time'] != 0:
            print("{0} x {1}".format(package['name'], package['time']))
            total += package['price'] * package['time']
    print('Total = {0} THB'.format(total))
main()
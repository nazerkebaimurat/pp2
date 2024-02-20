import json

with open('sample-data.json') as file:
    data = json.load(file)

print("Inerface status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-"*80)

for interface in data['imdata']:
    dn = interface['topSystem']['attributes']['dn']
    description = interface['interfaceEntity']['attributes']['descr']
    speed = interface['interfaceEntity']['attributes'].get('speeed', 'inherit')
    mtu = interface['interfaceEntity']['attributes'].get('mtu', 'inherit')
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
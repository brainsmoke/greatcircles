from math import cos, sin, radians

designator_cache = {}
def get_designator(s):
    n = designator_cache.get(s, 0)+1
    designator_cache[s] = n
    return s+str(n)

types = {
    "WS2812B-V5/W" : { 'sym':'D', 'footprint':'LED-4_L5.0-W5.0-P3.30-LS5.4', 'lcsc':'C2874885' }

}

cx=42.767612
cy=131.68451
dy=15
r=120
angles=[-9, 9]

centers = [ [cx, cy+i*dy] for i in range(7) ]

leds = []

for cx,cy in centers:
    for a in angles:
        t = "WS2812B-V5/W"
        sym = types[t]['sym']
        p = [cx + r*sin(radians(a)), cy - r*cos(radians(a))]
        leds.append( { 'type': t, 'd': get_designator(sym), 'pos':p, 'angle':a,  'side':"top"} )
        leds.append( { 'type': t, 'd': get_designator(sym), 'pos':p, 'angle':-a, 'side':"bottom"} )

def bomfile(components):
    print ('"Comment","Designator","Footprint","JLCPCB Part #"')
    distinct_types = set( c['type'] for c in components )
    for t in distinct_types:
        dlist = ','.join(c['d'] for c in components if c['type'] == t)
        print (f'"{t}","{dlist}","{types[t]["footprint"]},"{types[t]["lcsc"]}"')

def posfile(components):
    print('"Designator","Val","Package","Mid X","Mid Y","Rotation","Layer"')
    for c in components:
        d, t = c["d"], c["type"]
        x, y, a, side = c['pos'][0], c['pos'][1], c['angle'], c["side"]
        fp = types[t]["footprint"]
        print (f'"{d}","{t}","{fp}","{x}","{-y}","{180-a}","{side}"')

if __name__ == '__main__':
    import sys
    if sys.argv[1] == 'bom':
        bomfile(leds)
    if sys.argv[1] == 'top':
        posfile(l for l in leds if l['side'] == 'top')
    if sys.argv[1] == 'bottom':
        posfile(l for l in leds if l['side'] == 'bottom')
    if sys.argv[1] == 'pos':
        posfile(leds)


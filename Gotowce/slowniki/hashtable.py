class hashnode:
    def __init__(self):
        self.key = None
        self.val = None
        self.state = 0


def insert(hashtable, x, val):   #indeksowanie otwarte - adresowanie pojedyncze
    n = len(hashtable)
    h = hash(x) % n

    i = 0
    while i < n and hashtable[h].state == 1:
        h += 1
        h = h % n
        i += 1

    hashtable[h].key = x
    hashtable[h].val = val
    hashtable[h].state = 1

def rem(hashtable, x):
    n = len(hashtable)
    h = hash(x) % n

    i = 0
    while i < n\
        and (hashtable[h].state == 2
            or (hashtable[h].state==1 and hashtable[h].key != key) ):
        h = (h+1) % n
        i += 1

    if (i == n):
        return
    hashtable[h].state = 2

def get(hashtable, x):
    n = len(hashtable)
    h = hash(x) % n

    i = 0
    while i < n and \
            (hashtable[h].state == 2
            or (hashtable[h].state==1 and hashtable[h].key != key) ):
        h = (h+1) % n
        i += 1

    if hashtable[h].key == key:
        return hashtable[h].val
    else:
        return None


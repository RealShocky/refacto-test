def p(d, t='mean'):
    """process data"""
    if not d or not isinstance(d, list):
        return None
    
    if t == 'mean':
        s = sum(d)
        l = len(d)
        return s/l if l > 0 else None
    elif t == 'median':
        if len(d) == 0:
            return None
        sd = sorted(d)
        n = len(sd)
        if n % 2 == 0:
            return (sd[n//2-1] + sd[n//2])/2
        else:
            return sd[n//2]
    elif t == 'mode':
        if len(d) == 0:
            return None
        from collections import Counter
        c = Counter(d)
        return c.most_common(1)[0][0]
    else:
        return None

def f(fname):
    """read file"""
    try:
        d = []
        with open(fname, 'r') as f:
            for l in f:
                try:
                    d.append(float(l.strip()))
                except:
                    continue
        return d
    except:
        return None

def s(d, fname):
    """save data"""
    if not d:
        return False
    try:
        with open(fname, 'w') as f:
            for x in d:
                f.write(str(x) + '\n')
        return True
    except:
        return False

def tr(d, op):
    """transform data"""
    if not d or not isinstance(d, list):
        return None
    
    r = []
    if op == 'sqrt':
        for x in d:
            try:
                import math
                r.append(math.sqrt(x))
            except:
                continue
    elif op == 'square':
        for x in d:
            try:
                r.append(x * x)
            except:
                continue
    elif op == 'log':
        for x in d:
            try:
                import math
                r.append(math.log(x))
            except:
                continue
    return r if r else None

def fl(d, c):
    """filter data"""
    if not d or not isinstance(d, list):
        return None
    
    r = []
    try:
        for x in d:
            if eval(f"x {c}"):
                r.append(x)
    except:
        return None
    return r if r else None

# Example usage
data = [1, 2, 3, 4, 5]
print(p(data, 'mean'))  # Calculate mean
print(p(data, 'median'))  # Calculate median
print(p(data, 'mode'))  # Calculate mode

transformed = tr(data, 'sqrt')  # Transform using square root
filtered = fl(transformed, "> 1.5")  # Filter values greater than 1.5

s(filtered, 'output.txt')  # Save to file
loaded = f('output.txt')  # Load from file

xs = input()
ys = input()
times = input()
start = 0
stop = 1
targets = 0
time_passed = 0

for item in range(0,len(xs)):
    x = xs[start:stop:1]
    for n in x:
        str_x = "".join(str(n))
    str_x = int(str_x)
    
    y = ys[start:stop:1]
    for n in y:
        str_y = "".join(str(n))
    str_y = int(str_y)
    
    t = times[start:stop:1]
    for n in t:
        str_t = "".join(str(n))
    str_t = int(str_t)
    
    seconds = int(str_t - time_passed)    
    time_passed = int(str_t)
    
    
    y_abs = abs(str_y - str_t)
    x_abs = abs(str_x - str_t)
    
    if y_abs > seconds and x_abs > seconds:
        targets += 0
    else:
        targets += 1
if targets == len(times):
    targets = int(-1)
   
    start = start + 1
    stop = stop + 1

print targets

    

    


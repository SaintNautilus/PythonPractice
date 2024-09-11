
test = [1, 1, 0, 1, 1, 1]

currentcount = 0
maximumcount = 0

for i in test:
    if i == 1:
        currentcount = currentcount + 1 
    elif i == 0:
        if currentcount > maximumcount:
            maximumcount = currentcount
            currentcount = 0

if currentcount > maximumcount:
    maximumcount = currentcount
    
print(maximumcount)

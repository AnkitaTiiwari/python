#we're counting who brought what and total things

guest = {
        "alice" : {"Banaa" : 1, "Apple" : 3},
        "mona" : {"Banaa" : 1, "Apple" : 3},
        "Rona" : {"Banaa" : 1, "Apple" : 3},
        "Dhone" : {"Banaa" : 1, "Apple" : 3}

}
total_banaa = 0
total_apple = 0
for k,v in guest.items():
    for key,val in v.items():
        print(k + "is bringing " + str(val) + " " + key)
        if key == "Banaa":
            total_banaa += val
        elif key == "Apple":
            total_apple += val

print("Total Banaa: " + str(total_banaa))
print("Total Apple: " + str(total_apple))
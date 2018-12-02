from time import sleep
import os

lvlp = "CustomSongs/" + input("Please provide path to level folder (use /):\t.../CustomSongs/")
print("Working...")
f = None
try:
    f = open(lvlp+"/info.json","r")
except FileNotFoundError:
    print("FileNotFoundError:  Level does not exist!")
    sleep(1)
    quit()
info_list = f.read().split('"')
if info_list[info_list.index("environmentName")+2] != "NiceEnvironment":
    if input("It looks like the environment of this level is not the NiceEnvironment.  Do you still want to proceed (y/n)?\t").lower() != y:
        quit()
for dif in ("Easy","Normal","Hard","Expert","ExpertPlus"):
    try:
        f = open(lvlp+"/"+dif+".json","r")
        switcht2 = list()
        switcht3 = list()
        data_list = f.read().split('"')
        final_data_tw = str()
        offseti = data_list.index("_events")
        toofar = data_list.index("_notes")
        
        try:
            while offseti < toofar:
                offseti = data_list.index("_type",offseti,toofar) + 1
                
                if data_list[offseti] == ":2,":
                    switcht3.append(offseti)
                elif data_list[offseti] == ":3,":
                    switcht2.append(offseti)
        
        except ValueError:
            pass
        
        for i in switcht2:
            data_list[i] = ":2,"
        for i in switcht3:
            data_list[i] = ":3,"
        
        f.close()
        os.remove(lvlp+"/"+dif+".json")
        f = open(lvlp+"/"+dif+".json","w")
        for i in range(len(data_list)):
            final_data_tw += data_list[i]
            if i != len(data_list) - 1:
                final_data_tw += '"'
        f.write(final_data_tw)
        
        f.close()
    
    except FileNotFoundError:
        pass

print("Done!")
sleep(1)

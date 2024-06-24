def Find_ph():
    ph_val=int(input("Enter ph value between 0 to 14:"))
    if ph_val>=0 and ph_val<7:
        print("ph_val", ph_val,"is acidic")
    if ph_val==7:
        print("ph_val",ph_val,"is neutral")
    if ph_val>7 and ph_val<=14:
        print("ph_val",ph_val,"is basic")
    if ph_val>14:
        print("wrong inut")
Find_ph()
        

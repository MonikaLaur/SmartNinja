is_waiting = True
has_time = False

if is_waiting:
    print "I am waiting"
    print "I am still waiting"  # everything that is indented belongs to if function
elif not is_waiting and has_time:
    print "I am not waiting and have time"
else: # if if function is not true then do this
    print "I am not waiting"
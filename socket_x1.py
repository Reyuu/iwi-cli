import sys, socket, random, string, time
execfile("configirc.ini")

readbuffer = ""
stateTrueLoop = True
onChannelMsg = 'PRIVMSG %s :' % (CHAN)

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((HOST, PORT))
irc.send("NICK %s\r\n" % NICK)
irc.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
time.sleep(5)
irc.send("JOIN %s\r\n" % (CHAN))
irc.settimeout(TIMEOUTTIME)

while stateTrueLoop == True:
    try:
        readbuffer = irc.recv(1024)
    except:
        readbuffer = ""
    temp = string.split(readbuffer, "\n")
    for line in temp:
        try:
            line = string.rstrip(line)
            line = string.split(line)

            if(line[0] == "PING"):
                irc.send("PONG %s\r\n" % line[1])
                print "Pinged and ponged"
            print ' '.join(line)  # putting this at end of try;except clause because it
            #  crashes on empty lines
        except:
            pass
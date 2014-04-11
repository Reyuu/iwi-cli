if counter == 0:
    self.sendMsg(CHAN, "Loaded "+PLUGINFILE)
    counter += 1
else:
    pass

if message[0] == '!':
    commandMsg = (message.split(' ')[0])
    argMsg = (message.split(' ')[1:])
    if len(message.split(' ')) > 1:
        argMsg2 = (message.split(' ')[1])
    else:
        argMsg2 = ''
    if len(message.split(' ')) > 2:
        argMsg3 = (message.split(' ')[2])
    else:
        argMsg3 = ''
    if len(message.split(' ')) > 3:
        argMsg4 = (message.split(' ')[3:])
    else:
        argMsg4 = ''
    if len(message.split(' ')) > 1:
        argMsgAll = (message.split(' '))[1:]
    else:
        argMsgAll = ''
    if(commandMsg == "!help" and argMsg2 == "all" and username in MASTERS):
        x1 = "|----------------Actuall commands:--------------------|"
        x2 = "|!roll big - rolls a big integer----------------------|"
        x3 = "|!roll small - rolls small integer--------------------|"
        x4 = "|!kick <nick> - kicks <nick>--------------------------|"
        x5 = "|!mode <mode> <nick> - gives <mode> to nick (only op)-|"
        x6 = "|!say <something> - bot says <something>--------------|"
        x7 = "|!losuj <1stitem>, <2nditem>... - returns random item-|"
        x8 = "|!quit now - shutdown bot-----------------------------|"
        x9 = "If command has only one word, remember to add \"null\" at the end!"
        for item in (x1, x2, x3, x4, x5, x6, x7, x8, x9):
            self.sendMsg(CHAN, item)
    else:
        pass

    if(commandMsg == "!roll"):
        if(argMsg2 == "big"):
            x1 = int(strftime("%S", gmtime()))
            x2 = int(strftime("%Y", gmtime()))
            x = random.randint(1, x1*x2)
            self.sendMsg(CHAN, username+" rolled "+str(x))
        elif(argMsg2 == "small"):
            x1 = int(strftime("%S", gmtime()))
            x = random.randint(1, x1)
            self.sendMsg(CHAN, username+" rolled "+str(x))
        else:
            try:
                argMsg2 = int(argMsg2)
                x = random.randint(1, argMsg2)
                self.sendMsg(CHAN, username+" rolled "+str(x))

            except ValueError:
                pass

    if(commandMsg == "!kick" or commandMsg == "!kill" and username in MASTERS):
        sayMsg = ' '.join(argMsg4)
        x = argMsg3+" "+sayMsg
        x2 = ' :Inappropriate conversation'
        if x == ' ':
            self.send("KICK "+CHAN+" "+argMsg2+x2)
        else:
            self.send("KICK "+CHAN+" "+argMsg2+" :"+x)
    else:
        pass

    if(commandMsg == "!mode" and username is TrueMaster):
        sayMsg = ' '.join(argMsg)[:]
        self.send(sayMsg)
    else:
        pass

    if(commandMsg == "!say" and username in MASTERS):
        sayMsg = ' '.join(argMsg)
        self.sendMsg(CHAN, sayMsg)
    else:
        pass

    if(commandMsg == "!quit" and argMsg2 == "now" and argMsg3 == '' and username in MASTERS):
        self.sendMsg(CHAN, "Bye")
        import os
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()
        os._exit(1)
    else:
        pass

    if(commandMsg == "!print" and argMsg2 == "MASTERS" and username in MASTERS):
        self.sendMsg(CHAN, 'My masters are '+', '.join(MASTERS)[:]+'. I love them soo much. <3')
    else:
        pass

    if(commandMsg == "!losuj"):
        sayMsg = ' '.join(argMsg)
        y = random.choice(sayMsg.split(', '))
        self.sendMsg(CHAN, y)
    else:
        pass

    if(commandMsg == "!vs"):
        sayMsg = ''.join(argMsgAll)
        y = random.choice(sayMsg.split(' vs '))
        yu = y[0].upper()+y[1:]
        self.sendMsg(CHAN, yu+" is better!")
    else:
        pass

    if(commandMsg == "!rss" and argMsg2 == "tokyotosho"):
        if(argMsg3 == ''):
            rssURL = 'http://tokyotosho.info/rss.php?filter=1'
            feedrss = feedparser.parse(rssURL)
            for i in range(0, 5):
                titlerss = u"05"+feedrss.entries[i].title
                self.sendMsg(CHAN, titlerss.encode('utf-8'))
        if(argMsg3 == 'links'):
            rssURL = 'http://tokyotosho.info/rss.php?filter=1'
            feedrss = feedparser.parse(rssURL)
            for i in range(0, 5):
                titlerss = u"05"+feedrss.entries[i].title+u" Link: 03"+feedrss.entries[0].link
                self.sendMsg(CHAN, titlerss.encode('utf-8'))
    else:
        pass

    '''if(commandMsg == "!faq"):
        self.send(values_dict[str(argMsg2)])
    else:
        pass'''

    if (commandMsg == "!raw"):
        sayMsg = ' '.join(argMsg)[:]
        self.send(sayMsg)
    else:
        pass

    if (commandMsg == "!exec" and username is TrueMaster):
        sayMsg = ' '.join(argMsg)
        exec(sayMsg)
    else:
        pass

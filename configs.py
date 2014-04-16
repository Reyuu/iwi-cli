import sys
import ConfigParser
import argparse
def fetchSettings():
    config = ConfigParser.ConfigParser()
    config.read('configirc.ini')
    try:
        global HOST, PORT, NICK, IDENT, REALNAME, CHAN, TIMEOUTTIME, PING, PLUGINFILE, MASTERS, counter, TrueMaster, NoticeMsgOnChannelJoin, NoticeMsgOnChannelJoinOn, HighLight
        HOST = config.get('Server', 'Server')
        PORT = int(config.get('Server', 'Port'))
        CHAN = config.get('Server', 'Channel')

        NICK = config.get('Bot', 'Nick')
        IDENT = config.get('Bot', 'Ident')
        REALNAME = config.get('Bot', 'RealName')

        NoticeMsgOnChannelJoin = config.get('Messages', 'WelcomeMsg')
        NoticeMsgOnChannelJoinOn = config.get('Messages', 'WelcomeMsgActive')
        PING = config.get('Messages', 'OutputPing')
        HighLight = config.get('Messages', 'HighlightPhrases').split(',')

        TIMEOUTTIME = float(config.get('Settings', 'SocketDelay'))
        PLUGINFILE = config.get('Settings', 'PluginFile')
        TrueMaster = config.get('Settings', 'BotOwner')
        MASTERS = config.get('Settings', 'Masters').replace(' ', '').split(',')


    except:
            print "[!] Error have happened while fetching settings from configirc.ini!"
            sys.exit(1)
def argSettings():
    global HOST, PORT, NICK, IDENT, REALNAME, CHAN, PING, TrueMaster
    def get_base_parser():
        parser = argparse.ArgumentParser(description="iWi CLI - simple IRC client")
        parser.add_argument("-s", "--server", dest="server", help="server name which you wish to connect")
        parser.add_argument("-c","--channel", dest="channel", help="channel which client will try to connect, also a default channel choosen on start (withou #)")
        parser.add_argument("-p", "--port", type=int, dest="port", help="port of the server")
        parser.add_argument("-n", "--nick", dest="nick", help="nickname of the client")
        parser.add_argument("-i", "--ident", dest="ident", help="IDENT name of the client")
        parser.add_argument("-r", "--realname", dest="realname", help="realname of the client")
        parser.add_argument("-tm", "-truemaster", dest="truemaster", help="change the True Master of the bot")
        parser.add_argument("--ping", help="type it to hide the ping messages", action="store_false")
        return parser
    parser = get_base_parser()
    (options, args) = parser.parse_known_args()
    #args = parser.parse_args()
    if options.server:
        global HOST
        HOST = options.server
    elif options.channel:
        global CHAN
        CHAN = "#"+str(options.channel)
    elif options.port:
        global PORT
        PORT = options.port
    elif options.nick:
        global NICK
        NICK = options.nick
    elif options.ident:
        global IDENT
        IDENT = options.ident
    elif options.realname:
        global REALNAME
        REALNAME = options.realname
    elif options.truemaster:
        global TrueMaster
        TrueMaster = options.truemaster
    elif options.ping:
        global PING
        PING = 0



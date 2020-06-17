import requests  # pip install requests for installation

url = "http://cluster.data.vatsim.net/vatsim-data.txt"


class Client:
    # callsign:cid:realname:clienttype:frequency:latitude:longitude:altitude:groundspeed:planned_aircraft:planned_tascruise:planned_depairport:planned_altitude:planned_destairport:server:protrevision:rating:transponder:facilitytype:visualrange:planned_revision:planned_flighttype:planned_deptime:planned_actdeptime:planned_hrsenroute:planned_minenroute:planned_hrsfuel:planned_minfuel:planned_altairport:planned_remarks:planned_route:planned_depairport_lat:planned_depairport_lon:planned_destairport_lat:planned_destairport_lon:atis_message:time_last_atis_received:time_logon:heading:QNH_iHg:QNH_Mb:
    def __init__(self, callsign, cid, realname, clienttype, frequency, latitude, longitude, altitude, groundspeed, planned_aircraft, planned_tascruise, planned_depairport, planned_altitude, planned_destairport, server, protrevision, rating, transponder, facilitytype, visualrange, planned_revision, planned_flighttype, planned_deptime, planned_actdeptime, planned_hrsenroute, planned_minenroute, planned_hrsfuel, planned_minfuel, planned_altairport, planned_remarks, planned_route, planned_depairport_lat, planned_depairport_lon, planned_destairport_lat, planned_destairport_lon, atis_message, time_last_atis_received, time_logon, heading, QNH_iHg, QNH_Mb):
        self. callsign = callsign
        self. cid = cid
        self. realname = realname
        self. clienttype = clienttype
        self. frequency = frequency
        self. latitude = latitude
        self. longitude = longitude
        self. altitude = altitude
        self. groundspeed = groundspeed
        self. planned_aircraft = planned_aircraft
        self. planned_tascruise = planned_tascruise
        self. planned_depairport = planned_depairport
        self. planned_altitude = planned_altitude
        self. planned_destairport = planned_destairport
        self. server = server
        self. protrevision = protrevision
        self. rating = rating
        self. transponder = transponder
        self. facilitytype = facilitytype
        self. visualrange = visualrange
        self. planned_revision = planned_revision
        self. planned_flighttype = planned_flighttype
        self. planned_deptime = planned_deptime
        self. planned_actdeptime = planned_actdeptime
        self. planned_hrsenroute = planned_hrsenroute
        self. planned_minenroute = planned_minenroute
        self. planned_hrsfuel = planned_hrsfuel
        self. planned_minfuel = planned_minfuel
        self. planned_altairport = planned_altairport
        self. planned_remarks = planned_remarks
        self. planned_route = planned_route
        self. planned_depairport_lat = planned_depairport_lat
        self. planned_depairport_lon = planned_depairport_lon
        self. planned_destairport_lat = planned_destairport_lat
        self. planned_destairport_lon = planned_destairport_lon
        self. atis_message = atis_message
        self. time_last_atis_received = time_last_atis_received
        self. time_logon = time_logon
        self. heading = heading
        self. QNH_iHg = QNH_iHg
        self. QNH_Mb = QNH_Mb

    def toList(self):
        l = [self.callsign, self.cid, self.realname, self.clienttype, self. frequency, self. latitude, self. longitude, self. altitude, self. groundspeed, self. planned_aircraft, self. planned_tascruise, self. planned_depairport, self. planned_altitude, self. planned_destairport, self. server, self. protrevision, self. rating, self. transponder, self. facilitytype, self. visualrange, self. planned_revision, self. planned_flighttype, self. planned_deptime,
             self. planned_actdeptime, self. planned_hrsenroute, self. planned_minenroute, self. planned_hrsfuel, self. planned_minfuel, self. planned_altairport, self. planned_remarks, self. planned_route, self. planned_depairport_lat, self. planned_depairport_lon, self. planned_destairport_lat, self. planned_destairport_lon, self. atis_message, self. time_last_atis_received, self. time_logon, self. heading, self. QNH_iHg, self. QNH_Mb]
        return(l)

    def toString(self):
        l = self.callsign + "\t"+ self.cid +"\t"+ self.realname+"\t "+ self.clienttype+" \t"+ self. frequency+"\t "+ self. latitude+"\t "+ self. longitude+"\t "+self. altitude+"\t "+ self. groundspeed+"\t "+ self. planned_aircraft+" \t"+ self. planned_tascruise+"\t "+ self. planned_depairport+"\t "+ self. planned_altitude+"\t "+ self. planned_destairport+"\t "+ self. server+"\t "+ self. protrevision+"\t "+ self. rating+"\t "+ self. transponder+"\t "+ self. facilitytype+"\t "+ self. visualrange+"\t "+ self. planned_revision+"\t "+ self. planned_flighttype+"\t "+ self. planned_deptime+"\t "+ self. planned_actdeptime+"\t "+ self. planned_hrsenroute+"\t "+ self. planned_minenroute+"\t "+ self. planned_hrsfuel+" \t"+ self. planned_minfuel+" \t"+ self. planned_altairport+" \t"+ self. planned_remarks+"\t "+ self. planned_route+"\t "+ self. planned_depairport_lat+"\t "+ self. planned_depairport_lon+"\t "+ self. planned_destairport_lat+"\t "+ self. planned_destairport_lon+"\t "+ self. atis_message+"\t "+ self. time_last_atis_received+" \t"+ self. time_logon+"\t "+ self. heading+"\t "+ self. QNH_iHg+" \t"+ self. QNH_Mb+ "\n"
        return(l)


def get_VATSIM_data():
    r = requests.get(url)
    return(r.text)

VATSIM_DATA = get_VATSIM_data()

def parse_VATSIM_clientsSection():
    rawData = VATSIM_DATA
    data = rawData.splitlines()
    for line in data:
        if line.startswith(";"): data.remove(line)
        if line.startswith("!CLIENTS"): del data[0: data.index(line) +1]
        if line.startswith("!SERVERS"): del data[data.index(line) -1 : len(data)]
    return(data)

ParsedSection = parse_VATSIM_clientsSection()

def select_VATSIM_byIDClientList(id):
    rawData = ParsedSection
    client = rawData[id]
    return (client)


def get_VATSIM_client(id):
    rawData = select_VATSIM_byIDClientList(id)
    c = rawData.split(':')
    client = Client(c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9], c[10], c[11], c[12], c[13], c[14], c[15], c[16], c[17], c[18], c[19], c[20], c[21], c[22], c[23], c[24], c[25], c[26], c[27], c[28], c[29], c[30], c[31], c[32], c[33], c[34], c[35], c[36], c[37], c[38], c[39], c[40])
    return(client)

clients = []
for number in list(range(len(ParsedSection))):
    cliente = get_VATSIM_client(number)
    clients.append(cliente)


def save_TextFile_allClients(textFileName):
    header = "callsign\tcid\trealname\tclienttype\tfrequency\tlatitude\tlongitude\taltitude\tgroundspeed\tplanned_aircraft\tplanned_tascruise\tplanned_depairport\tplanned_altitude\tplanned_destairport\tserver\tprotrevision\trating\ttransponder\tfacilitytype\tvisualrange\tplanned_revision\tplanned_flighttype\tplanned_deptime\tplanned_actdeptimevplanned_hrsenroute\tplanned_minenroute\tplanned_hrsfuel\tplanned_minfuel\tplanned_altairport\tplanned_remarks\tplanned_route\tplanned_depairport_lat\tplanned_depairport_lon\tplanned_destairport_lat\tplanned_destairport_lon\tatis_message\ttime_last_atis_received\ttime_logon\theading\tQNH_iHg:QNH_Mb"
    with open("{}.txt".format(textFileName), 'a') as out:
        out.write(header + "\n")
        for number in list(range(len(ParsedSection))):
            out.write(clients[number].toString() + "\n")
            
def get_clients_bycompanyCalsign(companyICAO):
    toReturn = []
    for client in clients:
        if client.callsign.startswith(companyICAO):
            toReturn.append(client)
    return toReturn

def get_clients_byDepAiport(airportICAO):
    toReturn = []
    for client in clients:
        if client.planned_depairport.startswith(airportICAO):
            toReturn.append(client)
    return toReturn
for client in get_clients_byDepAiport("LPPT"):
    print(client.toString())
import sipfullproxy
import socketserver

if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 5060
    # ipaddress = '147.175.163.88'
    # ipaddress = '192.168.43.99'
    ipaddress = '10.10.29.157'

    sipfullproxy.recordroute = "Record-Route: <sip:{}:{};lr>".format(ipaddress, PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP {}:{}".format(ipaddress, PORT)

    sipfullproxy.set_logging_config()

    server = socketserver.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
    server.serve_forever()



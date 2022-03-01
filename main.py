import sipfullproxy
import socketserver
import sys

if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 5060

    if len(sys.argv) >= 2:
        ipaddress = sys.argv[1]
    else:
        print('IP address must be provided in argument')
        exit(0)

    sipfullproxy.recordroute = "Record-Route: <sip:{}:{};lr>".format(ipaddress, PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP {}:{}".format(ipaddress, PORT)

    sipfullproxy.set_logging_config()

    server = socketserver.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
    print("Server is running on {}:{}".format(ipaddress, PORT))
    server.serve_forever()





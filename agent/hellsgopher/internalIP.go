package hg

import "net"

func GetInternalIP(rhost string, rport string) string {
	conn, err := net.Dial("udp", rhost+":"+rport)
	if err != nil {
		return ""
	}
	defer conn.Close()

	localAddr := conn.LocalAddr().(*net.UDPAddr)

	return localAddr.IP.String()
}

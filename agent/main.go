package main

import (
	"fmt"
	"strconv"
)

var (
	sSLEEP    string                         // whats edited by the go compiler
	sJITTER   string                         // whats edited by the go compiler
	SLEEP, _         = strconv.Atoi(sSLEEP)  // interval between callbacks
	JITTER, _        = strconv.Atoi(sJITTER) // +- time in callbacks
	RHOST     string = "127.0.0.1"           // host to callback to
	RPORT     string = "80"                  // port to callback to
	USERAGENT string = "bingoc2/1.0.0"       // useragent of callback
	URI       string = "index.php"           // uri to callback to
	AgentID   string = "abcd"                // ID of agent (used by server to identify who is calling)
)

func main() {
	fmt.Printf("SLEEP: %d\nJITTER: %d\nRHOST: %s\nRPORT: %s\nUSERAGENT: %s\nURI: %s\nAGENT ID: %s", SLEEP, JITTER, RHOST, RPORT, USERAGENT, URI, AgentID)
}

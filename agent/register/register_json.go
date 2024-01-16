package register

type dataJSON struct {
	AgentID         int    `json:"AgentID"`
	Hostname        string `json:"Hostname"`
	Username        string `json:"Username"`
	Domain          string `json:"Domain"`
	InternalIP      string `json:"InternalIP"`
	ProcessPath     string `json:"Process Path"`
	ProcessID       int    `json:"Process ID"`
	ParentProcessID int    `json:"Process Parent ID"`
	ProcessArch     string `json:"Process Arch"`
	ProcessElevated int    `json:"Process Elevated"`
	OSBuild         string `json:"OS Build"`
	OSVersion       string `json:"OS Version"`
	OSARCH          string `json:"OS Arch"`
	Sleep           int    `json:"Sleep"`
}

type registerJSON struct {
	Task string   `json:"task"`
	Data dataJSON `json:"data"`
}

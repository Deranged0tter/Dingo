package hg

import (
	"os"
	"runtime"
)

func GetProcessPath() string {
	procpath, err := os.Executable()
	if err != nil {
		return ""
	}

	return procpath
}

func GetProcessID() int {
	return os.Getpid()
}

func GetParentProcessID() int {
	return os.Getppid()
}

func GetProcessArch() string {
	if runtime.GOARCH == "amd64" {
		return "x86_64"
	} else if runtime.GOARCH == "i386" {
		return "x86"
	} else {
		return ""
	}
}

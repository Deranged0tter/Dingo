// +windows
package hg

import (
	"fmt"

	"golang.org/x/sys/windows"
)

const VER_NT_WORKSTATION = 0x0000001

func GetOSVersion() string {
	osVersion := windows.RtlGetVersion()
	var osName string
	if osVersion.MajorVersion == 6 {
		switch osVersion.MinorVersion {
		case 0:
			if osVersion.ProductType == VER_NT_WORKSTATION {
				osName = "Vista"
			} else {
				osName = "Server 2008"
			}
		case 1:
			if osVersion.ProductType == VER_NT_WORKSTATION {
				osName = "7"
			} else {
				osName = "Server 2008 R2"
			}
		case 2:
			if osVersion.ProductType == VER_NT_WORKSTATION {
				osName = "8"
			} else {
				osName = "Server 2012"
			}
		case 3:
			if osVersion.ProductType == VER_NT_WORKSTATION {
				osName = "8.1"
			} else {
				osName = "Server 2012 R2"
			}
		}
	} else {
		if osVersion.ProductType == VER_NT_WORKSTATION {
			osName = "10"
		} else {
			osName = "Server 2016"
		}
	}
	return "Windows " + osName
}

func GetOSBuild() string {
	osVersion := windows.RtlGetVersion()
	return fmt.Sprint(osVersion.BuildNumber)
}

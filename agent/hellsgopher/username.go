package hg

import "os/user"

func GetUsername() string {
	currentUser, err := user.Current()
	if err != nil {
		return ""
	}

	return currentUser.Username
}

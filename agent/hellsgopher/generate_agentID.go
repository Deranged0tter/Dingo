package hg

import (
	"math/rand"
	"strings"
)

const charset = "0123456789"

func GenerateAgentID(length int) string {
	sb := strings.Builder{}
	sb.Grow(length)
	for i := 0; i < length; i++ {
		sb.WriteByte(charset[rand.Intn(len(charset))])
	}
	return sb.String()
}

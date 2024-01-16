BIN_NAME=dingo.exe
OUT_PATH=../bin/
isDLL=False


SLEEP=5
JITTER=5
RHOST=127.0.0.1
RPORT=80
USERAGENT=dingo
URI=

cGOOS=windows
cGOARCH=amd64

build-dingo:
ifeq (${isDLL}, False)
	GOOS=${cGOOS} GOARCH=${cGOARCH} go build \
	-ldflags "-X 'main.sSLEEP=${SLEEP}' -X 'main.sJITTER=${JITTER}' -X 'main.RHOST=${RHOST}' -X 'main.RPROT=${RPORT}' -X 'main.USERAGENT=${USERAGENT}' -X 'main.URI=${URI}' -H windowsgui" \
	-o ${OUT_PATH}${BIN_NAME}
else
	GOOS=${cGOOS} GOARCH=${cGOARCH} go build \
	-ldflags "-X 'main.sSLEEP=${SLEEP}' -X 'main.sJITTER=${JITTER}' -X 'main.RHOST=${RHOST}' -X 'main.RPROT=${RPORT}' -X 'main.USERAGENT=${USERAGENT}' -X 'main.URI=${URI}' -H windowsgui" \
	-o ${OUT_PATH}${BIN_NAME} -buildmode=c-shared
endif
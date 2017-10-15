#!/bin/bash
PORT=8080
N=0;
while sleep .25; do
	echo
	figlet -w 130 -f small "Request #$N..."
	echo http://$C9_HOSTNAME
	echo "[Hit Ctrl-C once to reload the document on the server]"
	echo "[Hit Ctrl-C twice in a row to exit]"
	(( N++ ))
	cat http.headers index.html | nc -l -p $PORT -q 1 | pygmentize -l http 2>/dev/null
	date
	sleep .25
done

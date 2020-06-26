package main

import (
	"flag"
	"fmt"
	"net/http"
	"net/http/httputil"
	"os"
)

func handler(w http.ResponseWriter, r *http.Request) {
	dump, err := httputil.DumpRequest(r, true)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(string(dump))
	}
	w.Write([]byte("true\n"))
}

func main() {
	var addr string
	flag.StringVar(&addr, "listen", "0.0.0.0:80", "The address to listen on, e.g. 0.0.0.0:80")
	flag.Parse()

	http.HandleFunc("/", handler)
	if err := http.ListenAndServe(addr, nil); err != nil {
		fmt.Printf("Failed to start server: %v\n", err)
		os.Exit(1)
	}
}

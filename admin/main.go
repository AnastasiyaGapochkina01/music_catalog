package main

import (
    "fmt"
    "log"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Fake Admin Panel - Hello!")
    })

    http.HandleFunc("/metrics", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "metrics: up")
    })

    log.Println("Starting admin on :8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}


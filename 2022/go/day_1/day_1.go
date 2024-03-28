package main

import (
	// "bufio"
	"fmt"
	// "io"
	"os"
)

// helper function to check for errors
func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	dat, err := os.ReadFile("./input.txt")
	check(err)
	fmt.Print((string(dat)))

}

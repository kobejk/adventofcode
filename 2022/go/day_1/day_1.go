package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

// helper function to check for errors
func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	f, err := os.Open("./input.txt")
	defer f.Close()

	check(err)

	scanner := bufio.NewScanner(f)

	maxCal := 0
	currentCal := 0
	elf := 1

	for scanner.Scan() {
		// read contents of a single line
		line := scanner.Text()

		// if line is empty, update max calories
		if line == "" {
			if currentCal > maxCal {
				maxCal = currentCal
				elf += 1
			}
			currentCal = 0
			// if line is not empty, update current elf total
		} else {
			value, err := strconv.Atoi(line)
			check(err)
			currentCal += value
		}
	}

	// final data block is not followed by a blank line
	if currentCal > maxCal {
		maxCal = currentCal
		elf += 1
	}

	fmt.Println("Elf", elf, "is carrying", maxCal, "calories.")

	// check for any scanning errors
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}

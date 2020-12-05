package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"utils"
)

func readSeats() []string {
	file, _ := os.Open("./in")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var seats []string
	for scanner.Scan() {
		seats = append(seats, scanner.Text())
	}
	return seats
}

func binarySearch(letters string, low int, high int) int {
	lo := low
	hi := high
	max_len := len(letters)
	mid := lo + ((hi - lo) / 2)

	i := 0
	for lo <= hi && i < max_len {
		currentChar := letters[i]
		if currentChar == 'F' || currentChar == 'L' {
			hi = mid
		} else if currentChar == 'B' || currentChar == 'R' {
			lo = mid + 1
		}
		if lo <= hi {
			mid = lo + ((hi - lo) / 2)
		}
		i += 1
	}
	return mid
}

func calcRow(seat string) int {
	return binarySearch(seat, 0, 127)
}

func calcColumn(seat string) int {
	return binarySearch(seat, 0, 7)
}

func calcSeatId(seat string) int {
	row := calcRow(seat[0:7])
	column := calcColumn(seat[7:len(seat)])
	return row*8 + column
}

func getSeatIds(seats []string) []int {
	seatIds := make([]int, 0)
	for _, seat := range seats {
		seatIds = append(seatIds, calcSeatId(seat))
	}
	return seatIds
}
func findHighestSeatId(seats []string) int {
	return utils.MaxInt(getSeatIds(seats)...)
}

func findMySeatId(seats []string) int {
	seatIds := getSeatIds(seats)
	sort.Ints(seatIds)
	for i := 1; i < len(seatIds); i++ {
		if seatIds[i]-1 != seatIds[i-1] {
			return seatIds[i] - 1
		}
	}
	return 0
}

func execPart1(seats []string) int {
	return findHighestSeatId(seats)
}

func execPart2(seats []string) int {
	return findMySeatId(seats)
}

func main() {
	seats := readSeats()

	// part 1
	highestSeatId := execPart1(seats)
	fmt.Println(highestSeatId)

	// part 2
	mySeatId := execPart2(seats)
	fmt.Println(mySeatId)
}

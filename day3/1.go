package main

import (
	"bufio"
	"fmt"
	"os"
)

func getTreeMap() []string {
	file, _ := os.Open("./in")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var treeMap []string
	for scanner.Scan() {
		treeMap = append(treeMap, scanner.Text())
	}
	return treeMap
}

type Slope struct {
	Right int
	Down  int
}

func traveseBySlope(treeMap []string, slope Slope) int {
	width := len(treeMap[0])
	height := len(treeMap)
	y := 0
	x := 0
	count := 0

	for y+slope.Down < height {
		x = (x + slope.Right) % width
		y += slope.Down
		if treeMap[y][x] == '#' {
			count += 1
		}
	}
	return count
}

func execPart1(treeMap []string) int {
	slope := Slope{3, 1}
	count := traveseBySlope(treeMap, slope)
	return count
}

func getSlopeList() [5]Slope {
	slopes := [...]Slope{Slope{1, 1}, Slope{3, 1}, Slope{5, 1}, Slope{7, 1}, Slope{1, 2}}
	return slopes
}

func execPart2(treeMap []string) int {
	slopes := getSlopeList()

	product := 1
	for _, slope := range slopes {
		product *= traveseBySlope(treeMap, slope)
	}
	return product
}

func main() {
	treeMap := getTreeMap()

	// part 1
	treeCount := execPart1(treeMap)
	fmt.Println(treeCount)

	// part 2
	product := execPart2(treeMap)
	fmt.Println(product)
}

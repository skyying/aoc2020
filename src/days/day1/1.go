package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
)

func readFile() []int {
	file, _ := os.Open("./in")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var nums []int
	for scanner.Scan() {
		n, _ := strconv.Atoi(scanner.Text())
		nums = append(nums, n)
	}
	return nums
}

func twoEntries(nums []int, target int) (int, error) {
	seen := make(map[int]bool, 0)
	for _, n := range nums {
		if _, ok := seen[target-n]; ok {
			return (target - n) * n, nil
		}
		seen[n] = true
	}
	return 0, errors.New("no matched")
}

func threeEntries(nums []int, target int) int {
	for i, n := range nums {
		complement := target - n
		val, err := twoEntries(nums[i+1:len(nums)], complement)
		if err == nil {
			return val * n
		}
	}
	return 0
}

func main() {
	nums := readFile()
	m2, err := twoEntries(nums, 2020)
	m3 := threeEntries(nums, 2020)
	fmt.Println(m2, m3)
}

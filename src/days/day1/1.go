package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"utils"
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
    a, b, err := utils.TwoSum(nums, target)
    return a * b, err
}

func threeEntries(nums []int, target int) int {
	for i, n := range nums {
		complement := target - n
		targetNum, err := twoEntries(nums[i+1:len(nums)], complement)
		if err == nil {
			return targetNum * n
		}
	}
	return 0
}

func main() {
	nums := readFile()
	// part 1
	fmt.Println(twoEntries(nums, 2020))

	// part 2
	fmt.Println(threeEntries(nums, 2020))
}

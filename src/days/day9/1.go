package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"utils"
)

func readNumbers() []int {
	file, _ := os.Open("./in")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var numbers []int
	for scanner.Scan() {
		n, _ := strconv.Atoi(scanner.Text())
		numbers = append(numbers, n)
	}
	return numbers
}

func execPart1(numbers []int, preambleRange int) int {
	for i := preambleRange; i < len(numbers); i++ {
		_, _, err := utils.TwoSum(numbers[i-preambleRange:i], numbers[i])
		if err != nil {
			return numbers[i]
		}
	}
	return 0
}

func execPart2(numbers []int, n int) int {
	left, right, sum := -1, 0, numbers[0]
	for sum != n && left < right && right < len(numbers) {
		if sum < n {
		    right++
			sum += numbers[right]
		} else {
		    left++
			sum -= numbers[left]
		}

		if sum == n && right-left > 1 {
		    break
		}
	}
    return utils.MaxInt(numbers[left:right+1]...) + utils.MinInt(numbers[left:right+1]...)
}

func main() {
	numbers := readNumbers()
	n := execPart1(numbers, 25)
	fmt.Println("Part 1 :", n)
	fmt.Println("Part 2 :", execPart2(numbers, n))
}

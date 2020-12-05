package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Policy struct {
	Password string
	Low      int
	Hi       int
	Char     byte
}

func parseInput() []Policy {
	file, _ := os.Open("./in")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var polices []Policy
	for scanner.Scan() {
		policy := cookPolicy(scanner.Text())
		polices = append(polices, policy)
	}
	return polices
}

func calcLimit(limitStr string) (int, int) {
	limit := strings.Split(limitStr, "-")
	low, _ := strconv.Atoi(limit[0])
	hi, _ := strconv.Atoi(limit[1])
	return low, hi
}

func cookPolicy(policyStr string) Policy {
	policyDataList := strings.Fields(policyStr)
	low, hi := calcLimit(policyDataList[0])
	char := policyDataList[1][0]
	pw := policyDataList[2]
	return Policy{pw, low, hi, char}
}

func calcValidPasswordCount(polices []Policy) int {
	count := 0
	for _, policy := range polices {
		charCountLookup := make(map[byte]int, 0)
		for i, _ := range policy.Password {
			charCountLookup[policy.Password[i]] += 1
		}
		if charCountLookup[policy.Char] >= policy.Low && charCountLookup[policy.Char] <= policy.Hi {
			count += 1
		}
	}
	return count
}

func calcValidPasswordCountContainOnePosition(polices []Policy) int {

	count := 0
	for _, policy := range polices {
		isOnlyHiPositionMatch := policy.Password[policy.Hi-1] == policy.Char && policy.Password[policy.Low-1] != policy.Char
		isOnlyLowPositionMatch := policy.Password[policy.Low-1] == policy.Char && policy.Password[policy.Hi-1] != policy.Char
		if isOnlyHiPositionMatch || isOnlyLowPositionMatch {
			count += 1
		}
	}

	return count
}

func main() {
	polices := parseInput()
	fmt.Println(calcValidPasswordCount(polices))
	fmt.Println(calcValidPasswordCountContainOnePosition(polices))
}

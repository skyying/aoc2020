package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func readGroupsFromFile(path string) [][]string {
	b, _ := ioutil.ReadFile(path) // just pass the file name
	trimmed := strings.TrimRight(string(b), "\n")
	groupsStr := strings.Split(trimmed, "\n\n")
	groups := make([][]string, 0)
	for _, g := range groupsStr {
		people := strings.Split(g, "\n")
		groups = append(groups, people)
	}
	return groups
}

func getNumberOfQuestionEverAnswered(groups [][]string) int {
	count := 0
	for _, group := range groups {
		answered := make(map[rune]int, 0)
		for _, person := range group {
			for _, question := range person {
				answered[question] = 1
			}
		}
		count += len(answered)
	}
	return count
}

func getNumberOfQuestionsThatEveryoneAnswered(groups [][]string) int {
	count := 0
	for _, group := range groups {
		answered := make(map[rune]int, 0)
		numberOfPeople := len(group)
		for _, person := range group {
			for _, question := range person {
				answered[question] += 1
			}
		}
		for _, answeredTimes := range answered {
			if answeredTimes == numberOfPeople {
				count += 1
			}
		}
	}
	return count
}

func main() {
	groups := readGroupsFromFile("./in")

	// part 1
	everAnswered := getNumberOfQuestionEverAnswered(groups)
	fmt.Println(everAnswered)

	// part 2
	everyoneAnswered := getNumberOfQuestionsThatEveryoneAnswered(groups)
	fmt.Println(everyoneAnswered)
}

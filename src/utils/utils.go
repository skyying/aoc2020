package utils

import (
    "math"
    "errors"
    )


func TwoSum(nums []int, target int) (int, int, error) {
	seen := make(map[int]bool, 0)
	for _, n := range nums {
		if _, ok := seen[target-n]; ok {
			return (target - n), n, nil
		}
		seen[n] = true
	}
	return 0, 0, errors.New("no matched")
}


func MaxInt(ary ...int) int {
    max_value := math.MinInt32
    for _, element := range ary {
        if element > max_value {
            max_value = element
        }
    }
    return max_value
}

package utils

import (
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


const (
    MaxInt64  = 1<<63 - 1
    MinInt64  = -1 << 63
)

func MinInt(ary ...int) int {
    minValue := MaxInt64
    for _, element := range ary {
        if element < minValue {
            minValue = element
        }
    }
    return minValue
}


func MaxInt(ary ...int) int {
    maxValue := MinInt64
    for _, element := range ary {
        if element > maxValue {
            maxValue = element
        }
    }
    return maxValue
}

package utils

import "math"

func MaxInt(ary ...int) int {
    max_value := math.MinInt32
    for _, element := range ary {
        if element > max_value {
            max_value = element
        }
    }
    return max_value
}

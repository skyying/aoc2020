#!/usr/bin/env bash

map=()

while IFS= read -a line; do
  map+=("$line")
done < ./in


function traverse_by_slope() {
  local right=$1
  local down=$2
  local x=0
  local y=0
  local width="${#map[0]}"
  local height="${#map[@]}"
  local count=0

  while (( (y + down) < height )); do
    x=$(( (x + right) % width))
    y=$(( y + down ))
    local row="${map[y]}"
    local char="${row:$x:1}"
    [[ "$char" == "#" ]] && (( count++ ))
  done
  echo "$count"
}


function get_sum_of_tress_by_slopes() {
  local count=1
  right_values=(1 3 5 7 1)
  down_values=(1 1 1 1 2)

  for i in {0..4}; do
    local right="${right_values[$i]}"
    local down="${down_values[$i]}"
    trees=$(traverse_by_slope "$right" "$down")
    count=$(( count * trees ))
  done
  echo $count
}

# part 1
number_of_tress=$(traverse_by_slope 3 1)
printf "Solution for Part 1 => %s\n" "$number_of_tress"

# part 2
product=$(get_sum_of_tress_by_slopes)
printf "Solution for Part 2 => %s\n" "$product"

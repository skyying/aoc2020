#!/usr/bin/env bash

policies=()

while IFS= read -a line; do
  policies+=("$line")
done < ./in

function calc_occurrence() {
  local char="$1"
  local password="$2"
  local length=$(("${#password}"))
  local i=0
  local count=0
  while (( i < length )); do
    if [[ "${password:$i:1}" == "$char" ]]; then
      ((count++))
    fi
   ((i++))
  done
  echo "$count"
}

function get_valid_password_count_by_boundaries_correctness() {
  local count=0
  for line in "${policies[@]}"; do
    IFS=' ' read -r -a policy <<< "$line"
    IFS='-' read -r -a limit <<< "${policy[0]}"
    IFS=':' read -r -a char <<< "${policy[1]}"

    ocr=$(calc_occurrence "${char[0]}" "${policy[2]}")
    if (( ocr >= limit[0] )) && (( ocr <= limit[1] )); then
      count=$(("$count" +  1))
    fi
  done
  echo "$count"
}


function get_valid_password_count_by_position_correctness() {
  local count=0
  for line in "${policies[@]}"; do
    IFS=' ' read -r -a policy <<< "$line"
    IFS='-' read -r -a limit <<< "${policy[0]}"
    IFS=':' read -r -a char <<< "${policy[1]}"
    local p1=$(( limit[0] - 1 ))
    local p2=$(( limit[1] - 1 ))
    local password="${policy[2]}"
    local c="${char[0]}"

    [[ "${password:$p1:1}" == "$c" ]] && [[ "${password:$p2:1}" != "$c" ]] && (( count++ ))
    [[ "${password:$p2:1}" == "$c" ]] && [[ "${password:$p1:1}" != "$c" ]] && (( count++ ))

  done
  echo "$count"
}

# part 1
part1Count=$(get_valid_password_count_by_boundaries_correctness)
printf "Solution for Part 1 ==> %s\n" "$part1Count"

# part 2
part2Count=$(get_valid_password_count_by_position_correctness)
printf "Solution for Part 2 ==> %s\n" "$part2Count"

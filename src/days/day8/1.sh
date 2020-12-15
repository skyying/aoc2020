#!/usr/bin/env bash

instructions=()

while IFS= read -a line; do
  instructions+=("$line")
done < ./in

ary_len=${#instructions[@]}
declare -A seen;

function part_one () {
  local instructions=("$@")
  i=0
  acc=0
  while (( i < ary_len )); do
    (( seen[$i] > 0 )) && break
    seen["$i"]="$i"
    IFS=" " read -a rules <<< "${instructions["$i"]}"
    opt=${rules[0]}
    val=${rules[1]}
    if [[ $opt == 'acc' ]]; then
      acc=$(( acc + val))
      (( i++ ))
    elif [[ $opt == 'jmp' ]]; then
      i=$(( i + val ))
    elif [[ $opt == 'nop' ]]; then
      (( i++ ))
    else
      pass
    fi
  done
  printf "Part 1: %s\n" "$acc"
}


part_one "${instructions[@]}"


#!/bin/bash

target_sum=2020

# read numbers from input
entries=($(cat  ./in |tr "\n" " "))
len_of_entreis=$(("${#entries[@]}"))


function get_product_from_2_sum() {

  # default value handling
  local target=2020
  [[ "$1" -gt "0" ]] && target=$1

  local start_idx=0
  [[ "$2" -gt "0" ]] && start_idx=$2

  declare -A lookup 
  local p=-1
  local len=$(( $len_of_entreis - $start_idx - 1))
  for n in "${entries[@]:$start_idx:$len}"; do
    local clp=$(($target - $n))
    [ ! -z ${lookup[$clp]} ] && p=$(($n * $clp)) && break
    lookup[$n]=$n
  done
  echo $p
}


function get_product_from_3_sum() {

  local count

  declare -A lookup 

  i=0

  while [ $i -le $len_of_entreis ]; do
    local cur=${entries[$i]}
    local product=$(get_product_from_2_sum $(($target_sum - $cur)) $(($i + 1)) )

    if (( $product > 0 )); then
      count=$(($cur * $product))
      break
    fi
    ((i++))
  done

  echo $count
}

function exec_part_1() {
  echo $(get_product_from_2_sum)
}

function exec_part_2() {
  echo $(get_product_from_3_sum)
}

exec_part_1
exec_part_2

  

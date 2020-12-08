package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"strconv"
	"errors"
)

type Instruction struct {
    Opt string
    Steps int
}

func readInstruction(path string) []Instruction {
	file, _ := os.Open("./in")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var instructions []Instruction
	for scanner.Scan() {
        instruction := strings.Fields(scanner.Text())
        if len(instruction) == 2 {
            opt := instruction[0]
            val, _ := strconv.Atoi(instruction[1])
            instructions = append(instructions, Instruction{opt, val})
        }
	}
	return instructions
}

func run(instruction Instruction, curIdx int, accumulator int) (int, int) {
    switch opt := instruction.Opt; opt {
    	case "acc":
    	    return curIdx+1, accumulator+instruction.Steps
    	case "jmp":
    	    return curIdx+instruction.Steps, accumulator
    	case "nop":
    	    return curIdx+1, accumulator
    	default:
    		fmt.Printf("%s.\n", opt)
    	}
    return 0, 0
}


func runProgram(instructions []Instruction) (int, error) {
    curIdx := 0
    accumulator := 0
    seen := map[int]bool{}
    for  {
        if _, ok := seen[curIdx]; !ok && curIdx < len(instructions) {
            seen[curIdx]=true
            instruction := instructions[curIdx]
            curIdx, accumulator = run(instruction, curIdx, accumulator)
        } else {
            break
        }
    }
    if curIdx < len(instructions) {
        return accumulator, errors.New("Stop")
    }
    return accumulator, nil
}


func swapOpt(opt string) string {
    if opt == "jmp" {
        return "nop"
    } else if opt == "nop" {
        return "jmp"
    }
    fmt.Println("you should not see this")
    return ""
}


func execPart1(instructions []Instruction) int {
	acc, err := runProgram(instructions)
	if err != nil {
	    fmt.Println(acc)
	    return acc
	}
	return 0
}


func execPart2(instructions []Instruction) int {
    for i, instruction := range instructions {
        if instruction.Opt != "acc" {
            cur := instruction
            instruction.Opt = swapOpt(instruction.Opt)
            instructions[i] = instruction
            acc, err := runProgram(instructions)
            if err != nil {
                instructions[i] = cur
            } else {
                fmt.Println(acc)
                return acc
            }
        }
    }
    return 0
}


func main() {
	instructions := readInstruction("./in")
	execPart1(instructions)
	execPart2(instructions)
}

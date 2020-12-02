const fs = require('fs');



fs.readFile('./in', 'utf8', (err, lines) => {
    const data = lines.split('\n');
    data.pop();
    performCalc(data.map(parsePolicy));
});


function parsePolicy(policyStr) {
    const [limit, char, password] = policyStr.split(' ')
    const [low, hi] = limit.split('-').map(Number)
    return [low, hi, char[0], password]
}

function getCountOfValidPassword(polices) {
    let count = 0
    for(let i = 0; i<polices.length; i++) {
        const lookup = {}
        const [low, hi, char, password] = polices[i]
        for(let j = 0; j< password.length; j++) {
            lookup[password[j]] = (lookup[password[j]] || 0) + 1
        }
        if (lookup[char] >= low && lookup[char] <= hi ) {
            count++
        }
    }
    return count
}

function getCountOfValidPasswordWithOnePosition(polices) {
    let count = 0
    for(let i = 0; i<polices.length; i++) {
        const lookup = {}
        const [low, hi, char, password] = polices[i]
        if (password[low-1] === char && password[hi-1] !== char) {
            count++
        }
        if (password[low-1] !== char && password[hi-1] === char) {
            count++
        }
    }
    return count
}

function performCalc(polices) {
    console.log(getCountOfValidPassword(polices))
    console.log(getCountOfValidPasswordWithOnePosition(polices))
}

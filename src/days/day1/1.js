const fs = require('fs');


function two_entries(nums, target){
  const seen = {}
  for(let i = 0; i<nums.length; i++) {
    const complement = target - nums[i]
    if (seen[complement]) {
      return nums[i] * complement
    }
    seen[nums[i]] = true
  }
  return null
}


function three_entries(nums, target){
  for(let i = 0; i<nums.length; i++){
    const matched = two_entries(nums.slice(i+1, nums.length), target - nums[i])
    if(matched) {
      return matched * nums[i]
    }
  }
  return null;
}


fs.readFile('./in', 'utf8', (err, data) => {
  performCalc(data.split('\n').map(Number))
});


function performCalc(nums) {
  console.log(two_entries(nums, 2020))
  console.log(three_entries(nums, 2020))
}

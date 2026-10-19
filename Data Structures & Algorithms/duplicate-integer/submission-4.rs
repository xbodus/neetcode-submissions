impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let seen: HashSet<i32> = nums.iter().copied().collect();
        seen.len() != nums.len()
    }
}

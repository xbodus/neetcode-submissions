impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let nums_clone = nums.clone();
        let seen: HashSet<i32> = nums_clone.into_iter().collect();

        seen.len() != nums.len()
    }
}

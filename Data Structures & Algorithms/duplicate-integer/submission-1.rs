impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut seen: Vec<i32> = Vec::new();

        for n in nums {
            if seen.contains(&n) {
                return true
            }

            seen.push(n);
        }

        false
    }
}

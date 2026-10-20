use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {return false}

        let mut s_freq: HashMap<char, u32> = HashMap::new();
        let mut t_freq: HashMap<char, u32> = HashMap::new();

        for s_char in s.chars() {
            let count = s_freq.entry(s_char).or_insert(0);
            *count += 1;
        }

        for t_char in t.chars() {
            let count = t_freq.entry(t_char).or_insert(0);
            *count += 1;
        }

        s_freq == t_freq
    }
}

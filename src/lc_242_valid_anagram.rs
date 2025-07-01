use std::collections::HashMap;

pub fn is_anagram(s: String, t: String) -> bool {
    let mut s_letters: HashMap<char, i32> = HashMap::new();
    let mut t_letters: HashMap<char, i32> = HashMap::new();

    let s_it = s.chars();
    for l in s_it {
	*s_letters.entry(l).or_insert(1) += 1;
    }

    let t_it = t.chars();
    for l in t_it {
	*t_letters.entry(l).or_insert(1) += 1;
    }

    if s_letters == t_letters {
	return true;
    }
    return false;
    
    
    
}


#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn ex1() {
	assert_eq!(is_anagram("anagram".to_string(), "nagaram".to_string()), true);
    }

    #[test]
    fn ex2() {
	assert_eq!(is_anagram("rat".to_string(), "car".to_string()), false);
    }
}

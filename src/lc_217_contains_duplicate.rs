use std::collections::HashMap;

pub fn contains_duplicate(nums: Vec<i32>) -> bool {
    let mut nums_map: HashMap<i32, i32> = HashMap::new();

    for i in nums {
	if nums_map.contains_key(&i) {
	    return true;
	}
	nums_map.insert(i, 1);
    }
    return false;
}


#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn ex1() {
	assert_eq!(contains_duplicate(vec![1, 2, 3, 1]), true)
    }
    
    #[test]
    fn ex2() {
	assert_eq!(contains_duplicate(vec![1, 2, 3, 4]), false)
    }

    #[test]
    fn ex3() {
	assert_eq!(contains_duplicate(vec![1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), true)
    }
}

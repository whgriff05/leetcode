use std::collections::HashMap;

pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
    let mut counts: HashMap<i32, i32> = HashMap::new();
    for i in nums {
	*counts.entry(i).or_insert(1) += 1;
    }

    let mut output: Vec<i32> = Vec::new();
    for _increment in 0..k {
	let mut greatest_index: i32 = -1;
	let mut greatest_count: i32 = -1;

	for (i, c) in &counts {
	    if c > &greatest_count {
		greatest_count = *c;
		greatest_index = *i;
	    }
	}

	output.push(greatest_index);
	counts.remove(&greatest_index);
    }

    return output;
}


#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn ex1() {
	assert_eq!(top_k_frequent(vec![1, 1, 1, 2, 2, 3], 2), vec![1, 2])
    }

    #[test]
    fn ex2() {
	assert_eq!(top_k_frequent(vec![1], 1), vec![1])
    }
}

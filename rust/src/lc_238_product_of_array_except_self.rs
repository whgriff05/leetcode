pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
    let mut output: Vec<i32> = Vec::new();
    let mut left: Vec<i32> = Vec::with_capacity(nums.len());
    left.resize(nums.len(), 1);
    let mut right: Vec<i32> = Vec::with_capacity(nums.len());
    right.resize(nums.len(), 1);
    left[0] = 1;
    right[nums.len() - 1] = 1;

    for i in 1..nums.len() {
	left[i] = left[i - 1] * nums[i - 1];
    }
    for i in (0..nums.len()-1).rev() {
	right[i] = right[i + 1] * nums[i + 1];
    }

    for i in 0..nums.len() {
	output.push(left[i] * right[i]);
    }
    

    return output;
}

/*

[1, 2, 3, 4]

left: [1, 1, 2, 6]
right: [24, 12, 4, 1]

 */


#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn ex1() {
	assert_eq!(product_except_self(vec![1, 2, 3, 4]), vec![24, 12, 8, 6])
    }

    #[test]
    fn ex2() {
	assert_eq!(product_except_self(vec![-1, 1, 0, -3, 3]), vec![0, 0, 9, 0, 0])
    }
}

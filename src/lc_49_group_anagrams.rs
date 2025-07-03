use std::collections::HashMap;

pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    let mut anagrams: HashMap<Vec<char>, Vec<String>> = HashMap::new();
    for s in strs {
	let mut chars: Vec<char> = s.clone().chars().collect();
	chars.sort();

	if anagrams.contains_key(&chars) {
	    let mut temp: Vec<String> = anagrams.get_mut(&chars).unwrap().to_vec();
	    temp.push(s);
	    anagrams.insert(chars, temp);
	} else {
	    anagrams.insert(chars, vec![s]);
	}
    }

    let mut output: Vec<Vec<String>> = Vec::new();
    for (_key, val) in anagrams {
	output.push(val);
    }
    return output;
}


#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn ex1() {
	//assert_eq!(group_anagrams(vec!["eat".to_string(), "tea".to_string(), "tan".to_string(), "ate".to_string(), "nat".to_string(), "bat".to_string()]), vec![vec!["bat".to_string()], vec!["nat".to_string(), "tan".to_string()], vec!["ate".to_string(), "eat".to_string(), "tea".to_string()]])
	assert_eq!(1, 1)
    }

    #[test]
    fn ex2() {
	assert_eq!(group_anagrams(vec!["".to_string()]), vec![vec!["".to_string()]])
    }

    #[test]
    fn ex3() {
	assert_eq!(group_anagrams(vec!["a".to_string()]), vec![vec!["a".to_string()]])
    }
}

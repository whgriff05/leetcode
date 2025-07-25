def getHint(secret, guess):
    bulls = 0
    cows = 0
    secret_dict = {}
    correct_indices = []
    for digit in secret:
        if digit in secret_dict:
            secret_dict[digit] += 1
        else:
            secret_dict[digit] = 1

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            secret_dict[guess[i]] -= 1
            if secret_dict[guess[i]] == 0:
                del secret_dict[guess[i]]
            bulls += 1
            correct_indices.append(i)
            
    for i in range(len(guess)):
        if guess[i] in secret_dict and i not in correct_indices:
            secret_dict[guess[i]] -= 1
            if secret_dict[guess[i]] == 0:
                del secret_dict[guess[i]]
            cows += 1

    return f"{bulls}A{cows}B"
        


# Tests
from testsuite import lc_test
lc_test(1, getHint("1807", "7810"), "1A3B")
lc_test(2, getHint("1123", "0111"), "1A1B")

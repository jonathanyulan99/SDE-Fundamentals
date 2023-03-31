'''
You are given a license key represented as a string s that consists of only alphanumeric characters
and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the
first group, which could be shorter than k but still must contain at least one character. Furthermore,
there must be a dash inserted between two groups, and you should convert all lowercase letters to 
uppercase.

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except 
the first part as it could be shorter as mentioned above.

'''


def license_key_formatting(S: str, K: int) -> str:
    # eliminate the dashes and replace with no spaces between
    # '5F3Z-2e-9-w' => '5F3Z2e9w'
    #  012345678910     01234567
    # '2-5g-3-J' ===> '25g3J'
    #  01234567        01234
    S = S.replace('-', '').upper()
    head = len(S) % K

    grouping = []
    if head:
        grouping.append(S[:head])

    for idx in range(head, len(S), K):
        grouping.append(S[idx:idx+K])

    return '-'.join(grouping)


print(license_key_formatting('5F3Z-2e-9-w', 4))
print(license_key_formatting('2-5g-3-j', 2))

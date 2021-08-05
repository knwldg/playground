def isPalindrome(s: str) -> bool:
    chars = [c for c in s.lower() if 97 <= ord(c) <= 122 or 48 <= ord(c) <= 57]

    if len(chars) == 1:
        return True

    for i, c in enumerate(chars[::-1]):
        if c != chars[i]:
            return False

    return True


if __name__ == '__main__':
    print(isPalindrome("A man, a plan, a canal: Panama"))

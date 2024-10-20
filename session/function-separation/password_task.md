# Exercise: Password Validation Criteria

Your task is to implement password validation functions that check the following criteria:

- Minimum length:
  Requirement: Password must be at least 8 characters long
  Example: “short” (invalid) vs “longenough” (valid)

- Uppercase letter:
  Requirement: Password must contain at least one uppercase letter (A-Z)
  Example: “alllowercase” (invalid) vs “OneUppercase” (valid)

- Lowercase letter:
  Requirement: Password must contain at least one lowercase letter (a-z)
  Example: “ALLUPPERCASE” (invalid) vs “OneLowercase” (valid)

- Numeric digit:
  Requirement: Password must contain at least one number (0-9)
  Example: “NoNumbers” (invalid) vs “One2Three” (valid)

- Special character:
  Requirement: Password must contain at least one special character (@, #, $, %, etc.)
  Example: “NoSpecialChars” (invalid) vs “Special@Char” (valid)

- No common words:
  Requirement: Password cannot contain words like “password”, “123456”, or “qwerty”
  Example: “MyPassword123” (invalid) vs “Un1que&Str0ng” (valid)

- Maximum length:
  Requirement: Password cannot be longer than 64 characters
  Example: A 65-character string (invalid) vs a 63-character string (valid)

- No consecutive repeated characters:
  Requirement: Password cannot contain the same character repeated more than twice in a row
  Example: “AAAbbbCC” (invalid) vs “AaBbCc” (valid)

- Minimum unique characters:
  Requirement: Password must contain at least 5 different characters
  Example: “AAAbbbCCC” (invalid) vs “Abcde123” (valid)

- No personal information:
  Requirement: Password cannot contain the user’s name or username
  Example: If username is “john”, “john123” (invalid) vs “Str0ng&P@ss” (valid)

Implement a separate function for each of these criteria, ensuring that each function has a single responsibility of checking one specific requirement.

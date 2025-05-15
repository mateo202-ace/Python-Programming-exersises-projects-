## Basics 🛠️
Regular expressions, or regex, are patterns used to match character combinations in strings. They are powerful tools for searching, replacing, and validating text. Below are the fundamental building blocks of regex:

| Symbol   | Description                                                                 | Example                                                                 |
|----------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `.`      | Matches any single character except newline.                                | `a.b` matches `acb`, `a1b`, but not `ab`.                              |
| `^`      | Matches the start of a string.                                              | `^hello` matches `hello` at the beginning of a string.                 |
| `$`      | Matches the end of a string.                                                | `world$` matches `world` at the end of a string.                       |
| `*`      | Matches 0 or more repetitions of the preceding element.                     | `ab*` matches `a`, `ab`, `abb`, etc.                                   |
| `+`      | Matches 1 or more repetitions of the preceding element.                     | `ab+` matches `ab`, `abb`, but not `a`.                                |
| `?`      | Matches 0 or 1 repetition of the preceding element.                         | `colou?r` matches both `color` and `colour`.                           |
| `{n}`    | Matches exactly `n` repetitions of the preceding element.                   | `a{3}` matches `aaa`.                                                  |
| `{n,}`   | Matches `n` or more repetitions.                                            | `a{2,}` matches `aa`, `aaa`, `aaaa`, etc.                              |
| `{n,m}`  | Matches between `n` and `m` repetitions.                                    | `a{2,4}` matches `aa`, `aaa`, or `aaaa`.                               |

---

## Character Classes 🔤
Character classes allow you to define a set of characters to match.

| Pattern   | Description                                                                 | Example                                                                 |
|-----------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `[abc]`   | Matches any one of `a`, `b`, or `c`.                                        | `[abc]` matches `a` in `apple`.                                        |
| `[^abc]`  | Matches any character except `a`, `b`, or `c`.                              | `[^abc]` matches `d` in `dog`.                                         |
| `[a-z]`   | Matches any lowercase letter.                                               | `[a-z]` matches `m` in `mouse`.                                        |
| `[A-Z]`   | Matches any uppercase letter.                                               | `[A-Z]` matches `G` in `Giraffe`.                                      |
| `[0-9]`   | Matches any digit.                                                          | `[0-9]` matches `5` in `12345`.                                        |
| `\d`      | Matches any digit (equivalent to `[0-9]`).                                   | `\d` matches `7` in `7up`.                                             |
| `\D`      | Matches any non-digit.                                                      | `\D` matches `a` in `abc123`.                                          |
| `\w`      | Matches any word character (alphanumeric + `_`).                            | `\w` matches `h` in `hello_world`.                                     |
| `\W`      | Matches any non-word character.                                             | `\W` matches `!` in `hello!`.                                          |
| `\s`      | Matches any whitespace character.                                           | `\s` matches the space in `hello world`.                               |
| `\S`      | Matches any non-whitespace character.                                       | `\S` matches `h` in `hello`.                                           |

---

## Anchors 📍
Anchors are used to match positions within a string.

| Anchor    | Description                                                                 | Example                                                                 |
|-----------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `\b`      | Matches a word boundary.                                                   | `\bcat\b` matches `cat` in `a cat is here`.                            |
| `\B`      | Matches a non-word boundary.                                               | `\Bcat` matches `cat` in `concatenate`.                                |

---

## Groups and Alternation 🔗
Groups and alternation allow you to create complex patterns.

| Pattern       | Description                                                                 | Example                                                                 |
|---------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `(abc)`       | Matches the exact sequence `abc`.                                           | `(abc)` matches `abc` in `alphabet`.                                   |
| `|`           | Acts as OR (e.g., `a|b` matches `a` or `b`).                                | `a|b` matches `a` in `apple` or `b` in `banana`.                       |
| `(?:...)`     | Non-capturing group.                                                       | `(?:abc)` matches `abc` but does not create a capturing group.         |
| `(?=...)`     | Positive lookahead.                                                        | `a(?=b)` matches `a` in `ab` but not in `ac`.                          |
| `(?!...)`     | Negative lookahead.                                                        | `a(?!b)` matches `a` in `ac` but not in `ab`.                          |
| `(?<=...)`    | Positive lookbehind.                                                       | `(?<=a)b` matches `b` in `ab`.                                         |
| `(?<!...)`    | Negative lookbehind.                                                       | `(?<!a)b` matches `b` in `cb` but not in `ab`.                         |

---

## Escaping 🛡️
Escaping allows you to match special characters literally.

| Pattern   | Description                                                                 | Example                                                                 |
|-----------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `\`       | Escapes a special character (e.g., `\.` matches a literal dot).             | `\.` matches `.` in `file.txt`.                                        |

---

## Common Patterns 📚
Here are some commonly used regex patterns:

| Pattern                     | Description                                                                 | Example                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` | Matches email addresses.                                               | `example@example.com`.                                                 |
| `https?://[^\s/$.?#].[^\s]*` | Matches URLs.                                                             | `http://example.com`.                                                  |
| `\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}` | Matches phone numbers.                                                | `(123) 456-7890`.                                                      |
| `\d{4}-\d{2}-\d{2}`         | Matches dates in `YYYY-MM-DD` format.                                      | `2023-10-01`.                                                          |

---

## Flags 🚩
Flags modify the behavior of regex patterns.

| Flag   | Description                                                                 | Example                                                                 |
|--------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `i`    | Case-insensitive matching.                                                  | `/abc/i` matches `ABC`.                                                |
| `g`    | Global matching.                                                            | `/a/g` matches all occurrences of `a` in `banana`.                     |
| `m`    | Multiline matching.                                                         | `^a` matches `a` at the start of each line in multiline text.          |
| `s`    | Dot matches newline.                                                        | `.` matches newline characters when the `s` flag is used.              |

---

## Examples 💡
Here are some practical examples of regex usage:

| Pattern           | Description                                                                 | Example                                                                 |
|-------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `^\d{5}$`         | Matches a 5-digit ZIP code.                                                 | `12345`.                                                               |
| `#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})` | Matches a hexadecimal color.                                          | `#FFFFFF` or `#FFF`.                                                   |


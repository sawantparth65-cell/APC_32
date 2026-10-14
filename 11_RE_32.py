import re

# 1. Extract all digits
print("\n1. EXTRACT ALL DIGITS")
text = input("Enter a string: ")
print("Digits:", re.findall(r'\d', text))


# 2. Words beginning with A or a
print("\n2. WORDS BEGINNING WITH A OR a")
text = input("Enter a sentence: ")
print("Words:", re.findall(r'\b[Aa]\w*\b', text))


# 3. Count vowels
print("\n3. COUNT VOWELS")
text = input("Enter a string: ")
vowels = re.findall(r'[aeiou]', text, re.I)
print("Vowels:", vowels)
print("Total vowels:", len(vowels))


# 4. Extract uppercase letters
print("\n4. UPPERCASE LETTERS")
text = input("Enter a string: ")
print("Uppercase letters:", re.findall(r'[A-Z]', text))


# 5. Identify spaces, tabs, and newlines
print("\n5. SPACES, TABS AND NEWLINES")
text = input("Enter text: ")
print("Spaces:", len(re.findall(r' ', text)))
print("Tabs:", len(re.findall(r'\t', text)))
print("Newlines:", len(re.findall(r'\n', text)))
print("All whitespace:", re.findall(r'[ \t\n]', text))


# 6. Replace multiple spaces with one space
print("\n6. REPLACE MULTIPLE SPACES")
text = input("Enter a string: ")
print("Result:", re.sub(r' {2,}', ' ', text))


# 7. Words containing exactly five characters
print("\n7. FIVE-CHARACTER WORDS")
text = input("Enter a sentence: ")
print("Words:", re.findall(r'\b[A-Za-z]{5}\b', text))


# 8. Words ending with s
print("\n8. WORDS ENDING WITH S")
text = input("Enter a sentence: ")
print("Words:", re.findall(r'\b\w+s\b', text, re.I))


# 9. Remove special characters
print("\n9. REMOVE SPECIAL CHARACTERS")
text = input("Enter a string: ")
print("Result:", re.sub(r'[^A-Za-z0-9 ]', '', text))


# 10. Count words in a sentence
print("\n10. COUNT WORDS")
text = input("Enter a sentence: ")
words = re.findall(r'\b\w+\b', text)
print("Number of words:", len(words))


# 11. Validate Indian mobile number
print("\n11. VALIDATE MOBILE NUMBER")
mobile = input("Enter mobile number: ")
if re.fullmatch(r'[6-9]\d{9}', mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")


# 12. Validate email address
print("\n12. VALIDATE EMAIL")
email = input("Enter email address: ")
pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
if re.fullmatch(pattern, email):
    print("Valid email format")
else:
    print("Invalid email format")


# 13. Extract dates in DD-MM-YYYY format
print("\n13. EXTRACT DATES")
text = input("Enter a paragraph: ")
pattern = r'\b(?:0[1-9]|[12]\d|3[01])-(?:0[1-9]|1[0-2])-\d{4}\b'
print("Dates:", re.findall(pattern, text))


# 14. Extract HTTP and HTTPS URLs
print("\n14. EXTRACT WEB ADDRESSES")
text = input("Enter text containing URLs: ")
print("URLs:", re.findall(r'https?://[^\s<>"\']+', text))


# 15. Extract hashtags
print("\n15. EXTRACT HASHTAGS")
text = input("Enter a social media post: ")
print("Hashtags:", re.findall(r'(?<!\w)#[A-Za-z0-9_]+', text))


# 16. Validate password strength
print("\n16. VALIDATE PASSWORD")
password = input("Enter password: ")
pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9\s])\S{8,}'
if re.fullmatch(pattern, password):
    print("Strong password")
else:
    print("Password does not meet requirements")


# 17. Identify consecutive repeated words
print("\n17. REPEATED WORDS")
text = input("Enter a sentence: ")
pattern = r'\b(\w+)\s+\1\b'
print("Repeated words:", re.findall(pattern, text, re.I))


# 18. Extract Indian PIN codes
print("\n18. EXTRACT PIN CODES")
text = input("Enter a paragraph: ")
print("PIN codes:", re.findall(r'\b[1-9]\d{5}\b', text))


# 19. Validate vehicle registration number
print("\n19. VEHICLE REGISTRATION")
number = input("Enter vehicle number: ").upper()
pattern = r'[A-Z]{2}\d{2}[A-Z]{1,3}\d{4}'
if re.fullmatch(pattern, number):
    print("Valid registration format")
else:
    print("Invalid registration format")


# 20. Extract file extensions
print("\n20. EXTRACT FILE EXTENSIONS")
text = input("Enter filenames: ")
pattern = r'\b[\w-]+\.(\w+)\b'
print("Extensions:", re.findall(pattern, text))


# 21. Remove HTML tags, extra whitespace and punctuation
print("\n21. CLEAN HTML TEXT")
text = input("Enter HTML text: ")
text = re.sub(r'<[^>]*>', '', text)
text = re.sub(r'\s+', ' ', text)
text = re.sub(r'[^\w\s.,!?-]', '', text)
print("Cleaned text:", text.strip())


# 22. Extract invoice number, date and amount
print("\n22. EXTRACT INVOICE DETAILS")
text = input("Enter invoice text: ")

invoice = re.search(
    r'Invoice\s*No\.?\s*[:#]?\s*([A-Z0-9-]+)',
    text, re.I
)
date = re.search(
    r'Date\s*:\s*(\d{2}-\d{2}-\d{4})',
    text, re.I
)
amount = re.search(
    r'Amount\s*:\s*(?:Rs\.?|INR|₹)?\s*([\d,]+(?:\.\d{2})?)',
    text, re.I
)

print("Invoice number:", invoice.group(1) if invoice else "Not found")
print("Date:", date.group(1) if date else "Not found")
print("Amount:", amount.group(1) if amount else "Not found")


# 23. Identify single-line Python comments
print("\n23. IDENTIFY PYTHON COMMENTS")
print("Enter Python source code, then type END on a new line.")

lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

source = "\n".join(lines)
comments = re.findall(r'^[ \t]*#.*$', source, re.M)

print("Single-line comments:")
for comment in comments:
    print(comment)

print("Note: Regex alone cannot reliably identify every comment inside Python source strings.")


# 24. Validate product code ABC-1234-XY
print("\n24. VALIDATE PRODUCT CODE")
code = input("Enter product code: ")
if re.fullmatch(r'[A-Z]{3}-\d{4}-[A-Z]{2}', code):
    print("Valid product code")
else:
    print("Invalid product code")


# 25. Extract student names, roll numbers and marks
print("\n25. EXTRACT STUDENT DETAILS")
text = input("Enter student details: ")
pattern = (
    r'Name:\s*([A-Za-z ]+),\s*'
    r'Roll:\s*(\d+),\s*'
    r'Marks:\s*(\d+(?:\.\d+)?)'
)
matches = re.findall(pattern, text, re.I)

if matches:
    for name, roll, marks in matches:
        print("Name:", name.strip())
        print("Roll number:", roll)
        print("Marks:", marks)
else:
    print("No matching student record found")


# 26. Extract DOI, years, emails and URLs
print("\n26. EXTRACT RESEARCH REFERENCE DETAILS")
text = input("Enter research paper references: ")

dois = re.findall(r'\b10\.\d{4,9}/[^\s<>"\']+', text)
years = re.findall(r'\b(?:19|20)\d{2}\b', text)
emails = re.findall(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    text
)
urls = re.findall(r'https?://[^\s<>"\']+', text)

print("DOI identifiers:", dois)
print("Publication years:", years)
print("Email addresses:", emails)
print("URLs:", urls)
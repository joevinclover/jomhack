
name = "Bob"             #String
age = 10                 #Integer
weight = 20.5            #Float
is_female = False        #Boolean
her_name = "Alice"
random_number = None     #Nontype
tapir = "animal"

print(name)
print(type(name))
print(her_name)
print(type(random_number))

C = 25
F = C*9/5+32

print(F)


text = """Python is a powerful programming language. It's easy to learn and versatile!
You can use Python for web development, data science, and automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""

char_count = len(text)
char_count_no_space = len(text.replace(" ",""))
word_count = len(text.split())
sentence_count = text.count('.') + text.count('!') + text.count('?')

print(f"Character count (including spaces): {char_count}")
print(f"Character count (excluding spaces): {char_count_no_space}")
print(f"Word count: {word_count}")
print(f"Sentence count: {sentence_count}")
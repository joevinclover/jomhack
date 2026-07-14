
text = "Python Programming"

print(text[0])
print(text[-1])
print(text[0:6])
print(text[:6])
print(text[7:])


name = 'bob the builder'

print(len(name))
print(name.strip())
print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("bob", "jane"))

name = "John Doe"
age = 30

message_1 = (f"My name is {name} and I am {age} years old")

print(message_1)


text = """Python is a powerful programming language. It's easy to learn and versatile!
You can use Python for web development, data science, and automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""



char_count = len(text) 
char_count_no_space = len(text.replace(" ", ""))
word_count = len(text.split())
sentence_count = text.count('.') + text.count('!') + text.count('?')


print(f"Character count (including spaces): {char_count}")
print(f"Character count (excluding spaces): {char_count_no_space}")
print(f"Word count: {word_count}")
print(f"Sentence count: {sentence_count}")

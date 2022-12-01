# Read file in read mode 'r'
with open('adventDay1.txt', 'r') as file:
  content = file.read()
# Replace string
content = content.replace('\n', '0\n')
# Write new content in write mode 'w'
with open('adventDay1.txt', 'w') as file:
  file.write(content)
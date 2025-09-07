# Retrieve the book instance created earlier
book = Book.objects.get(title="1984")

# Update the title of the book
book.title = "Nineteen Eighty-Four"

# Save the changes
book.save()

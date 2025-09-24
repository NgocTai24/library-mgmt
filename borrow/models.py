from django.db import models
from django.contrib.auth.models import User
from books.models import Book

class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('borrowed', 'Borrowed'), ('returned', 'Returned')],
        default='borrowed'
    )

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

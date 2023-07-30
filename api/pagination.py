from rest_framework import pagination


class CreatedAtPagination(pagination.CursorPagination):
    ordering = "-pk"

from rest_framework.pagination import LimitOffsetPagination


# NOTE: it has one caveat - you are allowed to specify "limit" yourself in request
class InventoryPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 3

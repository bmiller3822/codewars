from django.shortcuts import render

# Removing an array from another array kata


def array_diff(a, b):
    return [x for x in a if x not in b]

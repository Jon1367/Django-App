#!/usr/bin/env python
import os
import sys
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

#from .models import Lunch

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviepicker.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

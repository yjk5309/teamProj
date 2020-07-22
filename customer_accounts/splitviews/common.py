from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from customer_accounts.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

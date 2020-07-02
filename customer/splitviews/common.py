from django.shortcuts import render,redirect,HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from accounts.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

import string
import random
import hashlib
import base64
from django.contrib.auth.hashers import pbkdf2

import os
import uuid
import json
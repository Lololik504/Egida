from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone, dateparse
from django.utils.dateparse import parse_date

from main.models import Personal, Disctict, Temperature, School, Building, services, MyModel, Requisites

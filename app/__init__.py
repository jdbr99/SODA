from flask import Flask
import dotenv
from pathlib import Path

app = Flask(__name__)

from app import views
from flask import Flask, Blueprint, render_template, url_for, session, request, redirect, send_file, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from flask_bcrypt import Bcrypt

from datetime import datetime
import os, re
import requests
import io
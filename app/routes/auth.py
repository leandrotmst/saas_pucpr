from flask import Flask, redirect, Blueprint, request, url_for
import os


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register')
def register():
    register_url = url_for('auth.register')
    return register_url

@auth_bp.route('/login')
def login():
    login_url = url_for('auth.login')
    return login_url

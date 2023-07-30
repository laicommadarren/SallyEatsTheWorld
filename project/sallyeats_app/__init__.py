from flask import Flask, session, flash, render_template
app = Flask(__name__)
app.secret_key = "sallyproject"
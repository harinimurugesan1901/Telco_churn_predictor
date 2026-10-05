from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Telco Churn Predictor</title>
<style>
  body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .card {
    background: #ffffff;
    padding: 32px 28px;
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    width: 90%;
    max-width: 380px;
    text-align: center;
  }
  h2 {
    color: #1a202c;
    font-size: 22px;
    margin: 0 0 22px 0;
    font-weight: 800;
  }
  input {
    width: 100%;
    box-sizing: border-box;
    padding: 13px 15

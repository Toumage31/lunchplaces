#!/usr/bin/env python3
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

restaurants = [
    "Viet-AN",
    "DICAPO",
    "Pizza du bout de la rue",
    "Boulangerie",
    "Choix de Victor",
    "Minotaure",
    "Pitaya",
    "Boulangerie de la gare",
]

@app.get("/", response_class=HTMLResponse)
def index():
    choix = random.choice(restaurants)
    html = f"""
    <html>
        <head>
            <title>Choix du resto 🍽️</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #ffecd2, #fcb69f);
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    color: #333;
                }}
                h1 {{
                    font-size: 2em;
                }}
                button {{
                    margin-top: 20px;
                    padding: 10px 20px;
                    border: none;
                    background-color: #ff7f50;
                    color: white;
                    font-size: 1em;
                    border-radius: 8px;
                    cursor: pointer;
                }}
                button:hover {{
                    background-color: #ff4500;
                }}
            </style>
        </head>
        <body>
            <h1>🍽️ Aujourd'hui, on mange chez :<br><b>{choix}</b></h1>
            <form action="/" method="get">
                <button type="submit">🔁 Rejouer</button>
            </form>
        </body>
    </html>
    """
    return html

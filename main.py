from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_seo(product, theme, style):
    prompt = f"""
    Create Etsy SEO for a product.
    Product: {product}
    Theme: {theme}
    Style: {style}

    Return:
    - 13 Etsy tags
    - A 140-character Etsy title
    - A 2-paragraph SEO description
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    return jsonify({
        "result": generate_seo(
            data["product"],
            data["theme"],
            data["style"]
        )
    })

@app.route("/")
def home():
    return "Etsy SEO Generator is live!"

if __name__ == "__main__":
    app.run()

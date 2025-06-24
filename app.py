from flask import Flask, render_template, jsonify
from fashion_catalog import load_catalog, generate_expensive_outfits

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_outfit')
def generate_outfit():
    catalog = load_catalog('/Users/bowenyao/CascadeProjects/fashion_catalog.txt')
    expensive_outfits = generate_expensive_outfits(catalog)
    return jsonify(expensive_outfits)

if __name__ == '__main__':
    app.run(debug=True)

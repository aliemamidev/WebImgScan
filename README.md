# WebImgScan

A lightweight visual audit tool for checking image formats on any webpage.

---

## ✅ What It Does

- Counts the total number of images
- Detects all image formats used (`webp`, `svg`, `jpg`, `png`, `gif`, etc.)
- Highlights whether the site is optimized with efficient formats
- Displays full image URLs with filtering by format
- Tells you if the site is 💚 **Green** (uses only WebP and SVG)

---

## 🚀 Live Demo

_Coming soon... Stay tuned!_

---

## 📦 Features

- Scans and analyzes all `<img>` tags from any given URL
- Groups and counts images by format
- Detects "green" websites (WebP + SVG only)
- Simple, clean UI with filtering by image type
- Built with [Streamlit](https://streamlit.io/) – fast and interactive

---

## 🖼 Example Output

```
📸 Image Format Breakdown:
png: 21 | webp: 10 | gif: 1

🚨 Optimization Tip:
Not all images are in efficient formats. Consider using WebP or SVG.

🌱 Green Site:
Awesome! All images are WebP or SVG.
```

---

## ⚙️ Installation

```bash
git clone https://github.com/aliemamidev/WebImgScan.git
cd webimgscan
pip install -r requirements.txt
streamlit run app.py
```

### 🧪 Requirements

In your `requirements.txt`:

```
streamlit
requests
beautifulsoup4
```

---

## 🧠 Future Ideas

- Show image previews (thumbnails)
- Detect CSS background images
- Analyze image file sizes / lazy loading
- Export detailed report as CSV

---

## 📜 License

**MIT License**  
Use it, fork it, improve it – just keep it geeky 😎

---

## 🤖 Built With

- Python 3
- Streamlit
- BeautifulSoup

---

## ✨ Author

**Ali Emami**  
(with a little help from ChatGPT 🤖 hehe)

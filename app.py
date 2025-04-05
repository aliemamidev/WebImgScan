import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import defaultdict
import re

st.set_page_config(page_title="Image Format Analyzer", page_icon="📸", layout="centered")

# --- Styles ---
st.markdown("""
    <style>
    .image-preview {
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        color: gray;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Helper Functions ---
def get_file_extension(url):
    path = urlparse(url).path
    match = re.search(r'\.([a-zA-Z0-9]+)(?:\?.*)?$', path)
    return match.group(1).lower() if match else None

def fetch_image_data(page_url):
    try:
        response = requests.get(page_url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        return {}, f"❌ Failed to fetch the page: {e}"

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    format_links = defaultdict(list)

    for img in img_tags:
        src = img.get('src')
        if not src:
            continue
        full_url = urljoin(page_url, src)
        ext = get_file_extension(full_url)
        if ext:
            format_links[ext].append(full_url)

    return format_links, None

# --- UI ---
st.title("📸 Image Format Analyzer")
st.caption("Made for developers & designers who care about performance and optimization ✨")

st.divider()

url_input = st.text_input("🔗 Enter a webpage URL", placeholder="https://example.com")
show_images = st.toggle("🖼️ Show Image Previews", value=True)

if url_input:
    with st.spinner("🔍 Fetching and analyzing image formats..."):
        format_links, error = fetch_image_data(url_input)

    st.divider()

    if error:
        st.error(error)
    elif not format_links:
        st.warning("⚠️ No `<img>` tags found on this page.")
    else:
        st.subheader("📊 Image Format Summary")
        total = sum(len(v) for v in format_links.values())
        green_total = len(format_links.get("webp", [])) + len(format_links.get("svg", []))

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Images", total)
        with col2:
            st.metric("Optimized Formats (WebP/SVG)", green_total)

        if total == green_total:
            st.success("✅ Excellent! All images are in WebP or SVG format. Great job! 🌿")
        else:
            st.info(f"🚨 {total - green_total} image(s) could be optimized (e.g., convert to WebP or SVG).")

        st.divider()

        # Format Filter
        st.subheader("🎯 Filter Images by Format")
        formats_available = sorted(format_links.keys())
        selected_format = st.selectbox("Select a format", formats_available)

        if selected_format:
            selected_images = format_links[selected_format]
            st.markdown(f"**{len(selected_images)} image(s) with .{selected_format} format**")

            if show_images:
                for link in selected_images:
                    st.image(link, caption=link, use_column_width=True, output_format="auto", clamp=True)
                    st.markdown("---")
            else:
                for link in selected_images:
                    st.markdown(f"- [🔗 View Image]({link}) `{link}`")

# --- Footer Watermark ---
st.markdown("""
<div class="footer">
    🛠️ Made with ❤️ by <strong>SeyedAli Emami</strong><br>
</div>
""", unsafe_allow_html=True)

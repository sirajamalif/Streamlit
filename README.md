# 📘 Streamlit Frontend Showcase

This project is a collection of everything I’ve learned so far while exploring **Streamlit**.

I wanted to get hands-on with the widgets, layouts, state management, charts, and other features — so I built this app to experiment and try things out in one place.

It’s not a polished product or a tutorial — just something I made while learning.

---

## 🛠 What It Includes

I tried to explore as many parts of Streamlit as I could. Here’s what ended up in the app:

### ✅ Widgets & Inputs

* Text inputs, checkboxes, sliders, radio buttons, toggles
* File uploaders, select boxes, and more

### 🧩 Layout Examples

* Tabs, columns, containers, sidebar
* Placeholders, expanders, popovers, and layout tricks

### 📊 Charts & Data

* Area, line, bar, scatter charts (with random data)
* Matplotlib example
* Editable and static DataFrames
* JSON and dictionary display

### 📋 Forms & Interactivity

* A complete form with input validation
* A multi-step "wizard"-style input flow
* Simple counter with increment and reset
* Sidebar input handling

### ⚙️ Advanced Stuff I Tried

* Session state handling
* Manual rerun (`st.rerun`)
* Caching examples (`st.cache_data`, `st.cache_resource`)
* File handling with append/read mode
* Dynamic widget keys based on state

---

## 🧪 Why I Made This

I wanted to **learn by doing** — not just reading docs or watching videos. So I kept adding small pieces to this app as I discovered more about Streamlit.

It helped me understand:

* How session state works
* How to organize components
* How to build interactive UIs quickly with Python

---

## 💻 How to Run It

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/streamlit-frontend-showcase.git
cd streamlit-frontend-showcase
```

### 2. Install dependencies

```bash
pip install streamlit pandas numpy matplotlib
```

### 3. Run the app

```bash
streamlit run stfront.py
```

---

## 📂 Project Structure

```bash
.
├── stfront.py         # Main file with everything I built
├── example.txt        # Just a test file for the file caching demo
├── pages/             # (Optional) for multipage layout
│   ├── 1_Home.py
│   ├── 2_About.py
│   └── 3_Contact.py
```


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.write("Hello, World!")
x = st.text_input("Enter your name")
st.write(f"Hello, **{x}**")
st.button("Click me!")
st.write("This is a simple Streamlit app.")
3+4 # streamlit magic
python_code = """
import streamlit as st
st.write("This is a code block in Streamlit.")
# to run, write: python -m streamlit run E:\stfront.py
"""
st.code(python_code, language='python')
st.divider()

st.image(r"E:\static\BG.jpg", caption="Image Rendering")

st.divider()

st.subheader("Editable DataFrame:")
data = {
    "name": ["Alex", "Riya", "Jordan", "Mina", "Sam"],
    "age": [24, 30, 27, 22, 29],
    "occupation": ["Engineer", "Designer", "Data Analyst", "Student", "Doctor"]
}
df = pd.DataFrame(data)
editable_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
st.subheader("Static DataFrame:")
st.dataframe(editable_df, use_container_width=True)
st.divider()

st.subheader("Metrics:")
st.metric(label="Total Rows", value=len(editable_df))
st.metric(label="Mean Age", value=editable_df['age'].mean())
st.metric(label="Max Age", value=editable_df['age'].max())
st.divider()

st.subheader("JSON and Dictionary Display:")
sample_dict = [
  {
    "name": "Alex",
    "age": 24,
    "occupation": "Engineer"
  },
  {
    "name": "Riya",
    "age": 30,
    "occupation": "Designer"
  }
]
st.json(sample_dict)
st.write(sample_dict)
st.divider()

# Genarate sample data
chart_data = np.random.rand(20,3)
columns = ['a', 'b', 'c']
df_chart = pd.DataFrame(chart_data, columns=columns)


st.subheader("Area Chart:")
st.area_chart(df_chart)
st.divider()


st.subheader("Line Chart:")
st.line_chart(df_chart)
st.divider()


st.subheader("Bar Chart:")
st.bar_chart(df_chart)
st.divider()


st.subheader("Map:")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)
st.divider()


st.subheader("Scatter Chart:")
st.scatter_chart(df_chart)
st.divider()


st.subheader("Matplotlib Chart:")
fig, ax = plt.subplots()
ax.plot(df_chart['a'], df_chart['b'])
st.pyplot(fig)
st.divider()

# can store form values in dictionary  also
st.header("Streamlit Form Demo")
with st.form("Sample Form"):
    st.write("This is a simple form to demonstrate various input widgets in Streamlit.")
    # text input and text area
    st.subheader("Text Input:")
    text_input = st.text_input("Enter your name:")
    description = st.text_area("Enter a description:")

    # Date and Time Input
    st.subheader("Date and Time Input:")
    date_input = st.date_input("Select a date:",min_value=pd.to_datetime('1900-01-01'), max_value=pd.to_datetime('2025-12-31'))
    # calculate age
    age = pd.to_datetime('today').year - date_input.year
    time_input = st.time_input("Select a time:")

    # selectbox and multiselect
    st.subheader("Selectbox and Multiselect:")
    selectbox_options = ["Male", "Female", "Other"]
    selectbox_value = st.selectbox("Gender", selectbox_options)
    multiselect_options = ["Option A", "Option B", "Option C"]
    multiselect_values = st.multiselect("Select multiple options:", multiselect_options)

    # checkbox and radio button
    st.subheader("Checkbox and Radio Button:")
    checkbox_value = st.checkbox("Check me!")
    radio_button_options = ["Option 1", "Option 2", "Option 3"]
    radio_button_value = st.radio("Select an option:", radio_button_options)  

    # slider and number input
    st.subheader("Slider and Number Input:")
    slider_value = st.slider("Select a value:", 0, 100, 50)
    number_input_value = st.number_input("Enter a number:", min_value=0, max_value=100, step=1) 

    #toggle and file uploader
    st.subheader("Toggle and File Uploader:")
    toggle_value = st.toggle("Toggle me!")
    uploaded_file = st.file_uploader("Upload a file:", type=["csv", "txt"])

    # submit button
    st.subheader("Submit Button:")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        if not all([text_input, description, date_input, time_input, selectbox_value, multiselect_values, checkbox_value, radio_button_value, slider_value, number_input_value]):
            st.error("Please fill in all fields before submitting.")
        else:
          # Display the submitted values
            st.balloons()
            st.success("Form submitted successfully!")
            st.write("Welcome,", text_input)
            st.write("You are a", description)
            st.write(f"You are {age} years old.")
            st.write("Time Input:", time_input)
            st.write("Selectbox Value:", selectbox_value) 
            st.write("Multiselect Values:", multiselect_values)
            st.write("Checkbox Value:", checkbox_value)
            st.write("Radio Button Value:", radio_button_value)
            st.write("Slider Value:", slider_value)
            st.write("Number Input Value:", number_input_value)
            st.write("Toggle Value:", toggle_value)
            if uploaded_file is not None:
                # Read the uploaded file and display its content
                if uploaded_file.type == "text/csv":
                    df_uploaded = pd.read_csv(uploaded_file)
                    st.write("Uploaded CSV Data:")
                    st.dataframe(df_uploaded)
                elif uploaded_file.type == "text/plain":
                    content = uploaded_file.getvalue().decode("utf-8")
                    st.write("Uploaded Text File Content:")
                    st.text(content)
                else:
                    st.warning("Unsupported file type. Please upload a CSV or text file.")

st.divider()
# implementing counter and reset button using session state
st.subheader("Counter Button:")
if "count" not in st.session_state:
    st.session_state.count = 0
def increment_counter():
    st.session_state.count += 1
st.button("Increment Counter", on_click=increment_counter)
st.write("Counter:", st.session_state.count)
def reset_counter():
    st.session_state.count = 0
st.button("Reset Counter", on_click=reset_counter)
st.divider()

# callback function example

# ---------- Initialize session state ----------
if "step" not in st.session_state:
    st.session_state.step = 0
if "name" not in st.session_state:
    st.session_state.name = ""
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "warning" not in st.session_state:
    st.session_state.warning = False

# ---------- Step logic handlers ----------
def next_step():
    name_input = st.session_state.get("name_input", "").strip()
    if name_input == "":
        st.session_state.warning = True
    else:
        st.session_state.name = name_input
        st.session_state.warning = False
        st.session_state.step += 1

def prev_step():
    if not st.session_state.submitted:
        st.session_state.step -= 1

def submit_form():
    st.session_state.submitted = True

# ---------- UI rendering ----------
st.title("Multi-Step Input Wizard 🧙‍♂️")

if st.session_state.step == 0:
    st.subheader("Step 1: What's your name?")
    st.text_input("Enter your name:", key="name_input")
    if st.session_state.warning:
        st.warning("⚠️ Please enter your name before continuing.")
    st.button("Next ➡️", on_click=next_step)

elif st.session_state.step == 1:
    st.subheader("Step 2: Confirm your name")
    st.write(f"✅ You entered: **{st.session_state.name}**")

    col1, col2 = st.columns(2)
    with col1:
        # Only show Back button if not submitted
        if not st.session_state.submitted:
            st.button("⬅️ Back", on_click=prev_step)
    with col2:
        st.button("✅ Submit", on_click=submit_form)

if st.session_state.submitted:
    st.success("🎉 Form submitted successfully!")
    st.write(f"Thanks, **{st.session_state.name}**.")
st.divider()

# Sidebar example
st.sidebar.header("Sidebar")
st.sidebar.write("This is the sidebar content.")
sidebar_input = st.sidebar.text_input("Sidebar Input", "Type here")
st.sidebar.write(f"You entered: {sidebar_input}")
st.sidebar.divider()


# Tabs layout example
st.header("Tabs Layout Example")
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.write("This is Tab 1 content.")
with tab2:
    st.write("This is Tab 2 content.")
with tab3:
    st.write("This is Tab 3 content.")
st.divider()

#columns layout example
col1, col2 = st.columns(2)
with col1:
    st.header("Columns Layout Example")
    st.write("This is Column 1")
with col2:
    st.header("Columns Layout Example")
    st.write("This is Column 2")
st.divider()

# container example
st.header("Container Example")
with st.container(border=True):
    st.write("This is a container.")
    st.write("You can add multiple elements inside a container.")
    st.write("Containers help in managing sections of your page.")
st.divider()

# Empty placeholder example
st.header("Empty Placeholder Example")
placeholder = st.empty()
placeholder.write("This is an empty placeholder.")

if st.button("Update Placeholder"):
    placeholder.write("Placeholder updated with new content!")
    placeholder.write("You can also clear the content using `placeholder.empty()`.")
st.divider()

#  Expander example
st.header("Expander Example")
with st.expander("Click to expand"):
    st.write("This is the content inside the expander.")
st.divider()

# Popover (tooltip) example
st.write("Hover over the button to see a popover.")
st.button("Hover me", help="This is a popover.")
st.divider()

# sidebar input handling
if sidebar_input:
    st.write(f"You entered in the sidebar: {sidebar_input}")

# Advance widget example
# key refers to the unique identifier to access the widget's value. Useful when you have duplicate widgets or want to manage state across reruns.
st.button("Ok")
st.button("Ok",key="unique_button_key")

# slider and session state

if "slider_value" not in st.session_state:
    st.session_state.slider_value = 25

# First slider to set min value
min_value = st.slider("Set min value", 0, 50, 25)

# Make sure the stored value isn't below the new min
if st.session_state.slider_value < min_value:
    st.session_state.slider_value = min_value

# Use a dynamic key based on min_value to force refresh
slider_value = st.slider(
    "Slider with Session State",
    min_value,
    100,
    st.session_state.slider_value,
    key=f"slider_{min_value}"  # 👈 key changes when min_value changes
)

# Update session state
st.session_state.slider_value = slider_value

st.write("Current slider value:", st.session_state.slider_value)

# Advance checkbox example

# Initialize state variables if not already set
if "checkbox" not in st.session_state:
    st.session_state.checkbox = False
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox("Show Input Field", value=st.session_state.checkbox, on_change=toggle_input)

# Use text_input only if checkbox is checked
if st.session_state.checkbox:
    user_input = st.text_input("Enter something:", value=st.session_state.user_input)
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input", "")

st.write(f"User Input: {user_input}")


# Caching example
import time
@st.cache_data(ttl=60)  # Cache for 60 seconds
def fetch_data():
    # Simulate a data fetch operation
    time.sleep(3)
    return{"data": "This is some cached data."}
st.write("Fetching data...")
data = fetch_data()
st.write(data)

# cache resource example
file_path = "example.txt"
@st.cache_resource
def get_file_handler():
    # open file in append mode, which creates the file if it doesn't exist
    file = open(file_path, "a+")
    return file

# Use the cached file handler
file_handler = get_file_handler()
# Write to the file using the cached file handler
if st.button("Write to File"):
    file_handler.write("This is a test line.\n")
    file_handler.flush()  # Ensure data is written to the file
    st.success("Data written to file successfully!")
# Read from the file using the cached file handler
if st.button("Read from File"):
    file_handler.seek(0)  # Reset file pointer to the beginning
    content = file_handler.read()
    st.text(content)
    
st.button("Close File Handler", on_click=file_handler.close)

# manual rerun example
st.title("Counter example with Manual Rerun")

if "count" not in st.session_state:
    st.session_state.count = 0

def increment_and_rerun():
    st.session_state.count += 1
    st.rerun()

st.write("Counter:", st.session_state.count)

if st.button("Increment Counter",key="inc_btn_1"):
    increment_and_rerun()


# Fragments
import streamlit as st

def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle me!")
    cols[1].text_area("Enter text here")

def filter_and_file():
    new_cols = st.columns(5)
    new_cols[0].checkbox("Filter")
    new_cols[1].file_uploader("Upload image")
    new_cols[2].selectbox("Choose option", ["Option 1", "Option 2", "Option 3"])  # Fixed missing bracket
    new_cols[3].slider("Select value", 0, 100, 50)
    new_cols[4].text_input("Enter text")

# Render the app
toggle_and_text()

cols = st.columns(2)
cols[0].selectbox("Select", [1, 2, 3], index=None)  # Use index=None for no default
cols[1].button("Update")

filter_and_file()


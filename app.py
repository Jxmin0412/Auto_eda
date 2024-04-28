import streamlit as st


def main():
    st.title("Uplaod a file")

    # Upload button
    uploaded_file = st.file_uploader("Choose a file")

    # Check if a file was uploaded
    if uploaded_file is not None:
        # Display some information about the uploaded file
        st.write("File details:")
        file_details = {
            "Filename": uploaded_file.name,
            "Filesize": uploaded_file.size,
            "File type": uploaded_file.type,
        }
        st.write(file_details)

        # You can use the uploaded file object as a file-like object
        # For example, you can read the content of the file
        st.write("File content:")
        text = uploaded_file.read()
        st.write(text)

    # Quit button
    if st.button("Quit for Now"):
        st.stop()


if __name__ == "__main__":
    main()

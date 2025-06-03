# Secret Language Encoder / Decoder

This is a simple Python script that lets you convert a message into a "secret language" by reversing the message and adding special tags (`"jkm"` at the start and `"hfj"` at the end). You can also decode the message back to its original form.

---

## How It Works

- If you choose **1**, the script:
  - Reverses your input message
  - Adds `"jkm"` at the start and `"hfj"` at the end to create the secret message

- If you choose **0**, the script:
  - Removes the first 3 and last 3 characters (the tags)
  - Reverses the remaining string to get back the original message

---

## How to Run

1. Run the script:
    ```bash
    python your_script_name.py
    ```
2. Enter your message when prompted.
3. Choose the option:
   - **1** to convert to secret language
   - **0** to convert back to normal language

---

## Example


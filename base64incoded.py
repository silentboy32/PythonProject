import base64


base64_string ="How are you ?"

base64_bytes = base64_string.encode("ascii")

sample_string_bytes = base64.b64decode(base64_bytes)
sample_string = sample_string_bytes.decode("ascii")

print(f"Decoded string: {sample_string}")


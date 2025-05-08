def format_text(txt, pre="", suf="", cap=False, max_len=None):
   # Capitalize if required
   if cap:
       txt = txt.capitalize()


   result = pre + txt + suf


   if max_len is not None:
       if len(result) > max_len:
           available_length = max_len - len(pre) - len(suf)
           if available_length < 0:
               return "Error: max_length too small for the prefix and suffix."
           txt = txt[:available_length]
           result = pre + txt + suf
   return result
# User input
if __name__ == "__main__":
   print("=== Text Formatter ===")


   txt = input("The Main text: ")
   pre = input("The prefix : ")
   suf = input("The suffix : ")
   cap_input = input("Capitalize the first letter? (yes/no): ").strip().lower()
   cap = cap_input == "yes"
   max_input = input("The maximum total length: ")


   # check if max_input is not empty and convert to int
   max_len = int(max_input.strip()) if max_input.strip() else None


   res = format_text(txt, pre, suf, cap, max_len)
   print("\n Formatted text: ", res)



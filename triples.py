Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums = (1, 2, 3, 4, 5, 6, 7) 
... print("Original list: ", nums)
... result = map(lambda x: x + x + x, nums) 
... print("\nTriple of said list numbers:")

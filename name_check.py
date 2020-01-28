def check():
   fh = open(r"D:\Sharv\JAVA\\2.txt", "r")
   word = input("Enter word to search")
   a = word.lower()
   s= " "
   while(s):
      s = fh.readline()
      lower = s.lower()
      if a  in lower:
          print("NAME FOUND")
          break
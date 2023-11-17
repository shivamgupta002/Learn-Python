# ------------------- Write in a file -------------------------

# s="Shivam Is a good boy"

# with open("test.txt","w") as f:
#     f.write(s)

# --------------- or ------------------
# fp=open("test.txt","w")
# fp.write(s)
# fp.close()

# ------------------- Read in a file -------------------------

# with open("test.txt","r") as f:
#     s = f.read()
#     print(s)

# --------------- or ------------------
# fp=open("test.txt","r")
# s=fp.read()
# print(s)
# fp.close()

# ------------------- Appending to a file -------------------------

# s="Shivam Is a good boy"

# with open("test.txt","a") as f:
#     f.write(" and smart")

# --------------- or ------------------
# fp=open("test.txt","a")
# fp.write(" and clever")
# fp.close()
pra = "1, 3, 54, 6565This website has a series of animated short stories to help children learn English with their parents. Each story has a downloadable transcript and an activities pack to help children explore and use the language."

p = ['.', ',', '"', "'", "_", "-", '*', '^', '&', '#', ':', ";", ')', ']', ">", "<",
     '(', '[', "?", "!", "=", "+", "×", "÷", '/', '~', '%', '}', '{', '$', '|', '`', '¡', "'"]
# cw=['is ','are ',' am ',' we ', ' you ', " he ",' she ', ' it ',' were ',' was ', ' has ', ' have ', ' do ', ' did ', ' dose ', ' not ', " doesn't ", " don't ", " of ", " for ", " when ", " where ", " whose ", " who ", " what ", " whome ", " be ", " being ", " can ", " could ", " will ", " would ", " must " , ' much ', 'many ', "too. " ,"how " ," in ", 'out ', ' on ', ' top ', ' and ',' this ', ' that ',' those ',' these ', '  ', ' i ']
cw = ['a', 'an', 'is', 'are', 'am', 'we', 'you', "he", 'she', 'it', 'were', 'was', 'has', 'have', 'do', 'did', 'dose', 'not', "doesn't", "don't", "of", "for", "when", "where", "whose", "who",
      "what", "whome", "be", "being", "can", "could", "will", "would", "must", 'much', 'many', "too", "how", "in", 'out', 'on', 'top', 'and', 'this', 'that', 'those', 'these', '  ', ' i ', 'to', 'the']
# Replace " I " by ""
pra = pra.replace(" I ", " ")
# print(pra)

# remove numbers
for i in range(10):
    pra = pra.replace(str(i), "")

# remove punctuations
for i in p:
    pra = pra.replace(i, "").lower()

# print(pra)

# make list
npra = pra.split(' ')


# remove ""
for i in range(npra.count("")):
    npra.remove("")

 # remove repeation
for i in npra:
    for j in range(npra.count(i)-1):
        npra.remove(i)


# remove cw
i1 = 0
for i in cw:
    i1 = npra.count(i)
    while i1 > 0:
        npra.remove(i)
        i1 -= 1

# Final Output:
print(npra)

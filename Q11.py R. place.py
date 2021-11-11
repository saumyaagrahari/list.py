# When the index is i, then what will be at index length - i -1.

places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
i=1
while i<6:
    # print (places[i])
    print(places[-i])
    i=i+1


# out put
# i	places[i]	length - i	places[length - i]
# 0	"delhi"	4	"kerala"
# 1	"gujrat"	3	"punjab"
# 2	"rajasthan"	2	"rajasthan"
# 3	"punjab"	1	"gujrat"
# 4	"kerala"	0	"delhi"
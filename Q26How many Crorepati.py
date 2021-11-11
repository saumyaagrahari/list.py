
kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]

index = 0
Crorepati_count = 0 
Lakhpati_count = 0
Dilwale_count = 0
while index <len(kitna_paisa_hai):
    c = kitna_paisa_hai[index]
    if c>=10000000:
        Crorepati_count+=1
    elif c>=100000 and c<10000000:
        Lakhpati_count+=1
    else:
        Dilwale_count+=1
    index+=1
print("crorepati_count:",Crorepati_count)
print("lakhpati_count:",Lakhpati_count)
print("dilwale_count:",Dilwale_count)



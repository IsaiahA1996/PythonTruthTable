def truth_table():
    print("p\tq\tp AND q\tp OR q\tNOT p")

    for p in [True, False]:
        for q in [True, False]:
            print(p, "\t", q, "\t", p and q, "\t", p or q, "\t", not p)

truth_table()

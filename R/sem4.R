harvest_data = read.table("harvest.txt",
    header = TRUE, sep = " ", dec = ".")

type_1 = harvest_data[[1]] #ставим двойные скобки, чтобы получить именно столбец значений
type_2 = harvest_data[[2]]
type_3 = harvest_data[[3]]
print(harvest_data[1,])
kruskal.test(list(type_1, type_2, type_3))

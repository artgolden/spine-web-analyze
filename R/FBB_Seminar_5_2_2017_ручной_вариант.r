
#������ �2
#��������� ������ �� �����:
adults = read.table(tk_choose.files(default = ""), header = TRUE, sep = " ", dec = ".")
babies = read.table(tk_choose.files(default = ""), header = TRUE, sep = " ", dec = ".")

#������� ������ ������� 
#NB! � ����������� �� ������� �������� ������ ������� ������� ����� �����������!
ad = adults[[1]]
ba = babies[[1]]
k=2 #���������� �������

#��� ������ ��������� � ���� ������
total = c(adults[[1]], babies[[1]])

wilcox.test(ad, ba, paired = FALSE, alternative = "less", exact = FALSE)

var.test (ad, ba, ratio=1, alternative = "two.sided")

t.test (ad, ba, alternative = "two.sided", mu = 0, paired = FALSE, var.equal = FALSE)

#������� ��������� ������ � �������������� ��������� (��������)
g = factor(rep(1:2, c(n1, n2)), labels = c("adult", "baby"))

#�������� �������� ��������-������� � �������������� ������� ��������
kruskal.test(total, g)

#������ �2
#��������� ������ �� �����:
cows = read.table(tk_choose.files(default = ""), header = TRUE, sep = " ", dec = ".")
#babies = read.table(tk_choose.files(default = ""), header = TRUE, sep = " ", dec = ".")

#������� ������ ������� 
#NB! � ����������� �� ������� �������� ������ ������� ������� ����� �����������!
gr1 = length(nurses[[1]])
gr2 = length(nurses[[2]])
gr3 = length(nurses[[3]])
k=3 #���������� �������

nurses
#��� ������ ��������� � ���� ������
total = c(nurses[[1]], nurses[[2]], nurses[[3]])
total

#������� ��������� ������ � �������������� ��������� (��������)
g = factor(rep(1:3, c(gr1, gr2, gr3)), labels = c("light", "medium", "tought"))

#�������� �������� ��������-������� � �������������� ������� ��������
kruskal.test(nurses)

posthoc.kruskal.dunn.test(cows, p.adjust.method = "none")

#��������� ������� ����� �� �������:
Rteacher = sum(rank(total_school, ties.method = "average")*(g == "teacher"))/n1
Radmin = sum(rank(total_school, ties.method = "average")*(g == "admin"))/n2
Rpersonal = sum(rank(total_school, ties.method = "average")*(g == "personal"))/n3

NNplus1 = (n1 + n2 + n3)*(n1 + n2 + n3 + 1)
alphaNew = 0.05/k/(k-1)
#������� �������� N(0, 1), ������������ ��� ������������� ����������
z = qnorm(alphaNew, mean = 0, sd = 1, lower.tail = FALSE)

#������� �������� ��� �������� �����
#as.factor(total_school): ������ ������������ �������� � total_school ��� ��������(������) �������
#table(as.factor(total_school)): ���������� �������� � total_school �� ��������� ��������� �������,
#�� ���� � ����� ������ �������, ������� � ��� ���� ����� ������� ��������
#as.data.frame(...): ��� �������� ��������� � ������ data.frame
for_B = as.data.frame(table(as.factor(total_school)), row.names = NULL)
#��� ��������� ������������� ������� (������� � ������� ��������):
colnames(for_B) = c("age", "freq")
#������ ����������� �������� �� �������:
#r = ���������� ����� = ���������� ����� � ������� for_B
B_adj = sum(((for_B[["freq"]])^3-(for_B[["freq"]]))/12/ (n1 + n2 + n3 - 1))
#sum: ��������� �� ���� ������� � �������

#���������, � ������� �� ���������� ������ �������� ������� ������ (��� ������������� ���������� ������ n_i)
Right_part = z*sqrt(NNplus1/12 - B_adj)*sqrt(1/n1+1/n2)
Right_part
Rteacher - Rpersonal
Radmin - Rpersonal

#������� p-value ��� ������ ���� �������:
2*pnorm(abs(Rteacher - Radmin)/sqrt(NNplus1/12-B_adj)/(sqrt(1/n1+1/n2)), mean = 0, sd = 1, lower.tail = FALSE)
2*pnorm(abs(Rteacher - Rpersonal)/sqrt(NNplus1/12-B_adj)/(sqrt(1/n1+1/n3)), mean = 0, sd = 1, lower.tail = FALSE)
2*pnorm(abs(Radmin - Rpersonal)/sqrt(NNplus1/12-B_adj)/(sqrt(1/n2+1/n3)), mean = 0, sd = 1, lower.tail = FALSE)






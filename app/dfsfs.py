from random import randint
l = "qw6tyuio2pqwe12ihl21gu671jhdf1722bgdzvydt12uyjfkifdt457hn6as5df657ghj6756klzx5cvbn6mas6"
sk = [l[randint(0, 30)] for t in range(0, 7)]
sk = "".join(sk)
unique_id = str(sk[2:6]) + sk + str(sk)
print(unique_id)
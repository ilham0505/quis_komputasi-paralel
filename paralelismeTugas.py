import multiprocessing
def hitung_total(data):
    print("total:", sum(data))

def hitung_rata_rata(data):
    print("rata-rata:", sum(data) / len(data))

def nilai_terbesar(data):
    print("nilai terbesar:", max(data))

if __name__ == "__main__":
    data = [145, 210, 115, 120, 125]

    p1 = multiprocessing.Process(target=hitung_total, args=(data,))
    p2 = multiprocessing.Process(target=hitung_rata_rata, args=(data,))
    p3 = multiprocessing.Process(target=nilai_terbesar, args=(data,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

import multiprocessing

def proses_data(angka):
    return angka * angka

if __name__ == "__main__":
    data = [182, 154, 146, 128, 110]
    
    with multiprocessing.Pool(processes=4) as pool:
        hasil = pool.map(proses_data, data)

    print("data awal:", data)
    print("hasil:", hasil)
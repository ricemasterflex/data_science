
def fit_knn_scratch_hyperparam(test_run, data, cat_columns, random_seed_adder, distance = 'euclidean'):
    
    import concurrent.futures
    import time

    runs, k_vals = 5, [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
    start = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor(max_workers = 12) as executor:
        futures = [executor.submit(test_run, runs, data, cat_columns, random_seed_adder, k, distance).result() for k in k_vals]

    end = time.perf_counter()
    print(f'finished execution in {(start - end) / 60}.{((start - end) % 60) / 60} min')
    print(str(futures))
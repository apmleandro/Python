
time_hose_red_hour = 2
time_hose_azul_hour = 1.2
time_hose_green_hour = 1

time_hose_red_min = time_hose_red_hour*60
time_hose_azul_min = time_hose_azul_hour*60
time_hose_green_min = time_hose_green_hour*60

Vazao_hose_red = 1/time_hose_red_min
Vazao_hose_azul = 1/time_hose_azul_min
Vazao_hose_green = 1/time_hose_green_min

Vazao_total = Vazao_hose_red + Vazao_hose_azul + Vazao_hose_green

time_total=1/Vazao_total

print(f'The total time to fill the pool with all three hoses will be {time_total}')
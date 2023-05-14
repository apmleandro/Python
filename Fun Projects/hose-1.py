# Atribui um valor as variaves que representam o tempo que a mangueira verde leva para encher a piscina.
time_green = 1.5

# Converte o tempo de horas para minuto
minutes_green = 60 * time_green


# define a vazao da mangueira verde (Volume/tempo). Como os volumes sao iguais, colocamos 1.
rate_hose_green = 1 / minutes_green


# Calcula a vazao total i.e. soma das vazoes de duas mangueiras verdes
rate_host_combined = 2* rate_hose_green 

# Calcula o tempo que levara para encher a mangueira com a vazao total. --- mesma idea do 1 para o volume. Se usassemos volume, o volume cortaria no final, entao nao e necessario.
time = 1 / rate_host_combined

print(time)
# Escreva nesse comentário qual será o valor de time no final da execução do código

print(f'O tempo total para encher a piscina usando duas mangueira verdes simultaneamente e {time} minutos')
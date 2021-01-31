tam_arquivo = float(input("Informe o tamanho do arquivo para download: "))

velocidade = float(input("Informe a velocidade do link em Mbps: "))

total_segundos = tam_arquivo / velocidade


dias = total_segundos // 86400
segundos_rest = total_segundos % 86400
horas = segundos_rest // 3600
segundos_rest = segundos_rest % 3600
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60

print("O tempo que levará para concluir o aquivo é de {0:.0f} dias, {1:.0f} horas, {2:.0f} minutos e {3:.0f} segundos". format(dias, horas, minutos, segundos_rest))



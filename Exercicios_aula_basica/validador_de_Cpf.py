import re
import sys

entrada = input ('digite seu cpf: [746.824.890-70]:  \n')
cpf_enviado_pelo_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)
entrada_sequencial = entrada == entrada[0]*len(entrada)
if entrada_sequencial:
    print (' Voce enviou dados sequenciais')
    sys.exit()

    
nove_digitos = cpf_enviado_pelo_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0



dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -=1
digito_2 = (resultado_digito_2 * 10 ) %11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_pelo_usuario == cpf_gerado_pelo_calculo:
    print (f'{cpf_enviado_pelo_usuario} é valido' )
else:
    print('cpf invalido')
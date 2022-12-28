# bibliotecas
import streamlit as st
from random import randint
import numpy as np

# configuração da página
st.set_page_config(page_title="Número da Sorte", page_icon=':four_leaf_clover:')

st.sidebar.write('Gostou ou se interessou?')
st.sidebar.write('Acesse o repositório no [github.](https://github.com/mmart8997/probabilidade_palpite)')

# cabeçalho
st.write('### **Gerador de números** :four_leaf_clover:')

st.write("""
*Este é um gerador de números para apostas na loteria. Informe os parâmetros do jogo, quantos números você deseja apostar e nós geraremos um palpite com a probabilidade dos números serem sorteados.*
""")

# função para gerar números aleatórios
def gerados(num, total):
    gerados = []
    i = 0
    while i < num:
        i+= 1
        num_gerado = randint(var(),total)
        if num_gerado not in gerados:
            gerados.append(num_gerado)
        else:
            i-= 1
    return(gerados)
    
# função para calcular a probabilidade
def probabilidade(num, total, min):
    try:
        if num == min:
            numerador = np.math.factorial(total)
            denominador = ((np.math.factorial(num))*np.math.factorial(total-num))
            chances = numerador/denominador
    except:
        pass
    
    try:
        if num < min:
            'Você precisa apostar um número maior ou igual a aposta mínima'
    except:
        pass
    
    try:
        if num > min:
            numerador = np.math.factorial(total)/((np.math.factorial(min))*np.math.factorial(total-min))
            denominador = np.math.factorial(num)/((np.math.factorial(min))*np.math.factorial(num-min))
            chances = numerador/denominador
    except:
        pass
    return(chances)

# função para aceite de zero no sorteio
def var():
    if contem_zero == True:
        return 0
    else:
        return 1

# inputs
col1, col2, col3 = st.columns(3)

with col1:
    total = st.number_input(label='Quantos números estão disponíveis?'
                            ,min_value=1
                            ,max_value=99
                            )
    
    contem_zero = st.checkbox('Aposta aceita zero?')
    
    
with col2:
    min = st.number_input(label='Qual é a aposta mínima?'
                            ,min_value=1
                            ,max_value=99
                            )

with col3:
    num = st.number_input(label='Quantos números vai apostar?'
                            ,min_value=1
                            ,max_value=99
                            )


# outputs
result = st.button('Gerar números')

text = 'Sua chance de ganhar com essa aposta é de 1 em '

aposta = gerados(num, total)
aposta.sort()
ordem = str("{:,.0f}".format(probabilidade(num, total, min))).replace(',','.')
try:
    if result == True:
        st.write('#### '+str(aposta).replace(',','-').strip('[]'))
        st.success('*'+text+ordem+'*')
        
        # cálculo
        st.write('Veja como a probabilidade é calculada:')

        if num == min:
                st.latex(r"""
                        Cn,p = \frac{n!}{p!(n-p)!}
                        = C%s,%s = \frac{%s!}{%s!(%s-%s)!} 
                        = %s
                        """%(
                             total
                            ,num
                            ,total
                            ,num
                            ,total
                            ,num
                            ,ordem
                            )
                        )
        else:
            pass

        if num > min:
            st.latex(r"""
                    Cn,p = \frac{n!}{p!(n-p)!} 
                    = C%s,%s = \frac{%s!}{%s!(%s-%s)!}
                    = %s"""%(
                             num
                            ,min
                            ,num
                            ,min
                            ,num
                            ,min
                            ,str("{:,.0f}".format(np.math.factorial(num)
                                            /((np.math.factorial(min))
                                            *np.math.factorial(num-min)))).replace(',','.')
                            )
                    )
            st.latex(r"""
                     = \frac{%s}{%s}
                     = %s
                     """%(
                        str("{:,.0f}".format(np.math.factorial(total)
                                        /((np.math.factorial(min))
                                        *np.math.factorial(total-min)))).replace(',','.')
                        ,str("{:,.0f}".format(np.math.factorial(num)
                                        /((np.math.factorial(min))
                                        *np.math.factorial(num-min)))).replace(',','.')
                        ,ordem
                        )
                    )
        else:
            pass
except:
    pass



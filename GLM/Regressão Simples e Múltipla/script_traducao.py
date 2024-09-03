#%%
import time
from googletrans import Translator

translator = Translator()

code = """
# In[1.1]: Gráfico de dispersão com o ajuste linear (fitted values de um modelo
#de regressão) que se adequa às observações: função 'regplot' do pacote 'seaborn'

plt.figure(figsize=(15,10))
sns.regplot(data=df_tempodist, x='distancia', y='tempo', marker='o', ci=False,
            scatter_kws={"color":'navy', 'alpha':0.9, 's':220},
            line_kws={"color":'grey', 'linewidth': 5})
plt.title('Valores Reais e Fitted Values (Modelo de Regressão)', fontsize=30)
plt.xlabel('Distância', fontsize=24)
plt.ylabel('Tempo', fontsize=24)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.xlim(0, 35)
plt.ylim(0, 60)
plt.legend(['Valores Reais', 'Fitted Values'], fontsize=24, loc='upper left')
plt.show
"""

def translate_comment(comment, translator, retries=5, delay=2):
    for attempt in range(retries):
        try:
            translated_comment = translator.translate(comment,
                                                      src='pt', dest='en').text
            return translated_comment
        except Exception as e:
            print(f"Erro ao traduzir: {e}. Tentativa {attempt + 1} de {retries}.")
            time.sleep(delay)
    return comment

def translate_comments(code, translator):
    lines = code.split('\n')
    translated_code = []
    for line in lines:
        if '#' in line:
            code_part, comment_part = line.split('#', 1)
            translated_comment = translate_comment(comment_part.strip(), translator)
            translated_code.append(f"{code_part.strip()} # {translated_comment}")
        else:
            translated_code.append(line)
    return '\n'.join(translated_code)

translated_code = translate_comments(code, translator)
print(translated_code)

#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:





# In[3]:


from flask import Flask, render_template, request
import openai

app = Flask(__name__, template_folder='templates')

openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/imc', methods=['GET', 'POST'])
def imc():
    if request.method == 'POST':
        altura = request.form['altura']
        peso = request.form['peso']
        resultado = int(calcular_imc(altura, peso))

        # Utilizando o resultado do IMC como input para o ChatGPT
        prompt = f"O IMC de uma pessoa é igual a {resultado}. O que esse resultado diz sobre a saúde dessa pessoa? Liste ações que essa pessoa deve tomar para melhorar a sua saúde"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=2048,
            n = 1,
            stop=None,
            temperature=0.5,
        )
        print(response)
        resultado_chat = response["choices"][0]["text"]

        return render_template('imc_result.html', resultado=resultado, resultado_chat=resultado_chat)
    else:
        return render_template('imc_form.html')

def calcular_imc(altura, peso):
    altura = float(altura)
    peso = float(peso)
    imc = peso / (altura * altura)
    return imc

if __name__ == '__main__':
    app.run(host='0.0.0.0')


# In[ ]:





# In[ ]:





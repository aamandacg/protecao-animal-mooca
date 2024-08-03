import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF

# 1. Obtenção dos Dados
dados_socioeconomicos = pd.read_csv('../data/dados_socioeconomicos_mooca.csv')

# 2. Tratamento e Limpeza dos Dados
dados_limpos = dados_socioeconomicos.drop(columns=['ColunaIrrelevante'])
dados_limpos = dados_limpos.fillna(method='ffill')
dados_limpos['RendaMedia'] = dados_limpos['RendaFamiliar'].apply(lambda x: x.replace('R$', '').replace(',', '').astype(float))

# 3. Análise dos Dados
media_renda = dados_limpos['RendaMedia'].mean()
print(f"Renda Média: R$ {media_renda:.2f}")

# 4. Visualização dos Dados
plt.figure(figsize=(10, 6))
sns.barplot(x='Bairro', y='RendaMedia', data=dados_limpos)
plt.title('Renda Média por Bairro')
plt.xlabel('Bairro')
plt.ylabel('Renda Média')
plt.xticks(rotation=45)
plt.savefig('../results/renda_media_por_bairro.png')
plt.show()

# 5. Treinamento dos Colaboradores
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Guia de Uso das Visualizações de Dados', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()
pdf.chapter_title('Introdução')
pdf.chapter_body('Este guia fornece instruções sobre como usar as visualizações de dados criadas...')
pdf.output('../guia/guia_de_uso.pdf')

# %%
import pandas as pd
import functions as funcao

# %%
def train_model():
    df = pd.read_csv('/app/data_base/atividade-2-churn-internet.csv')

    print("Quantidades linhas e colunas:")
    funcao.data_old(df)

    print("Tratamento de dados:")
    print(funcao.data_analytics(df.head()))

    print("Tratamento de dados:")
    df = funcao.data_treatment(df)

    print("Treinando o modelo:")
    model, data_train, data_test, target_train, target_test = funcao.good_model(df)

if __name__=='__main__':
    train_model()
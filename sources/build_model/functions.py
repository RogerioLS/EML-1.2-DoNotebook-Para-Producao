# %%
import pandas as pd
import numpy as np
import pickle

from time import sleep
from tqdm import tqdm

import matplotlib.pyplot as plt

# Utilizado para transformar variaveis categoricas em numericas
from sklearn.compose import make_column_transformer as transformer

# Utilizado para separar nossos dados em treino e teste
from sklearn.model_selection import train_test_split

# Utilizado para padronizar os dados
from sklearn.preprocessing import StandardScaler

# Utilizado para montar o pipeline de dados
from sklearn.pipeline import make_pipeline

# Tipos de modelos de ML Classificação
from xgboost import XGBClassifier

# Mostra a estrutura do pipeline
from sklearn import set_config
set_config(display='diagram')

# Plot para analise de desempenho do modelo
from yellowbrick.classifier import ROCAUC
from yellowbrick.classifier import ConfusionMatrix

#
from sklearn.impute import SimpleImputer

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

# Exibir todas as colunas no data frame
pd.options.display.max_columns = None

# %%
def data_old(df):
    """
    Brief
    ----------
    Está função foi criada para exibir a quantidades de linhas e colunas no
    data set.
    Return
    ----------
    Retorna o data frame total.
    """

    print(f"O dataset contém {df.shape[0]} amostras e "f"{df.shape[1]} colunas")
    return df


def data_analytics(df):
    """
    Brief
    ----------
    Está função foi criada para realizar a exibição de dados faltantes,
    percentual de dados faltantes qual é o tipo do dado, e describe desses
    dados.
    Return
    ----------
    Retorna o data frame de analise para dados faltante, quartis, média, std.
    """

    for i in tqdm(range(0, 100), desc ="Create column null"):
        df_null = (pd.DataFrame(df.isnull().sum(),
                columns = ['quantities number null'])
                .rename_axis('Columns')
                .reset_index())
                #df_null.reset_index(level=0, inplace=True)
        sleep(.05)


    for i in tqdm(range(0, 100), desc ="Creating column missing"):
        df_missing = (pd.DataFrame((df.isnull().sum() / len(df))*100,
            columns = ['percentage data missing'])
            .rename_axis('Columns')
            .reset_index())
        sleep(.05)


    for i in tqdm(range(0, 100), desc ="Creating column type data"):
        df_type = (pd.DataFrame(df.dtypes,
                columns = ['data type'])
                .rename_axis('Columns')
                .reset_index())
        sleep(.05)


    for i in tqdm(range(0, 100), desc ="Creating column describe"):
        df_describe = (pd.DataFrame(df.describe(include="all").transpose()
                .rename_axis('Columns'))
                .reset_index())
        sleep(.05)

    df_1 = pd.merge(df_null, df_missing)
    df_2 = pd.merge(df_1, df_type)
    df   = pd.merge(df_2, df_describe)

    return df

def data_treatment(df):
    """
    Brief
    ----------
    Está função foi criada para realizar tratamento de dados tais como:
    * Dados faltante;

    Return
    ----------
    Retorna um novo data frame tratado.
    """
    df.drop('id', axis = 1, inplace = True)
    df['download_avg'] = df['download_avg'].interpolate()
    df['upload_avg'] = df['upload_avg'].interpolate()
    df['reamining_contract'].fillna(0.00, inplace = True)
    df['reamining_contract'] = np.where(df['reamining_contract'] != 0.00, 1, 0)

    return df


def plot_churn(df):
    """
    Brief
    ----------
    Está função foi criada para realizar plot dos dados do nosso target.
    Return
    ----------
    Retorna plot de churn.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)

    df['churn'].value_counts().plot(kind='bar',
                                    color=['#be4d25','#49be25'],
                                    figsize=(10,5),
                                    rot = 0,
                                    title="Churn");

    plt.xlabel("1 - Verificações de churn |  0 -  Verificações de não churn");
    plt.ylabel("Quantidade");
    for p in ax.patches:
        ax.annotate('{:.2f}%'.format(100 * p.get_height() / df.shape[0]),
                    (p.get_x() + 0.20, p.get_height() + 30))
    plot = plt.show()

    return plot

def good_model(df):
    """
    Está função criada para gerarmos a construção do pipeline do nosso modelo e o que utilizamos para isso:

    * selector -> Para selecionar o tipo das nossas feature;
    * train test split -> Para separar nosso conjunto de treino e teste;
    * 7 modelos lineares -> KNeighborsRegressor(), DecisionTreeRegressor(), RandomForestRegressor(),
                            AdaBoostRegressor(), GradientBoostingRegressor(), LinearRegression(), linear_model.LassoCV().
    * transformer -> Para transformar e normalizar nossos dados de treinamento;
    * make_pipeline -> Orquestrador de pipeline;
    * ShuffleSplit -> Metodo de validação cruzada;
    * cross_val_score -> Utilizado para output de metricas do modelo;
    """

    numerical_columns = ['is_tv_subscriber', 'is_movie_package_subscriber', 'subscription_age',
                         'bill_avg', 'reamining_contract', 'service_failure_count', 'download_avg',
                         'upload_avg', 'download_over_limit']

    target_column = 'churn'

    data_numeric, target = df[numerical_columns], df[target_column]

    data_train, data_test, target_train, target_test = train_test_split(
        data_numeric, target, random_state=42, test_size=0.25)

    # Usando XGBClassifier, que é compatível com a interface do scikit-learn
    classifier = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

    # Pipeline para transformação e classificação
    pipeline = make_pipeline(SimpleImputer(strategy='mean'), StandardScaler(), classifier)

    pipeline.fit(data_train, target_train)

    with open('modelo_churn.pkl', 'wb') as file:
        pickle.dump(pipeline, file)
    
    print("Modelo salvo como 'modelo_churn.pkl'")

    return pipeline, data_train, data_test, target_train, target_test

def plotarMatrizConfusao(model, classes, X_train, X_test, y_train, y_test):
    plt.figure(figsize=(4,4))
    ax = plt.axes()
    matriz = ConfusionMatrix(model, classes=classes, percent=True)
    matriz.fit(X_train, y_train)
    matriz.score(X_test, y_test)
    mat = matriz.show()

    return mat


def plotarCurvaROC(model, X_train, X_test, y_train, y_test):
    plt.figure(figsize=(4,4))
    ax = plt.axes()
    viz = ROCAUC(model)
    viz.fit(X_train, y_train)
    viz.score(X_test, y_test)
    vi = viz.show()

    return vi
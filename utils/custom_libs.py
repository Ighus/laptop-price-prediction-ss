import pandas as pd

def contar_valores_unicos(df: pd.DataFrame) -> pd.Series:
    """
    Conta quantos valores únicos existem em cada coluna do DataFrame,
    convertendo listas para tuplas para evitar o erro 'unhashable type: list'.

    Parâmetros:
        df (pd.DataFrame): DataFrame a ser analisado.

    Retorna:
        pd.Series: Série com as contagens de valores únicos por coluna.
    """
    return df.apply(lambda col: col.apply(lambda x: tuple(x) if isinstance(x, list) else x).nunique())

def show_unique_values(df, max_values=10):
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, list)).any():
            df[col] = df[col].apply(lambda x: str(x) if isinstance(x, list) else x)

        unique_values = df[col].dropna().unique()  # Valores únicos, ignorando NaNs
        unique_count = len(unique_values)

        print(f"Column: {col}")
        print(f"Total Unique Values: {unique_count}")
        print(f"Type: {type(col)}")

        if unique_count > max_values:
            print(f"Sample of {max_values} unique values (and {unique_count - max_values} more):")
            print(unique_values[:max_values])  # Mostra apenas os primeiros 'max_values'
        else:
            print("Unique Values:")
            print(unique_values)

        print("-" * 50)
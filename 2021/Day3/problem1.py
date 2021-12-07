import pandas as pd
mode = (
    pd
        .read_csv('2021/Day3/input.txt', dtype=str, header=None)[0]
        .apply(lambda x: pd.Series(list(x)))
        .mode().astype('int')
)
gamma = int(mode.applymap(str).iloc[0].str.cat(), 2)
epsilon = int(mode.applymap(lambda x: str(x ^ int('0b1', 2))).iloc[0].str.cat(), 2)
print(gamma * epsilon)


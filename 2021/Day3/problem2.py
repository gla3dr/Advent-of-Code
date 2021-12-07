import pandas as pd
df = (
    pd
        .read_csv('2021/Day3/input.txt', dtype=str, header=None)[0]
        .apply(lambda x: pd.Series(list(x)))
        .astype('int')
)

o2df = df
co2df = df
for i in range(df.shape[1]):
    if o2df.shape[0] > 1:
        mode = o2df.iloc[:, i].mode().max()
        o2df = o2df[o2df.iloc[:, i] == mode]
    
    if co2df.shape[0] > 1:
        antimode = co2df.iloc[:, i].mode().max() ^ int('0b1', 2)
        co2df = co2df[co2df.iloc[:, i] == antimode]

o2 = int(o2df.applymap(str).iloc[0].str.cat(), 2)
co2 = int(co2df.applymap(str).iloc[0].str.cat(), 2)
print(o2, co2, o2 * co2)
from task2 import file_name
from task3 import list_scores, result_valid_df


df = result_valid_df
score = list_scores
df_result = df.assign(score=score).loc[:,["ID","score"]]

f = open(f'{file_name}_grades.txt', 'w')
f.write(str(df_result))
f.close()


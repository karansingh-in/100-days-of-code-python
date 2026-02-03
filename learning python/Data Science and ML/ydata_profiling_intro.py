from ydata_profiling import ProfileReport
import pandas as pd
df = pd.read_csv('./train.csv')
pr = ProfileReport(df)
pr.to_file(output_file='output.html')
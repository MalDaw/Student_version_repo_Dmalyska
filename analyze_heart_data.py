import pandas as pd
import json
 
 #Własna poprawka: output w formacie .json
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)
 
 
def basic_report(df: pd.DataFrame) -> dict:
    numeric_df = df.select_dtypes(include=['number'])
    
    report = {
        'shape': {'rows': len(df), 'columns': len(df.columns)},
        'memory_usage_kb': float(df.memory_usage(deep=True).sum() / 1024), 
        'duplicate_rows': int(df.duplicated().sum()),
        
        'missing_data': {
            'total': int(df.isna().sum().sum()),
            'by_column': df.isna().sum()[df.isna().sum() > 0].astype(int).to_dict()
        },
        
        'data_types': df.dtypes.astype(str).value_counts().to_dict(),
        
        'numeric_stats': {
            'averages': numeric_df.mean().round(2).to_dict(),
            'std_dev': numeric_df.std().round(2).to_dict(),
        }
    }
    return json.loads(json.dumps(report, default=str)) 

 
 
if __name__ == '__main__':
    path = 'data\\Data.csv'
    data = load_data(path)
    print(json.dumps(basic_report(data), indent=4))
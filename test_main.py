import lib
import pandas as pd

def testMain():
    df_raw = pd.read_csv('Dataset.csv', header = 0)
    df = df_raw[(df_raw['YEAR']>=1990)&(df_raw['YEAR']<=2010)].copy()
    
    #France
    df_fra = df[df['COUNTRY_REGION']=='FRA'].copy()
    assert lib.calMean(df_fra, 'GDP per Capita') >= 29206.775
    assert lib.calMean(df_fra, 'GDP per Capita') <= 29206.784
    assert lib.calMedian(df_fra, 'Suicide Rate') >= 16.475
    assert lib.calMedian(df_fra, 'Suicide Rate') <= 16.484
    
    #Albania
    df_alb = df[df['COUNTRY_REGION']=='ALB'].copy()
    df_alb_medium = df_alb[(df_alb['Suicide Rate']>=5)&(df_alb['Suicide Rate']<15)]
    assert df_alb_medium.shape[0] == 2
    df_alb_low = df_alb[df_alb['Suicide Rate']<5]
    assert df_alb_low.shape[0] == 16
    pass

if __name__ == '__main__':
    testMain()
    pass


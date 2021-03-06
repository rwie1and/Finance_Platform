
import pandas as pd


def to_numeric_(object_):
    def _decorator(fn):
        '''
        Decorator change type to numeric
        '''
        def wrapper(self):

            dataframe_ = getattr(self, str(object_))

            for col in dataframe_:
            #for col in self.df_index.columns:
                try:
                    #self.df_index[col] = pd.to_numeric(self.df_index[col])
                    dataframe_[col] = pd.to_numeric(dataframe_[col])

                except:
                    continue

            return fn(self)
        return wrapper
    return _decorator

def cleaning_dataframe(df):
    '''
    - round to 4 digits
    '''
    try:
        df.drop(columns='index', inplace=True)
    except Exception:
        pass


    df = df.round(4).astype(str)
    df.drop_duplicates(inplace=True, ignore_index=True)
    df = df[30:] # drop first 30 entries -> windows for rolling figures not longer

    return df
